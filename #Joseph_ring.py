#Joseph_ring
def Joseph_ring(n,q,m):
    list_sum = list(range(int(n)+1))[1:int(n)+1]
    sum = int(n)
    counter = 1
    subscript = 0
    list_pop = []
    while sum > int(n)-int(m):
        if counter < int(q):
            counter += 1
        else:
            counter = 1
            list_pop.append(list_sum[subscript])
            sum -= 1
        if subscript < len(list_sum):
            if subscript > len(list_sum)-int(q)-1:
                list_sum = list_sum[subscript+1:len(list_sum)] + list_sum[0:subscript+1]
                for i in range(len(list_pop)):
                    list_sum.remove(list_pop[i])
                #print(list_pop)
                subscript = -1
                list_pop = []
            subscript += 1
    print('剩余人为：',list_sum)

n = input('总人数为：')
q = input('相隔人数为：')
m = input('排除人数为：')
Joseph_ring(n,q,m)

#Joseph_ring_recursion
def Joseph_ring_recursion(n,q):
    if int(n) == 1:
        return 0
    else:
        return (Joseph_ring_recursion(int(n)-1,int(q))+int(q))%int(n)

n = input('总人数为：')
q = input('相隔人数为：')
print('约瑟夫环结果为：',Joseph_ring_recursion(n,q)+1)

#约瑟夫环数组
def Joseph(n,q,m):
    list_sum = [0]*(int(n))
    sum = int(n)
    counter = 1
    subscript = -1
    while sum > int(n)-int(m):
        if subscript == len(list_sum)-1:
            subscript = -1
        subscript += 1
        if list_sum[subscript] != 1:
            if counter == int(q):
                list_sum[subscript] = 1
                counter = 1
                sum -=1
            else:
                counter += 1
    return list_sum

n = input('总人数为：')
q = input('相隔人数为：')
m = input('排除人数为：')
print(Joseph(n,q,m))
