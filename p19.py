from datetime import timedelta, date

end = date(2000, 12, 30)
current = date(1901, 1, 1)

sunday_count = 0
while current < end:
  current += timedelta(1)
  if current.isoweekday() == 7 and current.day == 1:
    sunday_count += 1
    print current, sunday_count


