fibs = [1,1]
while fibs[-1] <= 4000000:
  fibs.append( fibs[-1] + fibs[-2] )

even = lambda x: x%2 == 0
print sum( filter( even, fibs ) )
