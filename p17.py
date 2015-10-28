def wordy(n):
  words = { 1: 'one',
            2: 'two',
            3: 'three',
            4: 'four',
            5: 'five',
            6: 'six',
            7: 'seven',
            8: 'eight',
            9: 'nine',
            10: 'ten',
            11: 'eleven',
            12: 'twelve',
            13: 'thirteen',
            14: 'fourteen',
            15: 'fifteen',
            16: 'sixteen',
            17: 'seventeen',
            18: 'eighteen',
            19: 'nineteen',
            20: 'twenty',
            30: 'thirty',
            40: 'forty',
            50: 'fifty',
            60: 'sixty',
            70: 'seventy',
            80: 'eighty',
            90: 'ninety',
            100: 'hundred',
            1000: 'thousand',
            'and': 'and'}

  s = []
  if n >= 1000: s += [ n//1000, 1000 ]

  if n >= 100 and n%1000 != 0:
    s += [ (n%1000) // 100, 100]

  if n > 100 and n%100 != 0:
    s += ['and']

  if n%100 > 0:
    if n%100 < 20:
      s += [n%100]
    else:
      tens = n%100 - n%10
      s += [tens]
      if n % 10 != 0:
        s += [n%100 - tens]


  result = ' '.join(words[w] for w in s)
  return result

S = 0
for n in xrange(1,1001):
  english = wordy(n)
  print str(n).ljust(5), english
  S += len( english.replace(' ','') )
print S


