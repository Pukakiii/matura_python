liczba_całkowita = 5 # Przykładowa liczba całkowita - int 
print(type(liczba_całkowita))

liczba_zmiennoprzecinkowa = 3.0 # Przykładowa liczba zmiennoprzecinkowa - float 
print(type(liczba_zmiennoprzecinkowa))

wartość_logiczna = True # Przykładowa wartość_logiczna - bool 
print(type(wartość_logiczna))

tekst = "Przykładowy tekst" # Przykładowa tekst - str 
print(type(tekst))

lista = [1, 2, 3, 4, 5] # Przykładowa lista - list 
print(type(lista))

# True jest rownóważne 1, False 0 w operacjach matematycznych
print(True+2)
print(False*4)

# Działania mieszane int + float dają zawse float
print(3.0+2)

lista = [1, 1, 'hello', False]
print(type(lista), lista)

krotka=(1,3,4) # tuple - niemutowalna kolekcja (nie moŻna zmieniać po utworzeniu)
print(type(krotka), krotka)

zbiór = set(lista) # set- kolekcja unikalnych wartości, bez indeksów
print(type(zbiór), zbiór)

słownik = {"klucz": "wartość", "wiek": 30} # dict - przechowuje pary klucz-wartość
print(type(słownik), słownik)

lista[0]= 10
print(lista[0])
print(list(krotka))

print(list(zbiór)[-1])

brak_wartości = None; 

# Dynamiczna zmiana typu
x=5
print(x, type(x))
x+=5.0
print(x, type(x))
x="hellp"
print(x, type(x))

# Dzielenie 
# / daje zawsze wynik typu float 
wyraŻenie = 5/2
print(wyraŻenie, type(wyraŻenie))
# // daje dzielenie całkowite (część całkowitą)
wyraŻenie = 5//2   
print(wyraŻenie, type(wyraŻenie))

# Kopiowanie listy
lista1=[1,2,3]
lista2=lista1 #płytka kopia - kopiuje referencje do zagnieŻdŻonych struktur - shallow copy
lista1[1]="zmiana"
print("lista2=lista1.copy():", lista2, end="\n\n")

import copy
lista3=copy.deepcopy(lista1)
lista1[1]= "inna zmiana"
print("lista3=copy.deepcopy(lista1):", lista3)
print("lista1", lista1)

# Modulo
print(5%2)
print(5.5%2)

# Potęgowanie i MnoŻenie
print(2**3*2)
print(2**2*3)

# Operator 'is' i '==' 
# == porównuje zawartość, is porównuje obiekty w pamięci
a=[1,2,3]
b=[1,2,3]
c=a
print(a==b)
print(a is b)
print(a is c) #poniewaŻ "c" to jest wskaźnik w pamięci na tę listę

# Wartości w strukturach danych
print(bool([]))
# False
print(bool(["a"]))
# True
print(bool(""))
# False
print(bool("Python"))
# True
print(bool([""]))
# False

# Porównywanie typów

#True i False
print("1 == True:", 1==True) #True
print("0 == False:", 0==False) #True

print("None == False:", None == False) # False
print("None == 0:", None == 0) # False

#Zakresy - range
# range generuje sekwencję liczb, stop jest wykluczony

#range(start,stop,step)
print(list(range(0,5,2)))
print(list(range(4,10,2)))
print(list(range(0,11,2)))

#Slice - wycinanie fragmentów kolekcji
LISTA7=[0,1,2,3,4,5]
# start : stop : step
print(LISTA7[:3])
print(LISTA7[3:])
print(LISTA7[::-1])
print(LISTA7[::2])
print(LISTA7[1::2])
print(LISTA7[-3:])
print(LISTA7[:-3])

