n = float(input("Unesite broj: "))

lista = []

while(n > 0):
  n = float(input("Unesite broj: "))
  if(n >= 0):
    lista.append(n)
  else:
    break

print("Najveći uneseni decimalni broj je: {}, najmanji uneseni decimalni broj je: {}".format(max(lista), min(lista)))