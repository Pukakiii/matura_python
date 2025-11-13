# PRINT
#print(*objects, sep=' ', sepend=1\n')
print("Hello", "world")
print(10, 20, 30)
print(1, 2, 3, sep='-')
print("A", "B", "C", sep='')
print("A", "B", "C", sep='...')
print("Hello", end='!')
# print()
print("Line 1", end=' |  ')
print("Line 2")

for i in range(10):
    print(i, end=' ')
print()  # Dodanie nowej linii po pętli
for i in range(10):
    print(chr(65 + i), sep='',end='')
print()  # Dodanie nowej linii po pętli

name = "Ala"
age = 20
print(f"{name} ma {age} lat.")
print(f"{2+2} to cztery. {2} + {2} = {2+2}")

pi=3.141592653589793
print(f"Pi zaokraglone: {pi:.2f}")

# abs(x) - wartość bezwzględna
print(abs(-10))
print(abs(5))
wynik = 24-25
print(abs(wynik))

# pow(x, y) - potęgowanie x^y
print(pow(2, 3))
print(pow(5, 4.2))
print(pow(25, 0.5))
print(9 ** 0.5)

# divmod(x, y) - dzielenie z resztą, zwraca (iloraz, reszte)
q, r = divmod(10, 3)
print(f"iloraz 10/3:{q}, reszta10/3:{r}")
q, r = divmod(10, 3.4)
print(f"iloraz 10/3.4:{q}, reszta10/3.4:{r}")

# round(x, n) - zaokrąglanie do n miejsc po przecinku
print(round(3.14159))
print(round(3.14159, 2))

# bin(x)[2:] - zamiana liczby na system binarny
print(bin(10)) 
print(bin(10)[2:]) # bez prefiksu '0b'
print(bin(255)[2:])
# hex(x)[2:] - zamiana liczby na system szesnastkowy
print(hex(255))
print(hex(255)[2:]) # bez prefiksu '0x'
# oct(x)[2:] - zamiana liczby na system ósemkowy
print(oct(255))
print(oct(255)[2:]) # bez prefiksu '0o'

# int(x, podstawa) - zamiana liczby w danym systemie na dziesiętny
print(int('1010', 2))  # binarny na dziesiętny
print(int('ff', 16))   # szesnastkowy na dziesiętny
print(int('377', 8))   # ósemkowy na dziesiętn

print(int('25'))      # string na int
print(int(2.99))
print(int(-2.99))

# float(x) - zamiana na liczbę zmiennoprzecinkową
print(float(10))
print(float("3.14"))
# print(int("2.99")) #Błąd

# format(x, 'len sys') - sustem liczbowy z wiodącymi zerami
print(format(10, '08b'))  # binarny z 8 znakami
print(format(255, '08b'))
print(format(255, '08x'))
print(format(255, '08X'))
print(format(255, '08o'))
print(format(2, '04b'))

import math
# math.sqrt(x) - pierwiastek kwadratowy
print(math.sqrt(25)) #zwraca float
print(math.sqrt(2))
print(math.sqrt(0))
# print(math.sqrt(-2)) #Błąd 

# math.ceil(x) - zaokrąglenie w górę
# math.floor(x) - zaokrąglenie w dół
print(math.ceil(3.14))
print(math.ceil(-3.14))
print(math.ceil(3.0))
print() 
print(math.floor(3.14))
print(math.floor(-3.14))
print(math.floor(3.0))

# math.gcd(x, y) - (gcd-greatest common divisor) największy wspólny dzielnik
# math.lcm(x, y) - (lcm-least common multiple) najmniejsza wspólna wielokrotność
print()
print(math.gcd(12, 15))
print(math.gcd(100, 75))
print(math.gcd(0, 0))
print()
print(math.lcm(12, 15))
print(math.lcm(100, 75))  
print(math.lcm(4, 6))
print(math.lcm(0, 0))

'''STRING FUNKCJE'''
# s.strip()  # usuwa białe znaki z początku i końca
s = "   Hi world?   \n"
print(s)
print(s.strip())
print(s.lstrip())
print(s.rstrip())

