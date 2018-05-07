#Sadin Pita - Zadaća 07 - 15.12.2017.
#Zadatak 3

from math import fabs

#funkcija koja sabira cifre varijable x koju proslijeđujemo
def suma_cifara(x):
    suma = 0
    while x > 0:
        y = x % 10
        suma += y
        x //= 10
    return suma

#funkcija koja trazi najvecu sumu
def najveca_suma(lista):
    a = -1
    for i in range(len(lista)):
        if suma_cifara(fabs(lista[i])) > a:
            a = suma_cifara(fabs(lista[i]))
    maximum = lista[0]
    for i in range(len(lista)):
        if suma_cifara(fabs(lista[i])) > suma_cifara(fabs(maximum)):
            maximum = lista[i]
    return maximum

lista = [22, 3, 87, -23, -2004, -789]
print(najveca_suma(lista))