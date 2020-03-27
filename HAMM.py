#coding: utf_8
#Расстояние Хэмминга
#Две цепочки ДНК, найти мутации(т.е. отличия)

file = open('D:\python\input.txt', 'r')
first = file.readline(1000)
second = file.readline(1000)
a = 0
i = 0
for x in first:
    if second[i]<>x:
        a=a+1
    i=i+1
print a

file.close()
