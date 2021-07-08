#Joseph_2.2
import random

#创建对象的类
class Person:
    def __init__(self,name,stu_number,gender):
        self.name = name
        self.stu_number = stu_number
        self.gender = gender

#类的实例化
list_name = ['A','B','C','D','E','F','G','H','I','J','K']
list_number = list(range(202001,202012))
list_gender = ['male','female']
for i in range(0,11):
    globals()[list_name[i]] = Person(list_name[i],list_number[i],list_gender[random.randint(0,1)])

#将实例化后的对象存在定义的列表中
joslist = list(range(0,11))
for i in range(0,11):
    joslist[i] = globals()[list_name[i]]

#定义约瑟夫环类型
class Joseph:
    def __init__(self,josephlist):          #josephlist由实例化的对象列表提供
        self.josephlist = josephlist

    def Josephring(self,step,start):        #Josephring实现原列表按照约瑟夫环顺序的重新排序，并存储在list_joseph中
        assert step > 0,'Step size out of range!'
        assert 0 < start < 12,'Start position out of range!'
        list_sum = self.josephlist[start-1:len(self.josephlist)+1]+self.josephlist[0:start-1]
        sum = len(self.josephlist)
        counter = 1
        subscript = 0
        list_pop = []
        list_joseph = []
        while sum > 1:
            if counter < step:
                counter += 1
            else:
                counter = 1
                sum -= 1
                list_pop.append(list_sum[subscript])
                list_joseph.append(list_sum[subscript])
            if subscript < len(list_sum):
                if subscript > len(list_sum)-step-1:
                    list_sum = list_sum[subscript+1:len(list_sum)] + list_sum[0:subscript+1]
                    for i in range(len(list_pop)):
                        list_sum.remove(list_pop[i])
                    subscript = -1
                    list_pop = []
                subscript += 1
        list_joseph.append(list_sum[0])
        return list_joseph

step = int(input('Step size:'))
start = int(input('Start position:'))
j = Joseph(joslist)    
for i in j.Josephring(step,start):
    print('Name:',i.name,'Student number:',i.stu_number,'Gender:',i.gender)

