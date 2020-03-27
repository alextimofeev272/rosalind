#coding: utf_8
#хреново написано в розалинде
#задача вывести список смежностей + символ,т.е материнский(м.и.) и дочерний(д.и.) индексы
#решение из решений на розалинде от Rayan(мое было хуже), наиболее кратко..мной подкорректировано
from itertools import permutations
#permutations(из чего,длинной) - делает перестановки
seqs = """
ATAGA
ATC
GAT
""".split()
file2 = open('D:\\python\output.txt','w')
#создается список не повторяющихся элементов строк
#от 1го символа до max в строке
#b = {'A'};e=['']
#for seq in seqs:
#    a = []
#    for i in xrange(1,len(seq)+1):
#       a.append(seq[:i])
#    d = set(a)
#    b = b|d
#e = e + list(b)
#print e
#все это ниже одной строчкой
nodes = [''] + list( set( [ seq[:i] for seq in seqs for i in xrange(1,len(seq)+1)] ) )

for node1, node2 in permutations(nodes,2):
    print node2[:-1],node2
    if node2[:-1] == node1:
        a = "%d %d %c"%(nodes.index(node1)+1, nodes.index(node2)+1, node2[-1])
        print a
        file2.write(a+'\n')
