#coding: utf_8

def prot_tr(RNA):
    RNA_table = {
       "UUU": "F", "CUU": "L", "AUU": "I", "GUU": "V",
       "UUC": "F", "CUC": "L", "AUC": "I", "GUC": "V",
       "UUA": "L", "CUA": "L", "AUA": "I", "GUA": "V",
       "UUG": "L", "CUG": "L", "AUG": "M", "GUG": "V",
       "UCU": "S", "CCU": "P", "ACU": "T", "GCU": "A",
       "UCC": "S", "CCC": "P", "ACC": "T", "GCC": "A",
       "UCA": "S", "CCA": "P", "ACA": "T", "GCA": "A",
       "UCG": "S", "CCG": "P", "ACG": "T", "GCG": "A",
       "UAU": "Y", "CAU": "H", "AAU": "N", "GAU": "D",
       "UAC": "Y", "CAC": "H", "AAC": "N", "GAC": "D",
       "UAA":  "", "CAA": "Q", "AAA": "K", "GAA": "E",
       "UAG":  "", "CAG": "Q", "AAG": "K", "GAG": "E",
       "UGU": "C", "CGU": "R", "AGU": "S", "GGU": "G",
       "UGC": "C", "CGC": "R", "AGC": "S", "GGC": "G",
       "UGA":  "", "CGA": "R", "AGA": "R", "GGA": "G",
       "UGG": "W", "CGG": "R", "AGG": "R", "GGG": "G"
    }
    codons = []
    for i in xrange(0, len(RNA), 3):
        RNA2 = RNA[i: i + 3]
        codons.append(RNA_table.get(RNA2, ''))
    return ''.join(codons)

def del_st(s,s2):
    for i in range(len(s)):
        if s[i:i+len(s2)]==s2:
            s3 = s[:i]+s[i+len(s2):]
    return s3

def string(text):
    results = []
    strings = text.strip().split('>')
    for s in strings:
        if len(s):
            parts = s.split()
            k = parts[0]
            v = ''.join(parts[1:])
            results.append(v)
    return results

file = open('D:\\python\input.txt')
text = file.read()
list1 = string(text);list2=[];

for i in list1:
    j = i.replace('T','U')
    list2.append(j)

a = list2[0]    
for i in range(1,len(list2)):
    a = del_st(a,list2[i])
    
print prot_tr(a)
file.close()







