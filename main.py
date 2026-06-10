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

salario = 3000.0
taxa_imposto = 15.0
valor_imposto = salario * (taxa_imposto / 100)
salario_final = salario - valor_imposto
print(f"Salário Final: R$ {salario_final}")
salario_usuario = float(input("Digite o seu salário: "))
taxa_usuario = float(input("Digite a taxa de imposto (ex: 15): "))

valor_imposto_usuario = salario_usuario * (taxa_usuario / 100)
salario_final_usuario = salario_usuario - valor_imposto_usuario

print(f"Seu Salário Final será: R$ {salario_final_usuario:.2f}")
