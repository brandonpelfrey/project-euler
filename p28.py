S = 1
m, n = 1, 2
for i in xrange(2):
  for j in xrange(4):
    m += n
    S += m
  n += 2
print S
