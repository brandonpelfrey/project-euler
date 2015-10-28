
memo = {}
def dr_paths(i,j):
  global memo
  if i == 0: return 1
  if j == 0: return 1

  tupl = (i,j)
  if tupl not in memo:
    memo[tupl] = dr_paths(i-1,j) + dr_paths(i,j-1)
  return memo[tupl]

print dr_paths(20, 20)

