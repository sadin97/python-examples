recenica = input()

recenica.lower()

brojac_a = 0
brojac_e = 0

for slovo in recenica:
  if slovo == "a":
    brojac_a += 1
  if slovo == "e":
    brojac_e += 1

if brojac_a > brojac_e:
  print("A")
elif brojac_e > brojac_a:
  print("E")
else:
  print("AE")