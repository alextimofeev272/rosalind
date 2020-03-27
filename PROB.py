#coding: utf_8
import math

s1 = 'GGATGAGTGGTTTTGCAATTTCATCTATGGAGCATTCGCCATCATATTGCTCAGGGGTGTAAAAGGGAGCGAAGCTAGGTC';
a = [0.125,0.180,0.218,0.284,0.329,0.418,0.492,0.533,0.599,0.676,0.689,0.798,0.862,0.908];
otvet='';

for A in a:
    d=1;prob1 = A/2;prob2 = (1 - A)/2;
    for i in s1:
        if i=='A' or i=='T':d = d*prob2;
        if i=='C' or i=='G':d = d*prob1;
    otvet = otvet + "%.3f" % math.log(d,10) + ' ';

print otvet    
        

