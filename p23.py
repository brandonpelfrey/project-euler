from collections import defaultdict

limit = 28123
n = limit

# Much faster than factorization :)
divisors = defaultdict(set)
for i in xrange(1, n):
  for k in xrange(i, n, i):
    if i < k:
      divisors[k].add(i)

def is_abundant(x):
  return sum( divisors[x] ) > x

abundants = sorted( filter(is_abundant, xrange(1,limit)) )

# Brute-force produce all the abundant sums
combos = set([])
for x in abundants:
  for y in abundants:
    if y > x: break
    combos.add(x+y)

# sum( numbers which aren't abundant )
print sum( set(xrange(1, limit + 1)) - combos )
