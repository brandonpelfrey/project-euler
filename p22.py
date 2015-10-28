names = open('inputs/p022_names.txt').read().replace('"', '').split(',')
names = map(str.lower, names)
names = sorted(names)

Q = 'abcdefghijklmnopqrstuvwxyz'
S = 0
for position, name in enumerate(names):
  letters = sum( map(lambda c: Q.index(c) + 1, name) )
  S += (position + 1) * letters
  print name, position, letters, S
