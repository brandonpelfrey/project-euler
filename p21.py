
memo = {}
def proper_divisors(x):
  global memo
  if x not in memo:
    memo[x] = filter(lambda q: x%q == 0, xrange(1, x))
  return memo[x]

def d(x):
  return sum( proper_divisors(x) )

amicable_sum = 0
for x in xrange(1,10000):
  S = d(x)
  if x != S and x == d(S):
    amicable_sum += x
    print amicable_sum
