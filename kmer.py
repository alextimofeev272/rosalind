#coding: utf_8
import itertools

kmers = [];a=[]

file = open('D:\\python\input.txt')
s = ''.join(file.read().split('\n'))

n = 4

for i in itertools.product(['A','C','G','T'],repeat=n):
    kmers.append(''.join(i));a.append(0);

otv = ''

for j in range(len(s)-n+1):
    for i in range(len(kmers)):
        if s[j:j+n] == kmers[i]:
            a[i] = a[i] + 1
            
print ' '.join(str(a[i]) for i in range(len(a)))

