#coding: utf_8
#Дан набор строк ДНК в формате FASTA
#Выдать список смежности

#создает список, элемент - названи и строка днк
def string(text):
    results = []
    strings = text.strip().split('>')#pазделяет строку по >,убирает пробелы
    
    for s in strings:
        if len(s):#если не нулевая длинна строки
            parts = s.split()
            k = parts[0]#название
            v = ''.join(parts[1:])#объеденяет строки(последоваельности амин)
            results.append((k, v))#добавляет название и строку в один элемент
    return results


file = open('D:\python\input.txt')
text = file.read()

DNA = string(text)

for i, j in DNA:
    for e, k in DNA:#если не одна и таже строки
        if i<>e:
            #endswith(a) - проверяет заканчивается ли строка, подстрокой a
            #endswith(a,i,j) - проверяет заканчивается ли часть строки с i до j
            if k.endswith(j[:3]):
                print e, i


