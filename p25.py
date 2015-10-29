a, b = 1, 1
for i in xrange(3,10000):
  c = a + b
  if len(str(c)) >= 1000:
      print i
      break
  a, b = b, c
