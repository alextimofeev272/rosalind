#coding: utf_8
import itertools
        
s = ['A','C','G','T']
n = 2

for i in itertools.product(s,repeat=n):
    print ''.join(i)



        

        
