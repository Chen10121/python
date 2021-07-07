#001
'生成200个激活码'
import random
filepath = r'C:\Users\MAC\Documents\GitHub\python\activation_code.txt'
def activation_code():
    with open(filepath,'r') as f:
        sum_code = f.readlines()
        for i in range(200):
            index = random.randint(0,len(sum_code))
            print(sum_code[index])
