
D = '123456789'
for a in D:
  for b in D:
    for c in D:
      for d in D:
        ai, bi, ci, di = map(int, [a,b,c,d])
        num = ai * 10 + bi
        denom = ci * 10 + di

        if denom <= num: continue
        if b == d and ai*denom == ci*num:
          print '%s%s / %s%s == %s / %s' % (a,b,c,d, a,c)

        if b == c and ai*denom == di*num:
          print '%s%s / %s%s == %s / %s' % (a,b,c,d, a,d)
