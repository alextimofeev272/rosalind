#coding: utf_8
#вычисляет число сочитаний по модулю
#для больших чисел
import numpy


n = 1902
m = 734
s = 0

def C(n,m,k):
        s = 0
        B = numpy.array([[0]*(n+1)]*(n+1))
        for i in range(n+1):
                B[i][0]=1;
                B[i][i]=1;
                for  j in range(1,i):
                        B[i][j]=B[i-1][j-1]%1000000+B[i-1][j]%1000000
        for i in range(m,k+1):
                s = s + B[n][i]
        return s % 1000000

print C(n,m,n)
