#coding: utf_8

#Дана цепочка РНК, мРНК(матричная РНК)
#Построить протеин

a = ('UUU','CUU','AUU','GUU','UUC','CUC','AUC','GUC','UUA','CUA','AUA','GUA')
a = a + ('UUG','CUG','AUG','GUG','UCU','CCU','ACU','GCU','UCC','CCC','ACC','GCC')
a = a + ('UCA','CCA','ACA','GCA','UCG','CCG','ACG','GCG','UAU','CAU','AAU','GAU')
a = a + ('UAC','CAC','AAC','GAC','UAA','CAA','AAA','GAA','UAG','CAG','AAG','GAG')
a = a + ('UGU','CGU','AGU','GGU','UGC','CGC','AGC','GGC','UGA','CGA','AGA','GGA')
a = a + ('UGG','CGG','AGG','GGG')

b = ('F','L','I','V','F','L','I','V','L','L','I','V')
b = b + ('L','L','M','V','S','P','T','A','S','P','T','A')
b = b + ('S','P','T','A','S','P','T','A','Y','H','N','D')
b = b + ('Y','H','N','D','0','Q','K','E','0','Q','K','E')
b = b + ('C','R','S','G','C','R','S','G','0','R','R','G')
b = b + ('W','R','R','G')

file = open('D:\python\input.txt')
file2 = open('D:\python\output.txt','w')
text = file.read()

n = len(text)
d = ''

for i in range(0,n,3):
    f = text[i:i+3]
    for j in range(64):
        if f == a[j]:
            d = d + b[j]
            
d = d.replace('0','\n\n')
print d
file2.write(d)
print n

file.close()
file2.close()
