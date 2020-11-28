def menu():
  print("1 - criar login")
  print("2 - formar a string de validacao")
  print("3 - para validar string no pagamento")

continuar = True
usuario_conta = {}
while continuar:
 menu()
 opcao = int(input("Digite a opçcao que deseja:\n"))
 if opcao == 1:
  continuar = "s"
  while continuar:
   identidade_conta = {}
   saldo = []
   contador_de_conta = 0
   nome =input("digite aqui seu nome:\n")
   senha = input("digite sua senha:\n")
   email = input("digite seu email:\n")
   contador_de_conta += 1 
   if contador_de_conta == +1:
    identidade_conta = contador_de_conta
    saldo = 1000
    valor = type(str(saldo))
    usuario_conta= nome, identidade_conta, email, saldo
    type(str(usuario_conta))
    continuar = False
    print(usuario_conta)
 elif opcao==2:
   continuar = True
   while continuar:
    quem = input("digite o nome de quem vai receber:\n")
    numero_da_conta = float(input("Qual a conta?\n"))
    valor = float(input("qual valor vai transferir? digita ai:\n"))
    mudar = "{};{};{}".format(quem.upper(), numero_da_conta, valor)
    if numero_da_conta == True: 
     print(mudar)
     continuar = False
    else:
     print("digite conta valida!")
 elif opcao ==3:
    continuar =True
    while continuar:
     nome = input ("digite o nome a que transferir:\n")
     numero_conta = input ("digite o numero da conta a quem transferir:\n")
     valor = input("digite o valor a transferir:\n")
     validacao = input("digite a validacao:\n")
     nome_validacao, numero_da_conta_validacao = validacao.split(';')
     if nome == nome_validacao and numero_da_conta == numero_da_conta_validacao:
      print ("dados validos!")
     else:
      print("Dados invalidos!")
 elif opcao == 0:
   continuar = False
 else:
   print("opção invalida!")
   input("Press enter to continue...")
