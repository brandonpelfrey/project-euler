
def pal_10(x):
  s = str(x)
  return s == s[::-1] and s[0] != '0'

def pal_2(x):
  s = "{0:b}".format(x)
  return s == s[::-1] and s[0] != '0'

S = 0
for i in xrange(1, 1000000):
  if pal_10(i) and pal_2(i):
    S += i
    print i, S
