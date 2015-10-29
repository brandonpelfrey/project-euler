import itertools
coins = [1, 2, 5, 10, 20, 50, 100]
ways = 0

def rsum(so_far, place):
  global coins, ways
  coin = coins[place]

  max_p = (200 - so_far) / coin + 1
  for p in xrange(max_p):
    with_p_coins = so_far + coin * p

    if with_p_coins == 200:
      ways += 1

    if with_p_coins < 200 and place + 1 < len(coins):
      rsum(with_p_coins, place+1 )

rsum(0, 0)
print ways + 1
