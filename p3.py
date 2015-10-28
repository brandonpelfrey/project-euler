import math

n = 600851475143
sqrt_n = int(math.sqrt(n))
print 'sqrt(n) =', sqrt_n

done = False
primes = [2,3]
k = 1
while 6*k <= sqrt_n and not done:
  for q in [6*k - 1, 6*k + 1]:

    is_prime = True
    for p in primes:
      if q % p == 0:
        is_prime = False
        break

    if is_prime:
      primes.append( q )

      # If this new prime divides whatever's left, reduce our problem
      if n % q == 0:
        r = 0
        while n % q == 0:
          n = n / q
          r += 1

        print 'New factor %s^%s -- %s remains' % (q, r, n)

        if n == 1:
          print 'Done'
          done = True

  k += 1

