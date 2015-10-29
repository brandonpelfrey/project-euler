import itertools

products = set([])
for perm in itertools.permutations('123456789'):
  for i in xrange(1,4):
    for j in xrange(i+1,9-3):
      a = int(''.join(perm[ :i]))
      b = int(''.join(perm[i:j]))
      c = int(''.join(perm[j: ]))
      if a*b == c:
        print a, b, c
        products.add(c)

print '------'
print sum(products)
