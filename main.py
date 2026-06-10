"""
# EXERCÍCIO — CÁLCULO DE SALÁRIO COM IMPOSTO

# Crie um programa em Python que calcule o valor do imposto
# e o salário final de uma pessoa após o desconto.

# O programa deve funcionar em duas etapas:

# 1) Primeiro, crie variáveis no código para:
#    - salário
#    - taxa de imposto
#    Depois calcule:
#    - valor do imposto
#    - salário final após desconto
#    Mostre todos os valores na tela.

# 2) Em seguida, peça ao usuário que digite:
#    - seu salário
#    - a taxa de imposto

# Lembre-se que o input() retorna texto,
# então você deve converter os valores para número.
# Depois calcule novamente:
#    - valor do imposto
#    - salário final

# Por fim, mostre os resultados formatados na tela.
"""
# ==========================================
# ETAPA 1: Variáveis fixas no código
# ==========================================

salario = 2200.0
taxa_de_imposto = 12.0

# Cálculos
valor_do_imposto = salario * (taxa_de_imposto / 100)
salario_final = salario - valor_do_imposto

print("--- RESULTADOS DA ETAPA 1 ---")
print("Salario original: ", salario)
print("Taxa de imposto: ", taxa_de_imposto)
print("Valor do imposto descontado: ", valor_do_imposto)
print("Salario final: ", salario_final)

# ==========================================
# ETAPA 2: Entrada de dados do usuário
# ==========================================

salario_usuario = float(input("Digite o seu salario: "))
taxa_usuario = float(input("Digite a taxa de imposto (ex: 10 para 10%): "))

imposto_usuario = salario_usuario * (taxa_usuario / 100)
salario_final_usuario = salario_usuario - imposto_usuario

print("--- RESULTADOS DA ETAPA 2 ---")
print("Seu salario: R$", salario_usuario)
print("Sua taxa:", taxa_usuario, "%")
print("Imposto a pagar: R$", imposto_usuario)
print("Salario liquido final: R$", salario_final_usuario)

