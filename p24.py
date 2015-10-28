import itertools

G = itertools.permutations('0123456789')
for i in xrange(1,1000003):
  x = G.next()
  if i >= 999995:
    print i, ''.join(x)
