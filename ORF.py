#coding: utf_8
#Найти варианты протеинов из строки ДНКА(и обратной..?)
dna_dict = {'TTT': 'F',     'CTT': 'L',     'ATT': 'I',     'GTT': 'V',
            'TTC': 'F',     'CTC': 'L',     'ATC': 'I',     'GTC': 'V',
            'TTA': 'L',     'CTA': 'L',     'ATA': 'I',     'GTA': 'V',
            'TTG': 'L',     'CTG': 'L',     'ATG': 'M',     'GTG': 'V',
            'TCT': 'S',     'CCT': 'P',     'ACT': 'T',     'GCT': 'A',
            'TCC': 'S',     'CCC': 'P',     'ACC': 'T',     'GCC': 'A',
            'TCA': 'S',     'CCA': 'P',     'ACA': 'T',     'GCA': 'A',
            'TCG': 'S',     'CCG': 'P',     'ACG': 'T',     'GCG': 'A',
            'TAT': 'Y',     'CAT': 'H',     'AAT': 'N',     'GAT': 'D',
            'TAC': 'Y',     'CAC': 'H',     'AAC': 'N',     'GAC': 'D',
            'TAA': 'Stop',  'CAA': 'Q',     'AAA': 'K',     'GAA': 'E',
            'TAG': 'Stop',  'CAG': 'Q',     'AAG': 'K',     'GAG': 'E',
            'TGT': 'C',     'CGT': 'R',     'AGT': 'S',     'GGT': 'G',
            'TGC': 'C',     'CGC': 'R',     'AGC': 'S',     'GGC': 'G',
            'TGA': 'Stop',  'CGA': 'R',     'AGA': 'R',     'GGA': 'G',
            'TGG': 'W',     'CGG': 'R',     'AGG': 'R',     'GGG': 'G'}

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

def prot(s):
    a = []; res = [];
    for i in range(0,len(s)-2):
        if dna_dict[s[i:i+3]] == 'M': a.append(i);
    for i in range(len(a)):
        o = ''; e = 0;
        for j in range(a[i],len(s)-2,3):
            b = dna_dict[s[j:j+3]]
            if b == 'Stop': e = 1; break;
            else: o = o + b
        if e == 1: res.append(o)
    return res
    

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
slist = string(text)
s = slist[0]
#set - cоздает множество без повторений
#'a'.joint - объеденяет элементы в строку между строк ставит a

print '\n'.join(set(prot(s)+prot(transver(s))))

file.close()



        
