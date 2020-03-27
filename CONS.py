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
            #k = parts[0]#название
            v = ''.join(parts[1:])#объеденяет строки(последоваельности амин)
            results.append(v)#добавляет название и строку в один элемент
    return results

file = open('D:\\rosalind_cons.txt')
file2 = open('D:\python\output.txt','w')

text = file.read()
a = 'A:'; c = 'C:'; g = 'G:'; t = 'T:'; otvet='';
A = [];C = [];G = [];T = []; DNA2 = [];
DNA = string(text)
for i in range(len(DNA[0])):
               A.append(0);C.append(0);G.append(0);T.append(0);DNA2.append('A');

for j in DNA:
    k = -1;
    for x in j:
        k = k + 1;
        if x == 'A':
            A[k] = A[k] + 1
        if x == 'C':
            C[k] = C[k] + 1
        if x == 'G':
            G[k] = G[k] + 1
        if x == 'T':
            T[k] = T[k] + 1

for i in range(len(DNA[0])):
    a = a + ' ' + str(A[i]);c = c + ' ' + str(C[i]);
    g = g + ' ' + str(G[i]);t = t + ' ' + str(T[i]);
    if C[i]>A[i]: 
        DNA2[i] = 'C'
    if T[i]>A[i] and T[i]>C[i]:
        DNA2[i] = 'T'
    if G[i]>A[i] and G[i]>C[i] and G[i]>T[i]:
        DNA2[i] = 'G'
    otvet =  otvet + DNA2[i]

file2.write(otvet+'\n')
file2.write(a+'\n');file2.write(c+'\n');file2.write(g+'\n');file2.write(t+'\n');

file.close()
file2.close()

    
        


        
               




                    
            

    
        



