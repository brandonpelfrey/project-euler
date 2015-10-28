import math, numba

class Primes:
  def __init__(self, n, Q=32):
    self.n = n
    self.bucket_bits = Q
    self.bits = [0] * ( (n // Q) + 1)
    self.p = 1
    self.set( 1 )
    self.prime_cache = []

  def get(self, i):
    m = i // self.bucket_bits
    bucket_index = i - m * self.bucket_bits
    B = self.bits[ m ]
    return (B >> bucket_index) & 1

  def set(self, i):
    m = i // self.bucket_bits
    bucket_index = i - m * self.bucket_bits
    self.bits[m] |= (1 <<bucket_index)

  def compute_max_primes(self):
    while self.p < self.n:
      self.advance_p()

  def advance_p(self):
    # Advance p so that we have captured all the primes up to p
    while self.p < self.n:
      if self.get(self.p) == 0:

        # Mark all the mutliples of p which are >p as composite
        # in our bit mask
        k = 2 * self.p
        while k <= self.n:
          self.set(k)
          k += self.p

        self.prime_cache.append(self.p)
        self.p += 1
        return self.p

      self.p += 1

  def all_prime_divisors(self, num):
    #while self.p < self.n and self.p <= num:
    #  self.advance_p()

    for q in self.prime_cache:
      if num % q == 0:
        yield q


primes = Primes(1 * 1000 * 1000)
primes.compute_max_primes()
primes = primes.prime_cache

@numba.autojit
def D(n):
  R = 1
  for pi in xrange(len(primes)):
    p = primes[pi]
    if p > n: break
    if n%p != 0: continue

    k = 1
    while n % p == 0:
      k += 1
      n = n / p
    R *= k
  return R

M = 0
for i in xrange(1, 100000):
  triangle = (i+1) * i / 2

  tM = D( triangle )
  if tM > M:
    M = tM
    print 'New Max',i, triangle, tM
    if M > 1000:
      break




