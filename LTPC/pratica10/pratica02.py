#aqui definimos a função:
def lerNumeroPositivo():
  continuar = True
  while continuar==True:
    numero = int(input("Informe um valor:"))
    continuar = numero < 0
  return numero

#definimos outra função para soma de dois numeros:
def somar_dois_numeros(numero1,numero2):
  return numero1+numero2
#Aqui definimos uma saida da função que queremos na resultante:
def exibir_saida_formatada(numero1, numero2, resultado):
  #a função .format ela se vira com a informação que lhe é passada assim na solução de {} não precisa identificar o dade se é int ou float!
  print("A soma de {} com {} é igual: {}".format(numero1, numero2, resultado))
  print("A soma de %i com %i é igual: %i" % (numero1, numero2, resultado))

primeiro_valor = lerNumeroPositivo()
segundo_valor = lerNumeroPositivo()
resposta = somar_dois_numeros(primeiro_valor, segundo_valor)
#chamamos a função e executamos ela:
exibir_saida_formatada(primeiro_valor, segundo_valor, resposta)
