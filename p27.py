n = 2000
sieve = [0] * n
primes = []
for p in xrange(2, 2000):
  if sieve[p] == 0:
    primes.append(p)
    for pk in xrange(p*2, n, p):
      sieve[pk] = 1

M = 0
for a in xrange(-999, 1000):
  for b in xrange(0, 1000):
    Lab = 0
    n = 0
    while n*n + n*a + b in primes:
      n += 1

    if n > M:
      M = n
      print a, b, n
