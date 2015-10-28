mult = lambda x: x%3 == 0 or x%5 == 0
print sum(filter(mult, xrange(1000)))
