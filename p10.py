import math

class Primes:
  def __init__(self, n, Q=32):
    self.n = n
    self.bucket_bits = Q
    self.bits = [0] * ( (n // Q) + 1)

  def get(self, i):
    m = i // self.bucket_bits
    bucket_index = i - m * self.bucket_bits
    B = self.bits[ m ]
    return (B >> bucket_index) & 1

  def set(self, i):
    m = i // self.bucket_bits
    bucket_index = i - m * self.bucket_bits
    self.bits[m] |= (1 <<bucket_index)

# Sum of the primes < 2mil

N = 2000000
primes = Primes(N+2)
p = 2
while p < N:
  if primes.get(p) == 0:
    k = 2*p
    while k <= N:
      primes.set(k)
      k += p
  p += 1

P = 0
for i in xrange(2, N):
  if primes.get(i) == 0:
    print i
    P += i
print 'sum',P
