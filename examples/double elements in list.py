lista = []
for i in range(0, 10):
    lista.append(int(input()))
    
lista.sort() #sortira listu
print(lista)


nova_lista = []

for j in lista:
  if j not in nova_lista:
    nova_lista.append(j)

print(nova_lista)
print(nova_lista[2])