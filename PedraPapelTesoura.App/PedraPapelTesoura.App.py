import random   
from enum import IntEnum

class Acoes(IntEnum):
    Pedra = 0
    Papel = 1
    Tesoura = 2

vitorias = {
    Acoes.Tesoura: [Acoes.Papel],
    Acoes.Papel: [Acoes.Pedra],
    Acoes.Pedra: [Acoes.Tesoura],
}

def get_selecao_usuario():
    escolhas = [f"{acao.name}[{acao.value}]" for acao in Acoes]
    escolhas_str = ", ".join(escolhas)
    selecao = int(input(f"Entre com uma opção ({escolhas_str}): "))
    acao = Acoes(selecao)
    return acao

def get_selecao_computador():
    selecao = random.randint(0, len(Acoes) - 1)
    acao = Acoes(selecao)
    return acao

def determinar_vencedor(acao_usuario, acao_computador):
    defeats = vitorias[acao_usuario]
    if acao_usuario == acao_computador:
        print(f"Os dois escolheram {acao_usuario.name}. Foi empate!")
    elif acao_computador in defeats:
        print(f"{acao_usuario.name} ganha {acao_computador.name}! Você Venceu!")
    else:
        print(f"{acao_computador.name} ganha {acao_usuario.name}! Você perdeu.")

while True:
    try:
        acao_usuario = get_selecao_usuario()
    except ValueError as e:
        range_str = f"[0, {len(Acoes) - 1}]"
        print(f"Seleção Inválida. Escolha dentro das opções  {range_str}")
        continue

    acao_computador = get_selecao_computador()
    determinar_vencedor(acao_usuario, acao_computador)

    novo_jogo = input("Jogar novamente? (s/n): ")
    if novo_jogo.lower() != "s":
        break