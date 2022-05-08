import math as m
def Newton(n,k):
  wynik= m.factorial(n) / (m.factorial(k)*m.factorial(n-k))
  return wynik
n_k= input()
wartosci=n_k.split(" ")
n=int(wartosci[0])
k=int(wartosci[1])
if k == 0 or k == n : 
  print('1')
else : 
  print(int(Newton(n,k)))