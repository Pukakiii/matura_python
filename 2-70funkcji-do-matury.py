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
