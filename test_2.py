# -*- coding:utf-8 -*-
# @version: 1.0
# @author: wuxikun
# @date: '5/5/18'

from collections import namedtuple
import numpy as np
import math

from gensim.models.doc2vec import Doc2Vec,LabeledSentence



#!/usr/bin/env python
# -*- coding: utf-8 -*-
# created by fhqplzj on 2017/06/30 上午11:34
"""
Doc2Vec简单例子
"""
import os
import random
import time
from collections import Counter

import gensim
import gensim.utils
import smart_open

from gensim import corpora, models, similarities
from collections import defaultdict
from pprint import pprint  # pretty-printer

documents = ["Human machine interface for lab abc computer applications",
             "A survey of user opinion of computer system response time",
             "The EPS user interface management system",
             "System and human system engineering testing of EPS",
             "Relation of user perceived response time to error measurement",
             "The generation of random binary unordered trees",
             "The intersection graph of paths in trees",
             "Graph minors IV Widths of trees and well quasi ordering",
             "Graph minors A survey"]

stoplist = set('for a of the and to in'.split())
texts = [[word for word in document.lower().split() if word not in stoplist]
          for document in documents]
frequency = defaultdict(int)

for text in texts:
    for token in text:
        frequency[token] += 1
texts = [[token for token in text if frequency[token] > 1]
         for text in texts]
pprint(texts)

dictionary = corpora.Dictionary(texts)
print(dictionary.token2id)

new_doc = "Human computer interaction"
new_vec = dictionary.doc2bow(new_doc.lower().split())
print new_vec