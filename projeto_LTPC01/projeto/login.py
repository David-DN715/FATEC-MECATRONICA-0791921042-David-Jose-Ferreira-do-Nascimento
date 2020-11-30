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
