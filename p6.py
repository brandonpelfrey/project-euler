square = lambda x: x*x

n = range(1,101)
a = sum(map(square, n))
b = square(sum(n))
print b - a
