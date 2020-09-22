#raizes de uma equação

#receber numeros da equação
a = float(input("digite um numero:"))
b = float(input("digite um numero:"))
c = float(input("digite um numero:"))

#vamos encontrar as raizes//potencia em PY
delta = (b**2)-(4*a*c)

#raiz do delta
if delta < 0:
 print ("Delta não tem raiz")
elif delta > 0:
  x1 =(-b +delta**0.5)/(2*a)
  x2 = (+b -delta**0.5)/(2*a)
  print ("Raizes", x1 , x2)
else:
  x2 = (-b - delta**0.5) / (2*a)
  print('Raiz:', x2)
