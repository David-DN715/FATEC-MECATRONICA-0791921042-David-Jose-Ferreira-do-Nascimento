#a biblioteca random abaixo permite que possa gerar numeros aleatorios!
import random

# A função abaixo mostra o menu
def menu():
  print("0 - parar progama")
  print("1 - criar login")
  print("2 - gerar requisição de pagamento!")
  print("3 - pagamento")

#a funçao abaixo gera a string com numero aleatorios
def mudar(quem, numero_da_conta, valor):
 numero_aleatorio = random.randint(1000,9999)
 type(str(numero_aleatorio))
 type(str(numero_da_conta))
 type(str(valor))
 mudar = "{};{};{};{}".format(quem.upper(), numero_da_conta, valor,numero_aleatorio)
 return mudar

#dicionarios que contem as informações dos usuarios!
conta001 ={'nome': 'Goku kakaroto', 'email':'gokukakaroto@dbz.com','saldo':'10000'}

conta002 ={'nome': 'Principe Vegeta', 'email':'vegetaprincipe@dbz.com','saldo':'9000'}

conta003 ={'nome':'Moro', 'email':'moro_absorvoki@dbz.com','saldo':'1000'}

#a função abaixo era para fazer a busca das contas declaradas abaixo e validar elas, porem não funciona!
def buscar(conta_busca):
  encontrei = False
  for conta in conta_busca.split(';'):
   if conta == conta001:
    print(conta_busca)
    encontrei = True
    if conta == conta002:
      print(conta_busca)
    encontrei = True
    if conta == conta003:
      print(conta_busca)
      encontrei = True
      return encontrei 
  
#codigo principal:
import os
continuar = True
while continuar:
 os.system('clear')
 input("press any key...")
 menu()
 opcao = int(input("Digite a opçcao que deseja:\n"))
 if opcao ==1:
   print("opção fora do ar!... desculpe pelo transtorno!")
   os.system('clear')
   input("press any key...")
   #a opção abaixo gera a string de validação, ela funciona!
 elif opcao ==2:
   continuar = "s"
   while continuar:
    quem = input("digite o nome de quem vai transferir:\n")
    numero_da_conta = input("Digite o numero da conta:\n")
    valor = input("digite o valor a transferir:\n")
    continuar = input("deseja fazer mais uma?")=='s'
    print(mudar(quem, numero_da_conta, valor))
    #a função abaixo pede para digitar a string de validação porem não funciona!
 elif opcao == 3:
   conta = input("Digite o codigo de validação:\n")
   print(buscar(conta))
   os.system('clear')
   input("press any key...")
   continuar = input("Voltar ao menu press any key..?")=='s'
   #A opção abaixo para o progama!
 elif opcao == 0:
   continuar = False  
 else:
   print("opção invalida!")
   input("Press enter to continue...")
