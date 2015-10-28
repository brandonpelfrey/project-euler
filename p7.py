import math

primes = [2,3]
k = 1
while len(primes) < 10002:

  for q in [6*k - 1, 6*k + 1]:
    is_prime = True
    for p in primes:
      if q % p == 0:
        is_prime = False
        break
    if is_prime:
      print len(primes), q
      primes.append( q )

  k += 1

