# Desafio de Código 03: Estruturas de Dados e Objetos - Escrevendo as Classes de um Jogo.
# Bootcamp Potência Tech iFood - Programação do Zero

class Heroi:
    def __init__(self, nome, idade, tipo):
        self.nome = nome
        self.idade = idade
        self.tipo = tipo

    def atacar(self):
        if self.tipo == "mago":
            ataque = "usou magia"
        elif self.tipo == "guerreiro":
            ataque = "usou espada"
        elif self.tipo == "monge":
            ataque = "usou artes marciais"
        elif self.tipo == "ninja":
            ataque = "usou shuriken"
        else:
            ataque = "usou um ataque genérico"

        mensagem = f"O {self.tipo} atacou usando {ataque}"
        print(mensagem)

heroi1 = Heroi("Gandalf", 75, "mago")
heroi2 = Heroi("Aragorn", 35, "guerreiro")

heroi1.atacar()
heroi2.atacar()
