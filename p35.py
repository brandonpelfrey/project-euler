
n = 1000000
sieve = [0] * n
primes = []
for p in xrange(2, n):
  if sieve[p] == 0:
    primes.append(p)
    for pk in xrange(p*2, n, p):
      sieve[pk] = 1
primes = set(primes)

count = 0
for p in primes:
  p_str = str(p)

  all_rotations = True
  for i in xrange(len(p_str)):
    p_str = p_str[1:] + p_str[0]
    if int(p_str) not in primes:
      all_rotations = False
      break

    for i in xrange(len(p_str)):
      p_str = p_str[-1] + p_str[:-1]
      if int(p_str) not in primes:
        all_rotations = False
        break

  if all_rotations:
    count += 1
    print p, count
