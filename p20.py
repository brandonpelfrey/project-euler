fact = lambda n: reduce(lambda x,y: x*y, xrange(1,n+1), 1)
print sum([int(c) for c in str(fact(100))])
