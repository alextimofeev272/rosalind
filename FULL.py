#coding: utf_8
#Данны массы.
#первое число - масса пептида
#остальные числа - b-ионы(начало белка) и y-ионы(конец белка)
#масса белка = масса b-ионна и y-ионна
#найти протеин

massa2 = {71.0371: 'A',103.0092:'C',115.0269: 'D',129.0426: 'E',147.0684: 'F',
         57.0215: 'G',137.0589: 'H',113.0841: 'I',128.095: 'K',113.0840: 'L',
         131.0405: 'M',114.0429: 'N',97.0528: 'P',128.0586: 'Q',156.1011: 'R',
         87.032: 'S',101.0477: 'T',99.0684: 'V',186.0793: 'W',163.0633: 'Y'}

file1 = open('D:\\python\input.txt')
S=file1.read().strip().split('\n');
a = [];
for s in S:
    a.append(float(s))

m_prot = a[0]#масса пептида
m_ions = sorted(a[1:])#масса ионов b и y(не понятно кто b, кто y)

#ищем пары b и y ионов
pairs_i = [];o='';b=0;
for i in range(len(m_ions)/2):
    for j in range(len(m_ions)):
        if round(m_ions[i]+m_ions[j],3)==round(m_prot,3):
            pairs_i.append((m_ions[i],m_ions[j]))
print pairs_i
protein = '';i=0
while i < len(pairs_i)-1:
    mio = 0
    for massa in massa2:
        #print pairs_i[i+1][0],pairs_i[i][0]
        #print i,round(pairs_i[i+1][0] - pairs_i[i][0],4),massa
        if round(pairs_i[i+1][0] - pairs_i[i][0],4)== massa:
        # значит [0] оказались b ионами
            mio = massa;protein += massa2[mio];i += 1;
            break
    if mio == 0:
        #если не нашли, значит перепутали b и y ионы
        pairs_i[i+1] = (pairs_i[i+1][1], pairs_i[i+1][0])
        #заново сортируем и заново ищем
        pairs_i.sort()
        i = 0
        protein = ''
            
print protein








