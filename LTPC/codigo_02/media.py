#esse codigo faz com que o usuario digite numeros quantas vezes ele quiser e depois ele imprime a media deles.

continuar = "sim"
contador = 0
quantidade_numeros = 0 

while continuar =="sim":
  numero = float(input("digite um numero:\n"))
  continuar = input("deseja continuar?\n")
  contador = contador +1
  quantidade_numeros = quantidade_numeros+1
  if numero %2 ==0:
    valor = numero
    contador = contador +1
  else:
    valor = numero
    contador = contador +1

soma = valor + valor 
media = soma/quantidade_numeros
print("media =", media)
