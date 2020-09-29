#estrutura de repetição
numero_secreto = 42

acertou = False
while acertou == False:
 chute = int(input("Chute um numero"))
if chute > numero_secreto:
  print("errou por alto")
  elif < numero_secreto:
    print("errou por baixo")
    else:
      acertou= True
      print("acertou")

print("obrigado por jogar") 
