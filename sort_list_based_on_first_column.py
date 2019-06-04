from operator import itemgetter
L=[[0, 1, 'f'], [4, 2, 't'], [9, 4, 'afsd']]
sorted(L, key=itemgetter(2))
#[[9, 4, 'afsd'], [0, 1, 'f'], [4, 2, 't']]