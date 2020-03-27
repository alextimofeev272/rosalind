#coding: utf_8

#Дано 15 протеинов
#Найти N-гликозилированный мотив

import urllib2#библиотечка для обработки веб-страниц, веб-форм

file = open('D:\python\input.txt')#открывает файл входных данных
names = file.readlines()#делает список название белков

for a in range(len(names)):#для каждого протеина
    name = names[a].replace('\n','')
    url='http://www.uniprot.org/uniprot/'+name+'.fasta'
    resp=urllib2.urlopen(url)#закружает текст с базы
    page=resp.readlines()
    protein = ''
    for j in range(1,len(page)):
        protein = protein + page[j]#Аминокислотная последовательность белка
    protein = protein.replace('\n','')
    otvet = ''
    for i in range(3,len(protein)):
            if protein[i-3]=='N' and protein[i-2]<>'P':
                    if protein[i-1]=='T' or protein[i-1]=='S':
                            if protein[i]<>'P':
                                    otvet = otvet + str(i-2) + ' '
                                    

    if otvet<>'':#если есть мотив
            print name  #Название белка
            print otvet #позиция начала мотивов

print 'end'
file.close()





         

