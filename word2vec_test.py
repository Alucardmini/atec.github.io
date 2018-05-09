# -*- coding:utf-8 -*-
# @version: 1.0
# @author: wuxikun
# @date: '5/9/18'

from gensim.models import Word2Vec


if __name__ == "__main__":
    sentences = [["cat", "say", "meow"], ["dog", "say", "woof"]]
    model = Word2Vec(sentences, min_count=1,size=5)
    say_vector = model["say"]
    print say_vector
