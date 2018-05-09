#/usr/bin/env python
# -*- coding: utf-8 -*-
import jieba
import sys
import gensim
from collections import namedtuple
import numpy as np
from gensim.models import doc2vec
import math

reload(sys)
sys.setdefaultencoding('utf-8')

TaggededDocument = gensim.models.doc2vec.TaggedDocument
from gensim.models.doc2vec import LabeledSentence

##读取向量
def getVecs(model, corpus, size):
    vecs = [np.array(model.docvecs[z.tags[0]]).reshape((1, size)) for z in corpus]
    return np.concatenate(vecs)

def getStopList ():
    stoplist = set()
    with open('stopwords.txt', 'r') as f:
        for line in f:
            stoplist.add(line.strip())
    return stoplist

def process(inpath, outpath):

    # stoplist = set([u'，', u'? ', u') ', u'( ', u'. ', u'。', u'?', u'\ufeff'])

    stoplist = getStopList()

    # 判断正确的选项
    accury_count = 0
    sum_count = 0
    jieba.add_word("花呗")
    jieba.add_word("借呗")
    jieba.add_word("蚂蚁借呗")
    jieba.add_word("蚂蚁借呗")
    jieba.add_word("还蚂蚁借呗")
    jieba.add_word("还蚂蚁借呗")
    jieba.add_word("还借呗")
    jieba.add_word("还花呗")
    jieba.add_word("还钱")
    jieba.add_word("更改")
    jieba.add_word("哈罗单车")
    texts = set()
    # 建立word2vec
    AnalyzedDocument = namedtuple('AnalyzedDocument', 'words tags')

    with open(inpath, 'r+') as fin, open(outpath, 'w') as fout:
        for line_test in fin:
            sum_count += 1
            docs = []
            word_set = set()
            line = line_test.encode('utf-8').decode('utf-8-sig')
            lineno, sen1, sen2, result = line.strip().split('\t')
            words1 = [w for w in jieba.cut(sen1) if w.strip() and str(w.strip()) not in stoplist and w != u'\ufeff']
            words2 = [w for w in jieba.cut(sen2) if w.strip() and str(w.strip()) not in stoplist and w != u'\ufeff']
            # model = Doc2Vec(words1, size=100, window=8, min_count=2, workers=2)

            for word in words1:
                word_set.add(word)
            for word in words2:
                word_set.add(word)

            docs.append(AnalyzedDocument(words1, [0]))
            docs.append(AnalyzedDocument(words2, [1]))
            size = len(word_set)
            # model = doc2vec.Doc2Vec(docs, size=50, window=1, min_count=1, workers=1)
            model = doc2vec.Doc2Vec(documents=docs, size=100, dm=1, min_count=1, workers=2)
            vec1 = np.array(model.docvecs[0])
            vec2 = np.array(model.docvecs[1])

            # ||vec1||
            vec1_v = math.sqrt(np.sum(vec1 ** 2))
            # ||vec2||
            vec2_v = math.sqrt(np.sum(vec2 ** 2))

            sim = np.sum(np.multiply(vec1, vec2)) / (vec1_v * vec2_v)

            if sim >= 0.5 and result == '1':
                accury_count += 1
                fout.write(lineno + '\t1\n')
            elif sim <= 0.5 and result == '0':
                accury_count += 1
                fout.write(lineno + '\t0\n')

            # for word in words1:
            #     if len(word) > 0 and word != u'\ufeff' and word.strip() not in stoplist:
            #         texts.add(word)
            # for word in words2:
            #     if len(word) > 0 and word != u'\ufeff' and word.strip() not in stoplist:
            #         texts.add(word)


    # model = gensim.models.Word2Vec(texts)

    # dictionary = corpora.Dictionary(texts)
    # dictionary.save('/tmp/deerwester.dict')
    # with open(inpath, 'r') as fin, open(outpath, 'w') as fout:
    #
    #     for line in fin:
    #         sum_count += 1
    #         lineno, sen1, sen2, result = line.strip().split('\t')
    #         words1= [ w for w in jieba.cut(sen1) if w.strip() ]
    #         words2= [ w for w in jieba.cut(sen2) if w.strip() ]
    #         union = words1 + words2
    #         same_num = 0
    #         for w in union:
    #             if w in words1 and w in words2:
    #                 same_num += 1
    #         if same_num * 2 >= len(union) and result == '1':
    #             accury_count += 1
    #             fout.write(lineno + '\t1\n')
    #         elif same_num * 2 <= len(union) and result == '0':
    #             accury_count += 1
    #             fout.write(lineno + '\t0\n')

    print float(accury_count)/sum_count

if __name__ == '__main__':
    # process(sys.argv[1], sys.argv[2])
    process("atec_nlp_sim_train.csv", "result.csv")