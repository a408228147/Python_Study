import re
import math

import copy

import sys

s = "abcdef"
#字符串具有不可变性
#s[0]='b'
#TypeError: 'str' object does not support item assignment
print(s[0])

s.replace("a","ABC")#此方法会返回一个被改变后的值 s的值不会被改变
print(s)#abcdef
s.upper()#ABCDEF 大写
s.isalpha()#true 测试字母，数字....
list1= "a,b,c,d,e,f"
print(list1.split(",")) #['a', 'b', 'c', 'd', 'e', 'f']
print(list1[0])#a
print(list1[1])#,
#格式化高级代替
'%s,b,c,%s' % ('a','b') #'a,b,c,d'

'{0},b,c,{1}'.format('a','b') #'a,b,c,d'

print(dir(s))
#['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__',
#  '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__',
#  '__gt__', '__hash__', '__init__', '__iter__', '__le__', '__len__', '__lt__', '__mod__',
#  '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__',
#  '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize',
# 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format',
#  'format_map', 'index', 'isalnum', 'isalpha', 'isdecimal', 'isdigit', 'isidentifier',
#  'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust',
#  'lower', 'lstrip', 'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust',
#  'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase',
# 'title', 'translate', 'upper', 'zfill']
print(help(s.isalpha))
#isalpha(...) method of builtins.str instance
    #S.isalpha() -> bool

#模式匹配
ma = re.match('w[ \t]*(.*)a' ,"w   python a")
print(ma.group(1))#python

L=[1,2,3,4,5]
print(L[1:])#[2, 3, 4, 5]
print(L[:3])#[1,2,3]
print(L[:-1])#[1, 2, 3, 4]
L.pop(1)
L.reverse()
L.sort()


M=[[1,2,3],[4,5,6],[7,8,9]]
col2 =[row[2] for row in M]
print(col2)
col = [sum(row) for row in M]
print(col)

K = {'a': 1, 'b': 2, 'c': 3}
L={'c':3,'b':2,'a':1}
print(K)#无序
ks =K.keys()#dict_keys(['c', 'b', 'a'])
K.keys()
print("-----------------------------------")
print(L)#无序
value=K.get('d',4)#获取一个不存在的键 不会报错
print(K)
print(value)
T=(1,2,24,4)
print(T.index(24))
'''
'r':默认值，表示从文件读取数据。
'w':表示要向文件写入数据，并截断以前的内容
'a':表示要向文件写入数据，添加到当前内容尾部
'r+':表示对文件进行可读写操作（删除以前的所有数据）
'r+a'：表示对文件可进行读写操作（添加到当前文件尾部）
'b':表示要读写二进制数据
'''
#int() #向下取整   5.1--》5  -5.1---》-5
#math.floot() #取小整数 5.1 --->5   -5.1-->6
#math.trunc()#直接去掉小数5.1-->5 -5.1--->-5
#round() #四舍五入  5.1---》5   -5.6---》6

x=[1,2,3,4]
y= copy.copy(x)
y= copy.deepcopy(x)
y[0]=-1;
print(x,y)

F = "abcdefghijk"
print(F[1:10])#bcdefghij
print(F[1:10:2])#b d f h j
print(F[::2])#a c e g i k
print(F[::-1])#kjihgfedcba
print(F[:-1])#abcdefghij
print(F[::-2])#k i g e c a

ord("A") #ASCII码 65
chr(65) #"A"

C=["2","1","3"]
print(C)#['1', '2', '3']
C.sort()#['1', '2', '3']升序
print(C)
#C.sort(key=str.lower)#['1', '2', '3']
print(C)
#C.sort(key=str.lower,reverse=True)#['3', '2', '1']
print(C)
C.reverse()#['3', '2', '1'] 反转排序
print(C)

D=sorted(C)
print(C)
print(D)


DDD = list(zip([1,2,3,4],[1,2,3,4]))
print(DDD)

print({ c.lower(): c*2 for c in ["A","B","C"]})

test = [i for i in range(5)]
print(test)


print(dict([("a",0),("b",0)]))#{'a': 0, 'b': 0}
dict.fromkeys(["a","b"],0)
{k:0 for k in 'ab'}


a=[]
a.append(1);
print(a)#[1]
a.extend([2,3]);
print(a)#[1, 2, 3]
a.insert(1,3)
print(a)#[1, 3, 2, 3]
del a[1]
print(a)#[1, 2, 3]

b={"a":1,"b":2,"c":3,"d":4}
del b["a"]
print(b)#{'b': 2, 'c': 3, 'd': 4}
b.update({"e":5,"f":6})
print(b)#{'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6}
b["a"]=1
print(b)#{'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'a': 1}

print(b.get("a",1))#判断有没有键“a”
print("------------")
print(b)
b["a"]=7
print(b)

T=(4,3,2,1)
print(T+T)
print([x*2 for x in T])
print(T.index(1))
print(T.count(1))

print(sorted(T))
print(T)

