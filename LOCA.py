#coding: utf_8
#PAM 250
#найти локальное выравнивание
#Смысл - когда начинает уменьше цена, ставим ноль
#Аналогичное EDTA,glob и т.д.
import numpy
from Bio.SubsMat.MatrixInfo import pam250

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
s = string(text)

s1 = s[0]
s2 = s[1]

gap = -5

dist = [[0 for j in xrange(len(s2)+1)] for i in xrange(len(s1)+1)]

def alignmentScore(s1,s2,dist):
    for i in xrange(1,len(s1)+1):
        for j in xrange(1,len(s2)+1):
            sc = pam250.get((s1[i-1], s2[j-1]))
            if sc == None:
                sc = pam250.get((s2[j-1], s1[i-1])) 
            match = dist[i-1][j-1] + sc
            delete = dist[i-1][j] + gap
            insert = dist[i][j-1] + gap
            dist[i][j] = max(0,match, delete, insert)
    maxv,maxi,maxj = float('-inf'),float('-inf'),float('-inf')
    for i in xrange(1,len(dist)):
        curr_maxv = max(dist[i])
        curr_maxj = dist[i].index(curr_maxv)
        if curr_maxv > maxv:
            maxv,maxi,maxj = curr_maxv,i,curr_maxj
    return maxv,maxi,maxj

def augment(dist,s1,s2,maxi,maxj):
    t1,t2,i,j = '','',maxi,maxj
    while dist[i][j] != 0:
        l,d,t = dist[i][j-1], dist[i-1][j-1], dist[i-1][j]
        if s1[i-1] == s2[j-1] or (d == max(l,d,t) and d>l and d>t):
            t1,t2,i,j = s1[i-1]+t1,s2[j-1]+t2,i-1,j-1
        elif t == max(l,d,t):
            t1,t2,i,j = s1[i-1]+t1,t2,i-1,j
        elif l == max(l,d,t):
            t1,t2,i,j = t1,s2[j-1]+t2,i,j-1
    return t1, t2

maxv,maxi,maxj = alignmentScore(s1,s2,dist)
t1,t2 = augment(dist,s1,s2,maxi,maxj)
output = '{0}\n{1}\n{2}'.format(maxv,t1,t2)
print output








