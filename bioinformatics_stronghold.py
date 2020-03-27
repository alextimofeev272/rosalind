# solve problems from rosalind.info
# Discover the algorithms underlying a variety of bioinformatics topics: computational mass spectrometry,
# alignment, dynamic programming, genome assembly, genome rearrangements, phylogeny, probability,
# string algorithms and others.

def HAMM(path):
    # Расстояние Хэмминга. Две цепочки ДНК, найти мутации(т.е. отличия)
    # Given two strings s and t of equal length, the Hamming distance
    # between s and t, denoted dH(s, t), is the number of corresponding symbols
    # that differ in s and t.
    # Given: Two DNA strings s and t of equal length(not exceeding 1 kbp).
    # Return: The Hamming distance dH(s, t).
    file = open(path, 'r')
    first = file.readline(1000)
    second = file.readline(1000)
    a, i = 0, 0
    for x in first:
        if second[i] <> x:
            a += 1
        i += 1
    print(a)
    file.close()

def IPRB(k,m,n):
    # Даны 3 числа: k,m,n
    # k - гомозиготные доминантные
    # m - гетерозигоные
    # n - гомозиготные рецесивные
    # k + m + n - общая популяций организмов
    # Найти вероятность что спаривание двух любых организмов приводит
    # к образованию организма с доминантной аллелем.

    def prob(k, m):
        return float(k) / float(m)

    def probline(k, m, n):
        s = k + m + n
        return prob(k, s) * prob(k - 1, s - 1), prob(k, s) * prob(m, s - 1), prob(k, s) * prob(n, s - 1)

    k = 23
    m = 15
    n = 17

    Pk = probline(k, m, n);
    Pm = probline(m, k, n);
    Pn = probline(n, k, m);

    P = Pk[0] + Pk[1] + Pk[2] + Pm[0] * 0.75 + Pm[1] + Pm[2] * 0.5 + Pn[1] + Pn[2] * 0.5

    print (P)

