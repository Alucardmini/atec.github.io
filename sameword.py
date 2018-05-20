# -*- coding:utf-8 -*-
# @version: 1.0
# @author: wuxikun
# @date: '5/12/18'
import sys
import pickle
reload(sys)
sys.setdefaultencoding('utf8')  # 设置默认编码格式为'utf-8'

def get_sym(w):
    inpath = 'wordnet.txt'
    f = open('wordnet2', 'r')
    lines = f.readlines()
    sym_word = []
    sym_class_word = []
    for line in lines:
        items = line.split(' ')
        index = items[0]
        if '=' == index[-1]:
            sym_word.append([items[1:]])
        if '#' == index[-1]:
            sym_class_word.append([items[1:]])
    result = []
    if (len(w) == 1):
        for each in sym_word:
            for word in each:
                if w == word:
                    result.append(each)
                    break
    else:
        for each in sym_word:
            for word in each:
                if w in word:
                    result.append(each)
                    break

    return result


if __name__ == "__main__":

    while True:
        w = raw_input()
        print (str(u'同义词').decode('string_escape'), 66 * '*')
        print str(get_sym(w)).decode('string_escape')