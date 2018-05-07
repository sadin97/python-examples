import random

BROJ_SIM = 10000

ulog = int(input("Unesite ulog: "))
opklada = int(input("Unesite opkladu: "))
cilj = int(input("Unesite koliko zelite osvojiti: "))

broj_pobjeda = 0
for s in range(BROJ_SIM):
    novac = ulog
    while novac > 0 and novac < cilj:
        if random.randrange(0, 100) < 49:
            novac += opklada
            print("Dobio si opkladu! Trenutni novac:", novac)
        else:
            novac -= opklada
            print("Izgubio si opkladu! Trenutni novac:", novac)
    if novac >= cilj:
        broj_pobjeda += 1
        print("Dobio si jos jednu pobjedu! Sada imas ukupno pobjeda:", broj_pobjeda)
        
print(broj_pobjeda/BROJ_SIM)