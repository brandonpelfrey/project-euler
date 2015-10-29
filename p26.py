def cycle_length(x):
  M = 10
  digits = []
  remainders = []

  for it in xrange(20000):
    if M == 0: break
    if M in remainders:
        return it - remainders.index(M)

    div = M // x
    digits.append( div )
    remainders.append( M )

    M = (M - x * div) * 10

  return 0

max_val = 0
for i in xrange(1,1000):
  Ci = cycle_length(i)
  if Ci > max_val:
    max_val = Ci
    print 'cycle_length(%s) = %s' % (i, Ci)