# line.split() - dzieli string na liste 
line = "Jiao has a cat"
words = line.split()
print(words)
csv="2024;05;03"
print(csv.split(';'))

# dzieli na liste
print(list("Hello")) 

# "sep".join(words) - łączy liste w string z separatorem
words= ['ja', 'm', 'mam', 'kota']
print("".join(words))
print(" ".join(words))
print("-".join(words))

# a.replace(old, new) - zamienia old na new w stringu
a = "kiwi, kiwi, kiwi"
print(a)
print(a.replace("kiwi", "banan"))
print(a.replace("kiwi", "banan", 2))  # tylko 2 pierwsze

bin="0b101010"
print(bin.replace('0b', ""))
 
# s.find(sub) - zwraca indeks lub -1
text="To jest test"
print(text.find('jest')) # zwraca 3
print(text.find('nie ma')) # zwraca -1

print(text.index("test")) # 8
# print(text.index("brak")) # ValueError

#s.count(sub) - ile razy występuje wyszukiwany element:

bin = "1010100100101000010000101111"

print(bin.count("1"))
print(bin.count("0"))
print(bin.count("10"))
print(bin.startswith("1"))
print(bin.endswith("0"))

# s.lower() / s.upper()
stringi="Pithon"
print(stringi.lower())
print(stringi.upper())

# s.isdigit() - czy tylko cyfry
print("12345".isdigit())
print("12345abc".isdigit())

# s.isalpha() - czy tylko litery
print("abcdDEF".isalpha())
print("12345abc".isalpha())

# ord(c) - kod ASCII/Unicode
print(ord('A'))
print(ord('h'))
print(ord('ą')) # unicode! dla polskich znaków

# chr(n) - znak o kodzie n
print(chr(65))
print(chr(76))

# sub in s - czy jest podciąg
p="To jest test"
print("to" in p) #False
print("jest" in p) #True

'''Funkcje na listach'''
nums = [2, 9, 3, 7]
print(max(nums))
print(min(nums))
print(len(nums))
print(sum(nums))

print(sorted(nums))
print(sorted(nums, reverse=True))
sorted(nums) # - nie!!! zmienia listy
print(nums) 
nums.sort() # - zmienia!!! listy
print(nums) 
nums.reverse() # - odwraca i zmienia listę!
print(nums) 

#l.append(x) - dodaje na koniec
fruits=["mango", "banana"]
fruits.append('pear')
print(fruits)

# l.extend() - dodaje wiele
fruits.extend(["kiwi","melon"])
print(fruits)

# l.insert(index, element) - wstawia na pozycję
fruits.insert(1, 'watermelon')
print(fruits)
fruits.insert(0, 'aboilowaer')
print(fruits)

# l.pop() - usuwa element na końcu i go zwraca
fruit=fruits.pop()
print(fruit)

print(fruits.pop(1)) #usuwa z podanej pozycji
print(fruits)

# l.remove(element) - usuwa pierwsze wystąpienie
num=[1,2,2,3]
num.remove(2)
print(num)

num.clear() # - wyczyszcza listę
print(num)

# l.count(element) - liczba wystąpień
colors=["red",'green', 'red', "blue"]
print(colors.count('red'))

# l.index(element) - zwraca indeks pierwszego wystąpienia
print(colors.index("blue"))
# print(colors.find("blue")) - BŁĄD, find() nie działa na listach

# list(set(l)) - usunięcie powtórzeń z listy

numbers = [1, 2, 2, 4, 5,5 ,5]
unique = list(set(numbers))
print(unique)

# zip(l1, l2) - tworzy pary
names=["Ala", "Jan"]
ages=[18, 20]
print(list(zip(names,ages)))

for name, age in zip(names, ages):
    print(f"{name} ma {age} lat")

animals=["ryba", 'kot', "królik"]
for i, a in enumerate(animals):
    print(f"{i}: {a}")

# I
for i, (name, age) in enumerate(zip(names,ages)):
    print(f"{i}: {name} ma {age} lat")
