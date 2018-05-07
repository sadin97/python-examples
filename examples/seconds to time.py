s = 26110439 // 1000
print("sekunde koje treba pretvoriti:", s)
if(s > 60):
  m = s // 60
  s = s % 60
  print("minute:", m)
  print("sekunde:", s)
  if(m > 59):
    h = m // 60
    m = m / 60
    s = m % 60
    print("h: {}, m: {}, s: {}".format(h, m, s))