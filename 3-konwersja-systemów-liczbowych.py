# Schemat Hornera, konwersja w system dzisiętny
'''
A[(0, ...n),(p)] - tab. cyfr 
    A[0][0] - najb. znacząca cyfra A[0][n] - najmn. znacząca cyfra  
    n - ilość cyfr
    A[1][0] - p - podstawa systemu liczenia 
Wynik - W - wartość liczby A[0][0] w systemie dzisiętnym
    W <- A[0]
    dla i=1,2,..,n wykonaj
      W <- W*p+A[0][i]
    return W
'''
liczba=[[1,5,6,1,7],[8]]
def horner_alg(l):
  w=l[0][0]
  li=liczba[0]
  for k in li[1:]:
    # print('1')
    w=w*l[1][0]+k
    print(w)
    print(k)
  return w
print(horner_alg(liczba))