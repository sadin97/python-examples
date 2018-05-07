s1 = "Sarajevo".lower()
s2 = "raja".lower()

current_pos = 0

for i in s2:
  print("current_pos: ", current_pos)
  current_pos = s1.find(i, current_pos) + 1
  print("current_pos: ", current_pos)
  print("i: ", i)
  if current_pos == 0:
    rez = False
  else:
    rez = True

print(rez)