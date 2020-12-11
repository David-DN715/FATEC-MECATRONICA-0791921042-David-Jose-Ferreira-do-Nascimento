#pedir que o usuario digite 2 numeros e diga se o numero é par ou impar
def par_impar(num1, num2):
 if num1 > num2:
   num1 %2 ==0
   print("Maior numero par:\t",num1)
 if num2 > num1:
   num2 %2 == 0
   print("Maior numero par:\t",num2)
 elif num1 %2 != 0:
   print("maior numero impar:\t", num1)
 elif num2 %2 != 0:
   print("maior numero impar:\t", num2)
 else:
   print("Tá de brincation whit me?")
   return num1, num2

num1 = int(input("DIGITE UM NUMERO:\n"))
num2 = int(input("DIGITE UM NUMERO:\n"))

par_impar(num1, num2)
