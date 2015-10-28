for a in xrange(3,1000):
  for b in xrange(1,a):
    c = 1000 - a - b
    if a*a + b*b == c*c:
      print a*b*c
