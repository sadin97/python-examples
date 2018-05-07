fajl = open('test01.in', 'r')

lista = []
korisnici = []
shifre = []
nesigurne = []

for red in fajl:
    k = red.strip().split(" ", 1)
    lista.append(k)

#print(lista)

for i in range(len(lista)):
  korisnici.append(lista[i][0])
  shifre.append(lista[i][1])

#print(korisnici, shifre)
#['smart_user', 'admin', 'root', 'safe_user', 'user'] ['W ?4 M7Luj', 'admin', 'pass1234word', 'fa !70 gEVa1', 'abc']

for j in range(len(shifre)):
  if shifre[j] == korisnici[j] or len(shifre[j]) < 5 or "1234" in shifre[j]:
    nesigurne.append(korisnici[j])
    nesigurne.append(shifre[j])

brojac = 2

for k in nesigurne:
  brojac -= 1
  print(k, end=" ")
  if brojac == 0:
    print("")
    brojac = 2