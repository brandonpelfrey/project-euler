nums = range(2,21)

def product(A):
  return reduce(lambda x,y: x*y, A, 1)

def divisible(x, y):
  return x % y == 0

n = 20
while True:
  all_divisible = True
  for num in nums:
    if not divisible(n, num):
      all_divisible = False
      break

  if all_divisible:
    print n
    break
  else:
    n += 20



