def menu():
  print("1 - somar ")
  print("2 - subtrair ")
  print ("3 - dividir ")
  print("4 - multiplicar")


def soma(num1, num2):
  return num1+num2

def subtração(num1, num2):
  return num1-num2

def dividir(num1, num2):
  if num2 != 0:
    return num1/num2
  else:
    return "Divisão por zero!"

def multiplicar(num1, num2):
  return num1*num2

continuar = True
import os
while continuar:
  os.system('clear')
  menu()
  opcao = int(input("Qual opção vai escolher?\n"))
  if opcao == 1:
    num1 = int(input("Digite um numero:\n"))
    num2 = int(input("Digite um numero:\n"))
    print(soma(num1, num2))
  elif opcao == 2:
    num1 = int(input("Digite um numero:\n"))
    num2 = int(input("Digite um numero:\n"))
    print(subtração(num1, num2))
  elif opcao == 3:
    num1 = int(input("Digite um numero:\n"))
    num2 = int(input("Digite um numero:\n"))
    print(dividir(num1, num2))
  elif opcao == 4:
    num1 = int(input("Digite um numero:\n"))
    num2 = int(input("Digite um numero:\n"))
    print(multiplicar(num1, num2))
  elif opcao == 0:
    continuar = False
  else:
    print("Invalid option!")
  input("press any key ")
