
def random_points(max_n):
  S = {0: 290797}
  for n in xrange(2*max_n):
    S[n+1] = (S[n] ** 2) % 50515093

  T = {}
  for key, val in S.items():
    T[key] = (val % 2000) - 1000

  return map(lambda k: (T[2*k-1], T[2*k]), xrange(1, max_n+1) )

n_points = 500
points = random_points(n_points)