# II
for i, value in enumerate(zip(names,ages)):
    name, age = value
    print(f"{i}: 2 {name} ma {age} lat")

# Operacje na zbiorach

# set(l) - tworzy zbiór , usuwa duplikaty
n=set(numbers)
print(n) # w klamrowych nawiasach
 
# z.add(x) - dodaje element do zbioru
zbiór={1,2}
zbiór.add(3)
print(zbiór)

# z.remove(x) - usuwa element (rzuca błąd jeśli nie ma)
zbiór.remove(2)
print(zbiór)

# z1.union(z2) - elementy z obu zbiorów
z1={1,2,4}
z2={3,4,5,6}
print(z1.union(z2))

# z1.intersection(z2) - wspólne elementy
z1={1,2,3}
z2={2,3,4}
print(z1.intersection(z2))

# z1.difference(z2) - zwraca elementy w z1, których nie ma w z2
print(z1.difference(z2)) 

"""Operacje na słownikach"""

# słownik.keys()/.values() - lista kluczy/wartości
slownik={"a":1,"b":2,"c":3}
print(list(slownik.keys())) # dodając metod .list() otrzymuje się czystą listę 
print(list(slownik.values())) # dodając metod .list() otrzymuje się czystą listę 

# slownik.items() - lista par (klucz, wartość)
print(slownik.items())
print(list(slownik.items()))
for k, w in slownik.items():
    print(f"{k}->{w}")

# slwonik.get(klucz, domyślna) - bezpieczne pobieranie
print(slownik.get("b")) 
print(slownik.get("x")) # NOne, bo nie ma klucza "x" w tym słowniku
print(slownik.get("x", 10)) # 0 (drugi argument to wartość domyślan, gdyby nie było poszukiwanego klucza)
print(slownik.get("b", 3)) # - nie zada ,poniewaz "b" klucz juz zdefioniowany

# slownik.clear() - czyści słownik
slownik.clear()
print(slownik)

# dict.fromkeys(lista kluczy, domyślna wartość)
klucze = [1,2,2,2,3,4,5,5,6,6,6,7,8,8,10]
slownik2= dict.fromkeys(klucze,0)
print(slownik2)
for klucz in klucze:
    slownik2[klucz]+=1
print(slownik2)

# slownik.default(klucz, domyślna) - ustawia tylko, jeśli klucza nie ma
slownik3={}
for klucz in klucze:
    slownik3.setdefault(klucz, 0)
    slownik3[klucz]+=1
print(slownik3)

# Counter z collections - zliczanie elementów
from collections import Counter

print(Counter("matura"))
klucze = [1,2,2,2,3,4,5,5,6,6,6,7,8,8,10]
licznik=Counter(klucze)
print(licznik)
print(dict(licznik))
posortowane=dict(sorted(licznik.items(), key= lambda x: x[1], reverse=True))
print(posortowane)

# Zamiana stringów na liczby
print(list(map(int, ['1','2','3'])))
print(list(map(float, ['1','2','3'])))

print(list(map(lambda x: x*2, [1,2,3])))

litery=['a','b','cde']
print(list(map(str.upper, litery)))

# lambda - funkcje anonimowe 

# prosta funkcja mnozaca x razy 2
f=lambda x: x*2
print(f(5))

# filter() Filtrowanie tylko liczby parzyste
klucze = [1,2,2,2,3,4,5,5,6,6,6,7,8,8,10]
print(list(filter(lambda x: x%2==0, klucze)))

# filter() Filtrowanie NIE pustych stringów
napisy=['', 'stringi  ', "  ", "abc"]
print(list(filter(lambda x: x.strip(), napisy)))

# sorted(lista, key=func, reverse=bool) - sortowanie według funkcji
imiona=['Jan', "aleksandra", "Piotr"]
print(sorted(imiona, key=len))

oceny={"Ala":3,"Jan":2,"Paweł":1}
print(sorted(oceny.items(), key=lambda x: x[1]))

liczby=[-10,3,1,-2]
print(sorted(liczby,key=abs, reverse=True))