terms = set([])
for a in xrange(2, 101):
  for b in xrange(2, 101):
    terms.add( a**b )
print terms
print len(terms)
