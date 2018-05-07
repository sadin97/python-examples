poeni = 0

for i in range(1, 500, 1):
  print("Za skill: ", i, " potrebno je: ", i*2, " poena.")
  poeni += i*2

print("Ukupno poena do full job skilla: ", poeni)