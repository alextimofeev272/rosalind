#coding: utf_8

#Даны 3 числа: k,m,n
# k - гомозиготные доминантные
# m - гетерозигоные
# n - гомозиготные рецесивные
# k + m + n - общая популяций организмов
# Найти вероятность что спаривание двух любых организмов приводит
# к образованию организма с доминантной аллелем.

def prob(k,m):
    return float(k)/float(m)

def probline(k,m,n):
    s = k + m + n
    return prob(k,s)*prob(k-1,s-1),prob(k,s)*prob(m,s-1),prob(k,s)*prob(n,s-1)
   
k = 23
m = 15
n = 17

Pk = probline(k,m,n);Pm = probline(m,k,n);Pn = probline(n,k,m);

P = Pk[0]+Pk[1]+Pk[2]+Pm[0]*0.75+Pm[1]+Pm[2]*0.5+Pn[1]+Pn[2]*0.5

print P
