#004
'统计单词个数'
import collections
def words_number(filepath):
    with open(filepath,'r') as f:
        chars = f.read().split()
        num = 0
        dict = collections.Counter(chars)
        for words in dict:
            print('%s的个数为%s' % (words,dict[words]))
            num += dict[words]
        print('单词总个数为',num)

Filepath = r'C:\Users\MAC\Documents\GitHub\python\eng_sentence.txt'
words_number(Filepath)
