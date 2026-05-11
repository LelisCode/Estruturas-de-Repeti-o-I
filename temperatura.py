# 2. Monitor de Temperatura de Servidor
# Monitorar um valor constante e agir caso ultrapasse o limite.

# Lógica: Implementar um loop que "escuta" um sensor (valor manual) até que o sistema seja desligado.

# Regra: Temperatura limite do servidor: 80 ºC

# Resultado Esperado: Alerta de "Resfriamento ativado"

l = 80
s_l = True

print("Iniciando monitoramento do sistema")

while s_l:
    # Entrada do valor
    t = int(input("\nDigite a temperatura atual (ou 0 para terminar): "))

    if t == 0:
        print("Desligando sistema...")
        sistema_ligado = False
    
    elif t >= l:
        print(f" {t}ºC! RESFRIAMENTO ATIVADO.")
        
       #Resfria até 20 graus
        for r in range(t, 19, -1):
            print(f"Resfriando... {r}ºC")
            
        print(" Temperatura estável.")
    
    else:
        print(f"Temperatura {t}ºC: encontra-se normal.")
