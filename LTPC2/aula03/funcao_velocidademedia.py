def leitura ():
  spaco_inicial = float(input("Digite o espaço inicial:\n"))
  spaco_final = float(input("Digite o espaço Final:\n"))
  tempo_inicial = float(input("Digite o tempo inicial:\n"))
  tempo_final = float(input("Digite o tempo Final:\n"))
  return spaco_inicial, spaco_final, tempo_inicial, tempo_final

def vel(spaco_final, spaco_inicial, tempo_final, tempo_inicial):
    return (spaco_final - spaco_inicial)/(tempo_final - tempo_inicial)

spaco_inicial,spaco_final,tempo_inicial,tempo_final = leitura()
resultado = vel(spaco_final, spaco_inicial, tempo_final, tempo_inicial)
print(f" A Velocidade é {resultado}")
