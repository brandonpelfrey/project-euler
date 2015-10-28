is_palindrome = lambda x: str(x) == str(x)[::-1]

M = -1
for i in xrange(1000, 99, -1):
  for j in xrange(i-1, 99, -1):
    n = i * j
    if is_palindrome( n ):
      M = max(M, n)
print M
