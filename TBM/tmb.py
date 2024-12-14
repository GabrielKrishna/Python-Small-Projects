# Fórmula da TMB para homens: TMB = 13,75 * peso(kg) + 5 * altura(cm) - 6,75 * idade + 66,5

# O gasto energético total é calculado multiplicando a TMB pelo fator de atividade física.

# Como o usuário pratica atividades físicas regularmente, utilizaremos um fator de 1.6 (moderadamente ativo).

peso = 78  # kg
altura = 170  # cm
idade = 21  # anos
fator_atividade = 1.6  # Moderadamente ativo

# Calculando a TMB
tmb = 13.75 * peso + 5 * altura - 6.75 * idade + 66.5

# Calculando o gasto energético total
gasto_energetico_total = tmb * fator_atividade


# Cálculo dos macronutrientes com base na proporção recomendada de calorias totais

# Proteínas: 2 g/kg
proteinas_por_kg = 2
proteinas = proteinas_por_kg * peso  # em gramas

# Calorias diárias recomendadas de proteínas (1g de proteína = 4 kcal)
calorias_proteinas = proteinas * 4


# Lipídeos: 1 g/kg
lipideos_por_kg = 1
lipideos = lipideos_por_kg * peso  # em gramas

# Calorias diárias recomendadas de lipídeos (1g de proteína = 9 kcal)
calorias_lipideos = lipideos * 9


# Calorias carboidratos:

calorias_carboidratos = gasto_energetico_total - calorias_proteinas - calorias_lipideos

# Carboidratos:

carboidratos = calorias_carboidratos / 4


print("Taxa metabólica basal:", tmb)
print("Gasto energético total:", gasto_energetico_total)


print("Gramas de proteínas:", proteinas)
print("Calorias das proteínas:", calorias_proteinas)

print("Gramas de lipídeos:", lipideos)
print("Calorias de lipídeos:", calorias_lipideos)

print("Gramas de carboidratos:", carboidratos)
print("Calorias de carboidratos:", calorias_carboidratos)