output = open(r'C:\spam','w')#输入  'a'在尾部打开文件
input = open('data','r')#读取
#a = input.read()
#print(a)
print("-------")
#a= input.read(30)#读取多少个字节
#print(a)
#astring= input.readline()
#print(astring)
aList = input.readlines()#组合成一个列表
print(aList)
output.writelines(aList)
output.close()
#output.flush()#把缓冲区输出到硬盘中，不关闭
#anyFile.seek(N) 偏移到文件N位置以便进行下一步操作
for line in open('data'):#文件迭代器 一行一行读取
    print(line)

q = "{'a':1,'b':2}"
c = "[1,2,3,4]"
q=eval(q)#把字符串转化为对象
c=eval(c)
print(q)
print(c)

'''
1.对象根据分类来共享操作，例如：字符串、列表、和元祖都共享
合并、长度和索引等序列操作
2.只有可变对象（列表，字典和集合）可在原处修改，不能原处修改
字符串，数字，元祖
3.文件到处唯一的方法，因此可变性并不适用于它们---当处理文件的时候
它们的状态可能会修改，但是这与python的核心类型可变性限制不完全相同
4.数字包含了所有数字类型  整数，小数，浮点数，负数，分数
5. byteearray字符串类型可变
6.集合类似于一个无值的字典的键，但是它们不能映射为值，并且没有顺序，frozenset是
集合一个不可变的版本

对象类型    分类      是否可变
数字        数值      否
字符串      序列      否
列表        序列      是
字典        对应      是
元祖        序列      否
文件        扩展      N/A
Sets        集合      是
frozenset   集合      否
bytearray   序列      是
'''
li= [1,2,3,4]
lis= li[:]
lis[0]=2
print(li)
print(lis)

copylist=[1,1,[1,1]]
topcopy=  copy.copy(copylist)#浅层复制  嵌套的数据 会被改变
decopy= copy.deepcopy(copylist)#深层复制 是否嵌套的数据都不会被改变
copylist[2]=2
print(topcopy)
print(decopy)

# == 比较值   is 比较对象（地址）是否一致



D1 = {"a":1,"b":2}

D2 ={"b":3,"a":1,}
D1 = D1.items()
#D1=list(D1.items())
D2=sorted(D2.items())
#print(D1>D2)
print(D1)
print(D2)
#print(D2>D1)


D3= [1,2,3,4]
D3.append(1)
print(D3)



print(True is 1)#false True ==1 true

"""
type() 不会认为子类是一种父类类型，不考虑继承关系。
isinstance() 会认为子类是一种父类类型，考虑继承关系。
"""
print(type([1])==list)
print(type([1])==type([]))
print(isinstance([1],list))


D4= (1,2,3,4)
#D4[0]=2#error
D4 =D4[:3]+(4,)#(1,2,3,4)

x= '1'
y='2'
x,y=y,x #等价于 x,y =2,1

L=[1,2,3,4]
while L:
    front,L =L[0],L[1:]#返回L
    print(front,L)



L=[1,2,3]
M=L
L+=[9,10]#Python  会自动调用 extend 而不是用+  会修改M的值

L=L+[9,10] #不会修改M的值

#print([object,..][,sep=''][,end=\n''][,file=sys.stdout])
                  #sep:分隔符  end：结尾  file 文件操作
"""
print(x,y)
等价于
import sys
sys.stdout.write(str(x)+' '+str(y)+'\n')
"""
temp= sys.stdout
sys.stdout = open('data','a')
print("123")#print 已经被重设 任何输出都会写进data文件里面
sys.stdout.close()#关闭写入
sys.stdout=temp#重新切换回来

print('back here')

log = open('data','a')
print(1,2,3,file=log)
print(4,5,6,file=log)
log.close()
print(7,8,9)

#print("d"*8,file=sys.stderr)

D5 = {'a':1,'b':2,'c':3}
for key in D5.keys():
    print(key,'=>',D5[key])

#file = open('data')
#print(file.read())

for line in open('data').readlines():
    print(line,end='')

for line in open('data'):
    print(line,end='')

D6= (1,2,3,4)
d2 = list(zip(D6,D6,D6,D6))
print("000000000000000000")
print(d2)
D6=list(zip(D6,D6)) #  两个集合 通过 zip构造字典 取短
print(D6)#[(1, 1), (2, 2), (3, 3), (4, 4)]
D6=dict(D6)#列表转字典 {1: 1, 2: 2, 3: 3, 4: 4}
print(D6)
#for (x,y) in zip(D6,D6):
 #   print(x,y,'---',x+y)

D7="abcdefg"
for (id,value) in enumerate(D7):
    print(id,value)

D8= [line.rstrip() for line in open('data')]
#['1231231', '312312', '312', '3121', '3', '12', '3ewq', '',
print(D8)

[x+y for x in 'abc' for y in '123']

#sorted(open('data'))#迭代
#list(zip(open('data'),open('data')))
#list(enumerate(open('data')))
#list(filter(bool,open('data')))
"""
import functools, operator
functools,reduce(operator.add,open('data'))
"""
#tuple(open('data'))#元祖
#list(open('data'))
'&&'.join(open('data'))#



0 if False else 1+2  #如果正确则返回0 失败返回3

[x**2 for x in range(10) if x%2==0]

