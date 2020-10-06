#V_out: Tensão de Saída
#T_ON: Tempo em nível alto
#T: Período total do sinal
#V_ON: Tensão em nível alto
continuar ="sim"

while continuar == "sim":
 T=float(input("digite o periodo total"))
 V_on =float(input("digite a tensão no nivel alto:"))
 T_on = float(input("digite o tempo que se manteve ativo :"))
 continuar = input("quer continuar?")
 if T == 0:
    T=float(input("redigite o periodo total:"))
 if V_on == 0:
    V_on = int(input("redigite a tensão no nivel alto:"))
 else:
    V_out = T_on/T*V_on

print(V_out)
