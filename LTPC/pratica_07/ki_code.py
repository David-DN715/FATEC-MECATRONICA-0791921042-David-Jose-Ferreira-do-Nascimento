continuar = True
while continuar:
  nome = input("digite seu nome:")
  if nome == "kuririn":
    continuar = False
  else:
    KI = int(input("digite seu KI:"))
    if KI > 8000:
      print("Maldito Kakaroto")
    else:
      print("Saia daqui seu verme!!")  
