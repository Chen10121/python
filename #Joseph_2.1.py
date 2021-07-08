#Joseph_2.1
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

#约瑟夫环应用
def Joseph_ring(step,remove,start,list_name):
    assert step > 0,'Step size out of range!'
    assert 0 < start < 12,'Start position out of range!'
    assert 0 < remove < 12,'Remove number out of range!'
    list_sum = list_name[start-1:len(list_name)+1]+list_name[0:start-1]
    sum = len(list_name)
    counter = 1
    subscript = 0
    list_pop = []
    while sum > len(list_name)-remove:
        if counter < step:
            counter += 1
        else:
            counter = 1
            list_pop.append(list_sum[subscript])
            sum -= 1
        if subscript < len(list_sum):
            if subscript > len(list_sum)-step-1:
                list_sum = list_sum[subscript+1:len(list_sum)] + list_sum[0:subscript+1]
                for i in range(len(list_pop)):
                    list_sum.remove(list_pop[i])
                subscript = -1
                list_pop = []
            subscript += 1
    list_pop = list_name
    for i in range(len(list_sum)):
        list_pop.remove(list_sum[i])
    print('The rest of people:\n')
    for i in range(len(list_sum)):
        print('Name:',globals()[list_sum[i]].name)
        print('Student number:',globals()[list_sum[i]].stu_number)
        print('Gender:',globals()[list_sum[i]].gender,'\n')
    print('Out of people:\n')
    for i in range(len(list_pop)):
        print('Name:',globals()[list_pop[i]].name)
        print('Student number:',globals()[list_pop[i]].stu_number)
        print('Gender:',globals()[list_pop[i]].gender,'\n')
    return list_sum

step = int(input('Step size:'))
remove = int(input('Semove number:'))
start = int(input('Start position:'))
Joseph_ring(step,remove,start,list_name)
