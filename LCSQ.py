import sys

s1 = 'CCTCCTCAGATATTTACCCAGGTCCTTTAGATGCTTAACCATGCGTCATTGTCTCGGGCCGGTCCAACCATGCATACATGTCCTCCCCCGTAGCTTTCGTATTGGTGCGATGCACGATGCATGCCGTTCAAGGAAGGCCCGCGCGGAACGCTTGTTATGCTACGCGTTCAGCTATCCTACGAATGGATGCCATCGCACATTACACGAACGGCGGAGATGTGGGAGTGGGAGTGTACACGCTGCCCCACATCAACTGGTGCCTGACTAGTGAAACTAGGACGTGATCCGTATAAACAAGAGGAGGACACTAATGCACGGCTTTTGATACAAACTGAATCATGGTAGTGCGTTCAAAGAGGCTGTTACATGGGCCGTGTAATGGTTGTTACACGGTAGGACTCAGCGCTCCGGGAATCCTGTGTAACTGGGTGGGACGGAGTAGCCTTACTTAATTGGGGATCTTCCAGGTAGTCTGGACATTTGGTCAATGCACTTCCATACGGTTGTCCCATCGAGGAGTTCTTTCTCCAGCGGTCAACGGCCAAGTATTCTCTCGCCATCAGAATCCAAAGAATGCACTAACTATCCACAGGATGCCACAAGCCTAACCGTACCTTACATCATCATGGTCCCGGAGGTACCAAGTTTGGATTCTGAACAGCGCACATGTACTTCCACGGCGCAGCAACCACCGCGCCCTGCTATAAAGCGGTTTGCATCAAAGATAACAAAACCGTGTCAGTTATATCATGTCACGTAGCTAATGCTCGCATAGGCTGGATCACTCGAGACGGTCGAGCAATCGCAAAGTTATGGCAACCTTATTGGAGTGCTCGTC'
s2 = 'TTGGTGTGTGCAACGGACTACGAACGAACCTGGCCACCGGACAGTTGGCCGGGCAGAGAAAAACTACTGCATCGCTTACCTGGCACCAGCATGCAAGGTATGTTAGACCCTTAAAAATAGATAGCCTCCACTCCGATAAGTCTGTTGCCAGGACGGTAAGTGGCTCAAAACCAGCCGGTTTTCAGTCATCCTAGTTTGATAACGCACGGGCTTCAACTAGGTTTAATCCGCTCGACTGGGGACTGAACAAGATGGTTGCTTTCGATAATTAAAGAAGTAGTGGGGATACTTTTGTGGCCGCTGACAGACAGGGGCAGCAGTAAGCATACGCATTTCTTCAGGCCCATGCAGTAGCGCATTAGCCTAGCGAGCACCGCTCGCATTTACGACGTAGGTCTTCAAGAGTCGGTTACTTGACCGACTCAAGATCTATTCGCGCACATGGTAAATCTGGCGACTCGCCACCAGATTCCTGGAGGGTCGGATAAGGAATGGTTACGCTTATTGAACGCACCCCCACCGCGGGAGTGGTTCAGGTCGCGGTCGGATCTAGAGCTACAAGCCTTCAATTCTATCAGGCCTCGGGACTGCTACGAGTCTCACGTTGAAAGCATGTATTGTTCAACACGGCGCGTGCCTGTGTCATAAATGTTAGAACTCGCTTGTGGCATAAAACTGTCATTCCTTTCGATAGCTGTACAATATCAGCATATACCAGACGCTACTACACCTATTAGGCTACATTGTAGCGCGAACAATACCATACTCTAGCTATGGGTCTACAGGCTGCGTCAATCTCAGGTTATTCACACAGAGTATGGCGTCGCAGAAGCTAGTGAAGTTACAGACAAGACGAGCATCTAGAATT'
otv = '';

a = [[0]*(1+len(s2)) for i in range(1+len(s1))]
      
for i in range(1,1+len(s1)):
    for j in range(1,1+len(s2)):
        if s1[i - 1]==s2[j - 1]:
            a[i][j]=a[i-1][j-1]+1
            
        else:
            a[i][j]=max(a[i][j-1],a[i-1][j])

def restore(i,j,otv):
    if i==0 or j==0:
        return;
    if s1[i-1]==s2[j-1]:
        otv = s1[i-1]+otv
        if len(otv)==a[len(s1)][len(s2)]:
            print otv
        restore(i-1,j-1,otv)
    else:
        if a[i-1][j]==a[i][j]:
            restore(i-1,j,otv)
        else:
            restore(i,j-1,otv)
            
sys.setrecursionlimit(2000) 
restore(len(s1),len(s2),otv)

