# A função abaixo mostra o menu
def menu():
  print("0 - parar progama")
  print("1 - gerar requisição de pagamento!")
  print("2 - pagamento")

#usuarios abaixo fazem parte do progama!
email ='gokusola@dbz.com'
nome = 'goku'
senha = 'CHICHI'
saldo = 10000
identidade = 00.1
usuario_teste = email, nome, identidade, saldo

print(usuario_teste)

email ='principevegeta@dbz.com'
nome = 'vegeta'
senha = 'MinhaBulma'
saldo = 9000
identidade2 = 00.2
usuario_teste2 = email, nome, identidade2, saldo
print(usuario_teste2)

email ='Midorua_allmight@dbz.com'
nome = 'Midorya'
senha = 'Toshinori'
saldo = 10000
identidade3=00.3
usuario_teste3= email, nome, identidade3, saldo
print(usuario_teste3)

#a função abaixo buscar e traz o saldo da c
def buscar(validacao):
  encontrei = False
  for nome in validacao:
    if nome == validacao:
      print(nome)
      return encontrei 

import random
#a funçao abaixo gera a string com numero aleatorios
def mudar(quem, numero_da_conta, valor):
 numero_aleatorio = random.randint(1000,9999)
 type(str(numero_aleatorio))
 type(str(numero_da_conta))
 type(str(valor))
 mudar = "{};{};{};{}".format(quem.upper(), numero_da_conta, valor,numero_aleatorio)
 return mudar

#codigo principal:
import os
continuar = True
while continuar:
 os.system('clear')
 input("press any key...")
 menu()
 opcao = int(input("Digite a opçcao que deseja:\n"))
 #gerar requisição do pagamento
 if opcao == 1:
   continuar ='s'
   quem = input("DIGITE O NOME:\n")
   numero_da_conta = input("DIGITE A CONTA\n")
   valor = float(input("DIGITE VALOR:\n"))
   continuar = input("quer continuar?")=='s'
   print(mudar(quem, numero_da_conta, valor))
   os.system('clear')
   input("press any key...")
 elif opcao ==2:
   continuar = 's'
   nome = input("Informe seu nome:")
   valor = float(input("Informe um valor:"))
   identidade = input("Informe o número da conta:")
   validacao = input("DIGITE O CODIGO DE VALIDAÇÃO:\n")
   nome_validacao, identidade_validacao, numero_aleatorio_validacao, valor_validacao=validacao.split(';')
   if nome == nome_validacao and identidade == identidade_validacao:
    nome = nome_validacao
    print(buscar(nome_validacao))
   continuar = input("quer continuar?")=='s'
   
