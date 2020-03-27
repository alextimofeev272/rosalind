#coding: utf_8

#Даны цепочки ДНКа
#Даны мотивы
#Найти пооложение мотива в ДНка

file = open('D:\python\input.txt')
s = file.read().split('\n')

for j in range(0,len(s),2):
    otvet = ''
    a = s[j]
    b = s[j+1]
    for i in range(len(a)):
        f = a[i:i+len(b)]
        if f == b:
            otvet = otvet + str(i+1) + ' '
    print otvet

file.close()

         
