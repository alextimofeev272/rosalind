#coding: utf_8
def string(text):
    results = []
    strings = text.strip().split('>')#pазделяет строку по >,убирает пробелы
    for s in strings:
        if len(s):#если не нулевая длинна строки
            parts = s.split()
            k = parts[0]#название
            v = ''.join(parts[1:])#объеденяет строки(последоваельности амин)
            results.append(v)#добавляет название и строку в один элемент
    return results

def transver(first):
    second = ''
    for x in first:
        if x=='T': second = 'A' + second
        if x=='A': second = 'T' + second
        if x=='C': second = 'G' + second
        if x=='G': second = 'C' + second
    return second

file = open('D:\\python\input.txt')
text = file.read()
f = string(text)
s = [];d=[];a=0;w=0;
#f = ['TCATC','TTCAT','TCATC','TGAAA','GAGGA','TTTCA','ATCAA','TTGAT','TTTCC']

for i in f:
   s.append(transver(i))

for i in f:
    if f.count(i)+f.count(transver(i))==1:
        d.append(i)
print len(d)

for i in d:
    c = ''
    for j in range(len(i)):
        for k in ('A','C','G','T'):
            if k<>i[j]:
                c = i[:j]+k+i[j+1:]
                if f.count(c)+f.count(transver(c))>1:
                    print i+'->'+c


                









