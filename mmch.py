#coding: utf_8
#найти размещения - упорядоченный набор к - элеменов из n
#что равно C(n,k)*k! - число сочетаний умноженное на число перестановок
#число размещений учитывает порядок
#пример: AUGCUUC

from math import factorial 
rna = 'AUGCUUC'

a, u, g, c = map(rna.count, ["A", "U", "G", "C"])

a = factorial(max(a, u)) / factorial(max(a, u) - min(a, u))
b = factorial(max(g, c)) / factorial(max(g, c) - min(g, c))
print a * b
        
