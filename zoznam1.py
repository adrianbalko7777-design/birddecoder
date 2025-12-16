import random
import math

def generuj(n: int) -> list:
   zoz = []
   for i in range(n):
       zoz.append(random.randrange(5, 101))
   return zoz


def sucet_parne(z:list)->int:
   a=0
   for i in range(len(z)):
       if z[i]%2==0:
           a+=z[i]
   return a
print(sucet_parne(generuj(10)))


def coho_je_viac (z:list) -> str:
   parne = 0
   neparne= 0
   for i in range(len(z)):
       if z[i]%2==0:
           parne+=1
       else:
           neparne+=1
   if parne>neparne:
       print('parne')
   elif neparne>parne:
       print('neparne')
   else:
       return'rovnake'


def parne_pozicie(zoz: list) ->list:
   zoz2 = []
   for i in range(len(zoz)):
       if i%2==0:
           zoz2.append(zoz[i])
   return zoz2
print(parne_pozicie(generuj(10)))

def nie_cisla(zoz: list) -> str:
    zoz2 = []
    for i in range(len(zoz)):
        if not (type(zoz[i])==int or type(zoz[i])==float):
            zoz2.append(zoz[i])
    return zoz2

print(nie_cisla(['kuk', 5, 'ahoj', -1, 2.5, 4, None, 7, [2,-12], 8, 'servus',11]))

def spolu_do_retazca(zoz:list) -> str:
   z =""
   for i in range(len(zoz)):
       z+= str(zoz[i])
   return z
print(spolu_do_retazca(generuj(10)))

'''return(",".join(zoz))'''

# Úloha 7
def zoznam_mocnin(n: int) -> list:
    zoz = []
    for i in range(1, n + 1):
        zoz.append(i ** 2)
    return zoz

print(zoznam_mocnin(6))

# Úloha 8
def ludolf(n: int):
    if n > 15:
        return False
    zoz = []
    for i in range(1, n + 1):
        zoz.append(round(math.pi, i))
    return zoz

print(ludolf(6))

# Úloha 9
def je_usp(z: list) -> bool:
    for i in range(len(z) - 1):
        if z[i] >= z[i + 1]:
            return False
    return True

print(je_usp([1, 5, 7, 12]))
print(je_usp([4, 1, 5, 2, 7, 12]))

# Úloha 10
def maxx(z: list):
    najv = z[0]
    for i in range(len(z)):
        if z[i] > najv:
            najv = z[i]
    return najv

print(maxx([4, 1, 5, 27, 7, 12]))

# Úloha 11
def ktory_min(z: list) -> int:
    najm = z[0]
    index = 0
    for i in range(len(z)):
        if z[i] < najm:
            najm = z[i]
            index = i
    return index

print(ktory_min([4, 1, 5, 27, -7, 12]))

# Úloha 12
def p_n(z: list) -> tuple:
    parne = []
    neparne = []
    for i in range(len(z)):
        if z[i] % 2 == 0:
            parne.append(z[i])
        else:
            neparne.append(z[i])
    return (parne, neparne)

print(p_n([2, 3, 5, 2, 1, 4, 6, 5, 3, 7]))

# Úloha bonus
def zisti(z: list, hodnota) -> bool:
    for i in range(len(z)):
        if z[i] == hodnota:
            return True
    return False

print(zisti([2, 3, 5, 2, 1, 4], 5))
print(zisti([2, 3, 5, 2, 1, 4], 10))