#coding: utf_8
#Последовательность чисел Фибоначчи
#k - число мясячев жизни кролика
#N - число месяцев воспроизведения кролликов
N = 95
k = 16
a = [0,1]
b = [0,1]
for x in range(N):
    x = 1 + x
    if x<k:
        g = b[x] + b[x-1]
    if x==k:
        g = b[x] + b[x-1]-1
    if x>k:
        g = b[x] + b[x-1]-b[x-k]
    b = b + [g]

print b
print b[N]


