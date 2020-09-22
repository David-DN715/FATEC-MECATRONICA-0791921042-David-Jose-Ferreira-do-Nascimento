# verificar se os numero faz parte de um triangulo
lado1 = int(input("digite um numero:\n"))
lado2 = int(input("digite um numero:\n"))
lado3 = int(input("digite um numero:\n"))

#Forma1
if (lado1 > 0) and (lado2 > 0) and (lado3 > 0):
  if (lado1+lado2) > lado3 and (lado2+lado3) > lado1 and (lado1 + lado3) > lado2:
    print('Pode formar um trinagulo!')

#Forma2
if (lado1 > 0) and (lado2 > 0) and (lado3 > 0) and (lado1+lado2) > lado3 and (lado2+lado3) > lado1 and (lado1 + lado3) > lado2:
  print('Pode formar um trinagulo!')
