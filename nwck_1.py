import sys
from StringIO import StringIO
from Bio import Phylo



pairs = [l2.split('\n') for l2 in open('D:\\python\input.txt').read().strip().split('\n\n')]
for s, line2 in pairs:
    x, y = line2.split()
    tree = Phylo.read(StringIO(s), 'newick')
    sys.stdout.write('%s ' % int(tree.distance(x, y)))
    sys.stdout.write('\n')
