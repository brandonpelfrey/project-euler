
lines = open('inputs/p18.txt','r').readlines()
numbers = map(int, (' '.join(lines)).split(' ') )
rows = []
ptr, stride = 0, 1
while ptr < len(numbers):
  rows.append( numbers[ptr:ptr+stride] )
  ptr, stride = ptr + stride, stride + 1

memo = {}
def dp(i, j, rows):
  global memo

  if i == len(rows)-1:
    return rows[-1][j]

  tupl = (i,j)

  if tupl not in memo:
    left  = rows[i][j] + dp(i+1, j, rows)
    right = rows[i][j] + dp(i+1, j+1, rows)
    memo[tupl] = max(left, right)

  return memo[tupl]

print dp(0, 0, rows)
