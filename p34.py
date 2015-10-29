

def curious(x):
  factorial = lambda n: reduce(lambda a,b: a*b, range(1,n+1), 1)
  digits = map(int, list(str(x)))
  return x == sum(map(factorial, digits))

S = 0
for i in xrange(10, 1000000):
  if curious(i):
    S += i
    print i, S
