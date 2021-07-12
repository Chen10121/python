#Joseph_3
import zipfile
import csv
import xlrd     

#创建父类
class Reader():
    def __init__(self,path):
        self.filepath = path

    def Josephring(self,step,start,josephlist):        #Josephring实现原列表按照约瑟夫环顺序的重新排序，并存储在list_joseph中
        assert step > 0,'Step size out of range!'
        assert 0 < start < 12,'Start position out of range!'
        list_rotate = josephlist[start-1:len(josephlist)+1]+josephlist[0:start-1]
        list_sum = [0]*len(list_rotate)
        sum = len(list_rotate)
        counter = 1
        subscript = 0
        list_joseph = []
        while sum > 1:
            if subscript == len(list_sum) - 1:
                subscript = -1
            subscript += 1
            if list_sum[subscript] != 1:
                if counter == step:
                    list_sum[subscript] = 1
                    list_joseph.append(josephlist[subscript])
                    counter = 1
                    sum -=1
                else:
                    counter +=1
        list_joseph.append(josephlist[subscript-1])
        return list_joseph

    def readfile(self):
        with open(self.filepath,'r') as f:
            read = []
            for line in f:
                read = line
        return read

#创建三个子类，分别实现csv、zip、xls文件的读取
class Reader_csv(Reader):
    def read_csv(self):
        with open(self.filepath,'r') as f:
            read = []
            for line in csv.reader(f):
                read.append(line)
        return read

class Reader_zip(Reader):
    def read_zip(self):
        z = zipfile.ZipFile(self.filepath,'r')
        read = []
        for filename in z.namelist():
            read.append(filename)
        print(read)
        return read

class Reader_xls(Reader):
    def read_xls(self):
        x = xlrd.open_workbook(self.filepath,'r')
        table = x.sheets()[0]
        read = []
        for i in range(table.nrows):
            read.append(table.row_values(i))
        return read

#filepath = r'C:\Users\MAC\Documents\GitHub\python\excel.xlsx'
#filepath = r'C:\Users\MAC\Documents\GitHub\python\CSV.csv'
filepath = r'C:\Users\MAC\Documents\GitHub\python\ZIP.zip'

#filelist = Reader_xls(filepath).read_xls()
#filelist = Reader_csv(filepath).read_csv()
filelist = Reader_zip(filepath).read_zip()

step = int(input('Step size:'))
start = int(input('Start position:'))

#j = Reader_xls(filepath)
#j = Reader_csv(filepath)
j = Reader_zip(filepath)

for i in j.Josephring(step,start,filelist):
    print(i)
