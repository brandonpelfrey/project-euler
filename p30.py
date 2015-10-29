def f(x):
  digits = map(int,list(str(x)))
  return x == sum(y**5 for y in digits)

S = 0
for x in xrange(2,2000000):
  if f(x):
    S += x
    print x, S
