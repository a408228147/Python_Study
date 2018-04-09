import sys
X=1
def  mark(N):
    n = N
    def action(x):
        nonlocal n
        #nonlocal X 运行失败必须要在def里面

        print(n)
        n=1
        return  n*x
    return action

def func():
    x = 4
    action=(lambda n: x*n)
    return action

def func2():
    x=2
    action=(lambda n, x=x:x*n)
    return action

def f():
    X='NI'
    def nested():
        nonlocal X
        X ='Spam'
    nested()
    print(X)

def any(*args): #任意参数
    print(args)
def dictany(**args):#字典参数
    print(args)

def kwonly(a,*b,c):
    print(a,b,c)

def kwonly2(a,*,b='spam',c='ham'):#*后必须带关键字传递 keyword-only不能出现在**参数后面
    print(a,b,c)

def intersect(*args):
    res=[]
    for x in args[0]:
        for other in args[1:]:
            if x not in other:break
        else:
            res.append(x)
    return res

#模拟print函数
def print3(*args,sep= ' ',end='\n',file=sys.stdout):
    output =''
    first = True
    for arg in args:
        output+=('' if first else sep)+str(arg)
        first=False
    file.write(output+end)

def mysum(L):
    first,*rest=L
    return first if not rest else first+mysum(rest)
def sumtree(L):
    tot = 0
    for x in L:
        if not isinstance(x,list):
            tot +=x
        else:
            tot +=sumtree(x)
    return tot
def mymap(func,*seqs):
   return [func(*args) for args in zip(*seqs)]
def myzip(*seqs):
    minlen = min(len(s) for s in seqs)
    return [tuple(s[i] for s in seqs) for i in range(minlen)]
def mymapPad(*seqs,pad =None):
    maxlen = max(len(s) for s in seqs)
    index =range(maxlen)
    return [tuple((s[i] if len(s) >i else pad ) for s in seqs) for  i in index]

def test(y):
    map()

if __name__=='__main__':
    print(mymap(abs,[-2,-1,0,1,2]))
    print(mymap(pow,[1,2,3],[2,3,4]))
    #L=[1,[2,[3,4],5],6,[7,8]]
    #print(sumtree(L))
    #print3(mysum('t321'))
     #print3('a','b','c')
    # print('a','b','c')
     #kwonly2(a=2)
    #kwonly(1,2,3,c=3)#带*参数的后面参数必须要标识
    # any(1,2,3,4,12,3,4)  元祖
    #dictany(a=1,b=3)   字典
    #f()
  #  t=mark(2)
   # print(t(2))
'''
   g=mark(3)
   print(g(2))'''
    #t=func2()
    #print(t(2))