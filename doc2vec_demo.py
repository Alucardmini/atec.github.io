# -*- coding:utf-8 -*-
# @version: 1.0
# @author: wuxikun
# @date: '5/6/18'


import gensim
import os
import collections
import smart_open
import random
import gensim.utils

test_data_dir = '{}'.format(os.sep).join([gensim.__path__[0], 'test', 'test_data'])
lee_train_file = test_data_dir + os.sep + 'lee_background.cor'
lee_test_file = test_data_dir + os.sep + 'lee.cor'


def read_corpus(fname, tokens_only=False):
    with smart_open.smart_open(fname, encoding="iso-8859-1") as f:
        for i, line in enumerate(f):
            if tokens_only:
                yield gensim.utils.simple_preprocess(line)
            else:
                # For training data, add tags
                yield gensim.models.doc2vec.TaggedDocument(gensim.utils.simple_preprocess(line), [i])

train_corpus = list(read_corpus(lee_train_file))
test_corpus = list(read_corpus(lee_test_file, tokens_only=True))

# print train_corpus[:2]

# model = gensim.models.doc2vec.Doc2Vec(vector_size=50, min_count=2)
data = ['only', 'you', 'can','not', 'prevent', 'forest', 'fires']
train_corpus = gensim.models.doc2vec.TaggedDocument(data, [0])

model = gensim.models.doc2vec.Doc2Vec(size=10, alpha=0.025, min_alpha=0.025)  # use fixed learning rate
model.build_vocab(train_corpus)


print model.infer_vector(['only', 'you', 'can', 'prevent', 'forest', 'fires'])

print model.infer_vector(['only', 'you', 'can', 'not', 'prevent', 'forest', 'fires'])
