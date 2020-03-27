#coding: utf_8
#Даны цепочки днк, найти где максимум CG

# open - открывает файл
# read - считывает файл
# replace - заменяет символ, тут убирает enter
# split('>')  - разбивает по символу >, символ не содержится в результате
# join(A) - объеденяет строку А

file = open('D:\python\input.txt')
text = file.read().replace('\n','').split('>')

percent1 = 0 #процент
name = [] #название абзаца	

for x in text[1:]: #чтение файла с 1 символа

    DNA = x[13:] #цепочка днка

    #вычесляем процент CG.
    #float - переводит целый тип в вещественный
    #.count - возращает количество символов в строке
    #len - длинна строки, кол-во символов
    
    percent2 = float(100)*(DNA.count('G')+DNA.count('C'))/len(DNA)
    
    if percent2 > percent1:
        percent1 = percent2
        name = x[:13] #имени присваивает первые 13 символов
        
print name
print percent1

file.close() #закрывает файл
