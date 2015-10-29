
n = 1000000
sieve = [0] * n
primes = []
for p in xrange(2, n):
  if sieve[p] == 0:
    primes.append(p)
    for pk in xrange(p*2, n, p):
      sieve[pk] = 1
primes = set(primes)

S = 0
count = 0
for p in primes:
  p_str = str(p)

  truncations = []
  for i in xrange(1,len(p_str)):
    truncations.append( p_str[:i] )
    truncations.append( p_str[i:] )

  truncations = map(int, truncations)
  all_prime = all(map(lambda x: x in primes, truncations))
  if all_prime:
    S += p
    count += 1
    print p, count, S

print S - 2 - 3 - 5 - 7
