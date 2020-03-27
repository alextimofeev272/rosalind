#coding: utf_8

import time

start = time.time()

file = open('D:\\python\input.txt')
text = file.readline()
f = text.count('F')
l = text.count('L')
s = text.count('S')
y = text.count('Y')
c = text.count('C')
w = text.count('W')
p = text.count('P')
h = text.count('H')
q = text.count('Q')
r = text.count('R')
i = text.count('I')
m = text.count('M')
t = text.count('T')
n = text.count('N')
k = text.count('K')
v = text.count('V')
a = text.count('A')
d = text.count('D')
e = text.count('E')
g = text.count('G')
qwe = f+l+s+y+c+w+p+h+q+r+i+m+t+n+k+v+a+d+e+g+1-len(text)
print qwe
otv = 3*(2**f)*(6**l)*(6**s)*(2**y)*(2**c)*(1**w)*(4**p)*(2**h)*(2**q)*(6**r)*(3**i)*(1**m)*(4**t)*(2**n)*(2**k)*(4**v)*(4**a)*(2**d)*(2**e)*(4**g)    
print otv%1000000
finish = time.time()

print (finish - start)

       
        
        
