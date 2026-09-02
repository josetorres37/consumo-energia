# Solicitando os dados do usuário
aparelho = input("Digite o nome do aparelho: ")
potencia = float(input(f"Digite a potência do(a) {aparelho} em Watts (W): "))
horas_dia = float(input(f"Digite o tempo médio de uso diário em horas: "))

# Calculando o consumo mensal em kWh
# Fórmula: (Potência * Horas * 30 dias) / 1000
consumo_mensal = (potencia * horas_dia * 30) / 1000

# Calculando o custo estimado (Dica da atividade: R$ 0,75 por kWh)
custo_estimado = consumo_mensal * 0.75

# Mostrando o resultado formatado na tela
print("\n" + "="*30)
print(f"Aparelho: {aparelho}")
print(f"Consumo estimado: {consumo_mensal:.2f} kWh/mês")
print(f"Custo mensal estimado: R$ {custo_estimado:.2f} (Tarifa: R$ 0,75/kWh)")

if consumo_mensal > 40:
    print("Aviso: Este aparelho tem um consumo considerado alto.")
else:
    print("Nota: Este aparelho tem um consumo considerado baixo/moderado.")

print("="*30)
