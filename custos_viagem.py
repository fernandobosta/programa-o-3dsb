class Veiculo:
    def __init__(self, modelo, consumo_km_litro, preco_combustivel):
        self.modelo = modelo
        self.consumo_km_litro = consumo_km_litro
        self.preco_combustivel = preco_combustivel

    def calcular_custo_viagem(self, distancia):
        litros_necessarios = distancia / self.consumo_km_litro
        return litros_necessarios * self.preco_combustivel

def calcular_custo_total_frota(lista_veiculos, distancia=200):
    custo_total = 0
    for veiculo in lista_veiculos:
        custo_total += veiculo.calcular_custo_viagem(distancia)
    return custo_total

# Exemplo de uso:
veiculos = [
    Veiculo("Carro A", 10, 5.80), # 10km/l, R$5.80/l
    Veiculo("Carro B", 15, 5.80), # 15km/l, R$5.80/l
    Veiculo("Moto", 35, 5.80)     # 35km/l, R$5.80/l
]

total = calcular_custo_total_frota(veiculos)
print(f"O custo total para a viagem de 200 km é: R$ {total:.2f}")
