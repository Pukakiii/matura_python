# Schemat Hornera, konwersja w system dzisiętny
'''
A[(0, ...n),(p)] - tab. cyfr 
    A[0][0] - najb. znacząca cyfra A[0][n] - najmn. znacząca cyfra  
    n - ilość cyfr
    A[0][1] - p - podstawa systemu liczenia 
Wynik - W - wartość liczby A[0][0] w systemie dzisiętnym
    W <- A[0]
    dla i=1,2,..,n wykonaj
      W <- W*p+A[0][i]
    return W
'''
liczba=[[1,1,1],[2]]
def horner_alg(l):
  w=l[0][0]
  return w
print(horner_alg(liczba))