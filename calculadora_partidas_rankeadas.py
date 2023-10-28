# Desafio de Código 02: Trabalhando com Funções - Calculadora de Partidas Rankeadas
# Bootcamp Potência Tech iFood - Programação do Zero

def calcular_nivel(vitorias, derrotas):
    saldoVitorias = vitorias - derrotas

    if vitorias < 10:
        nivel = "Ferro"
    elif 10 <= vitorias <= 20:
        nivel = "Bronze"
    elif 21 <= vitorias <= 50:
        nivel = "Prata"
    elif 51 <= vitorias <= 80:
        nivel = "Ouro"
    elif 81 <= vitorias <= 90:
        nivel = "Diamante"
    elif 91 <= vitorias <= 100:
        nivel = "Lendário"
    else:
        nivel = "Imortal"

    return saldoVitorias, nivel

vitorias = int(input("Digite a quantidade de vitórias: "))
derrotas = int(input("Digite a quantidade de derrotas: "))

saldo, nivel = calcular_nivel(vitorias, derrotas)

print(f"O Herói tem um saldo de {saldo} está no nível de {nivel}")
