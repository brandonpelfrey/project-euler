
def collatz_length(n):
  length = 1
  while n != 1:
    n = n/2 if n%2 == 0 else 3*n+1
    length += 1
  return length

M = 0
for n in xrange(2,1000000):
  c = collatz_length(n)
  if c > M:
    M = c
    print n, c
