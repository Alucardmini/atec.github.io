# -*- coding:utf-8 -*-
# @version: 1.0
# @author: wuxikun
# @date: '5/6/18'

# documents = ["怎么 更改 花呗 手机号码"]
# new_doc="我的 花呗 以前 手机号码 怎么 更改 现在 支付宝 号码"


from gensim import corpora,models,similarities

#nine documents,each consisting of only a single sentence
# documents = ["Human machine interface for lab abc computer applications",
#              "A survey of user opinion of computer system response time",
#              "The EPS user interface management system",
#              "System and human system engineering testing of EPS",
#              "Relation of user perceived response time to error measurement",
#              "The generation of random binary unordered trees",
#              "The intersection graph of paths in trees",
#              "Graph minors IV Widths of trees and well quasi ordering",
#              "Graph minors A survey"]
# new_doc="Human computer interaction"

# documents = [u'怎么 更改 花呗 手机号码',u'花呗 手机号码 怎么 更改 现在 支付宝 号码']
documents = [u'怎么 更改 花呗 手机号码',u'花呗 手机号码 怎么 更改 现在 支付宝 号码']
first_doc=u'怎么 更改 花呗 手机号码'

second_doc=u'花呗 手机号码 怎么 更改 现在 支付宝 号码 '
# new_doc=u'怎么 更改 花呗 手机号码'


#remove commen words and tokenize
stoplist=set('for a of the and to in'.split())
texts=[[word for word in document.lower().split() if word not in stoplist]
		for document in documents]

#remove words that appear only once
from collections import defaultdict
frequency=defaultdict(int)
for text in texts:
	for token in text:
		frequency[token]+=1

texts=[[token for token in text if frequency[token]>=1]
		for text in texts]


from pprint import pprint
print "--- texts ---"
pprint(texts)

dictionary=corpora.Dictionary(texts)
# dictionary.save('/tmp/deerwester.dict') #store the dictionary,for future reference

print "--- dictionary ---"
print(dictionary)
print "--- token2id ---"
print(dictionary.token2id)

# new_doc="我的 花呗 以前 手机号码 怎么 更改 现在 支付宝 号码"
# new_doc="怎么 更改 花呗 手机号码"

# new_doc="Human computer interaction"


#the word 'interaction' does not appear in the dictionary and is ignored
second_vec=dictionary.doc2bow(second_doc.lower().split())
print "--- second_vec ---"
print(second_vec)

print "--- first_doc ---"
print first_doc.lower().split()

first_vec = dictionary.doc2bow(first_doc.lower().split())
print "--- first_vec ---"
print first_vec


corpus = [dictionary.doc2bow(text) for text in texts]
# corpora.MmCorpus.serialize('/tmp/deerwester.mm',corpus) #store to dist,for later use
pprint(corpus)


#set tfidf model
tfidf=models.TfidfModel(corpus)

featureNum=len(dictionary.token2id.keys())
index = similarities.SparseMatrixSimilarity(tfidf[corpus], num_features=featureNum)
print ('---- tfidf[new_vec] ----')
print tfidf[second_vec]

print ('---- tfidf[first_vec] ----')
print tfidf[first_vec]

vec = [(0, 1), (1, 1), (2, 1), (3, 1), (4, 1), (5 , 1)]
print(tfidf[vec])

sims=index[tfidf[second_vec]]

print ('---- result ----')
print(sims)



lsi = models.LsiModel(corpus, id2word=dictionary, num_topics=2)
first_lsi = lsi[first_vec]
print first_lsi

second_lsi = lsi[second_vec]
print second_lsi

index = similarities.MatrixSimilarity(lsi[corpus])
print index
