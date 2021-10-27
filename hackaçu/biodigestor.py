toneladas_cana = float(input('Digite quantas toneladas de cana as indústrias de Goytazes produziram esse mês'))
etanol = 70 * toneladas_cana #litros
vinhaça = 13 * etanol #litros
biogas = 14 * vinhaça #litros , pq 1 000 l vinhaça -> 14 000 biogas
kW_geradoIndustria = (6.5 / 1000) * biogas   # kw/h por litro de biogas
print(f"Ao todos as usinas geram mensalmente {kW_geradoIndustria} kWh de energia")

familias_beneficiadas = kW_geradoIndustria / 152.2 #pq o consumo medio brasileiro eh 152.2kw/h no mês

print(f"A insdustria consegue abastecer {familias_beneficiadas}familias no mês em média")

