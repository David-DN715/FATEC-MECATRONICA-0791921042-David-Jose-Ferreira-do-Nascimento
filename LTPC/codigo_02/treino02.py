#esse ("inf")O primeiro cria um número infinito, o segundo cria um número que não é um número "Not a Number"

#aqui declaramos variaveis para o funcionamento como continuar, maior, menor, a quantidade de numeros que digitei. 
maior = -float("inf")
menor = float("inf")
continuar ="sim"
quantos_numeros = 0 


#esse while faz a pergunta da condição de continuar até o usuario dizer que não quer mais, e comprara dentro dos if se o numero é maior ou menor.
while continuar == "sim":
  numero = int(input("digite um numero\n"))
  continuar = (input("deseja continuar\n"))
  if numero < menor:
    menor = numero
  if numero > maior:
    maior = numero
  quantos_numeros +=1
  soma = maior = menor
  

media = soma/quantos_numeros
print("menor", menor)
print("maior", maior)
print("media", media)
