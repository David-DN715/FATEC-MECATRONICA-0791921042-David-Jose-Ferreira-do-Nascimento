#progama que calcula o valor das parcelas
valor_total = float(input("digite o valor total"))
numero_parcelas =int(input("valor das parcelas"))


#olhas os numeros de numero_parcelas
if numero_parcelas == 1:
  parcelas = (valor_total*0.95)/numero_parcelas
elif numero_parcelas == 2:
  parcelas = valor_total/numero_parcelas
elif numero_parcelas ==3:
   parcelas = (valor_total*1.05)/numero_parcelas
else:
   parcelas = (valor_total*1.1)/numero_parcelas

print("Valor das parcelas:", parcelas)
