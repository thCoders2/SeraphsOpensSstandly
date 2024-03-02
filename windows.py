import random
import time

class Entidade:
    def __init__(self, nome, vida, forca, defesa):
        self.nome = nome
        self.vida = vida
        self.vida_maxima = vida
        self.forca = forca
        self.defesa = defesa

    def atacar(self, alvo):
        dano = self.forca - alvo.defesa
        if dano > 0:
            alvo.vida -= dano
            print(f"{self.nome} atacou {alvo.nome} causando {dano} de dano!")
        else:
            print(f"{self.nome} atacou {alvo.nome}, mas não causou dano!")

    def esta_vivo(self):
        return self.vida > 0

class Personagem(Entidade):
    def __init__(self, nome, classe):
        super().__init__(nome, vida=100, forca=10, defesa=5)
        self.classe = classe
        self.experiencia = 0
        self.nivel = 1

    def ganhar_experiencia(self, experiencia):
        self.experiencia += experiencia
        if self.experiencia >= 10:
            self.nivel += 1
            self.vida_maxima += 10
            self.vida = self.vida_maxima
            self.forca += 2
            self.defesa += 1
            self.experiencia -= 10
            print(f"{self.nome} subiu para o nível {self.nivel}!")

    def exibir_status(self):
        print(f"{self.nome} ({self.classe}) - Nível: {self.nivel}, Vida: {self.vida}/{self.vida_maxima}, Força: {self.forca}, Defesa: {self.defesa}, Experiência: {self.experiencia}")

class Inimigo(Entidade):
    def __init__(self, nome, vida, forca, defesa):
        super().__init__(nome, vida, forca, defesa)

def batalhar(personagem, inimigo):
    print(f"Você encontrou um {inimigo.nome}!")
    while personagem.vida > 0 and inimigo.esta_vivo():
        personagem.atacar(inimigo)
        if inimigo.esta_vivo():
            inimigo.atacar(personagem)

    if personagem.vida > 0:
        experiencia_ganha = random.randint(5, 10)
        print(f"Você derrotou o {inimigo.nome} e ganhou {experiencia_ganha} pontos de experiência!")
        personagem.ganhar_experiencia(experiencia_ganha)

moedas_de_ouro = 20
def loja(personagem):
    print(f"Bem-vindo à loja! Você tem {moedas_de_ouro} moedas de ouro.")
    while True:
        print("1 - Poção de Cura (10 moedas de ouro)")
        print("2 - Voltar para a cidade")
        opcao = input("Escolha o que deseja comprar ou digite 'sair' para sair da loja: ")
        if opcao == '1':
            if moedas_de_ouro >= 10:
                moedas_de_ouro -= 10
                personagem.vida = personagem.vida_maxima
                print(f"{personagem.nome} comprou uma Poção de Cura e se curou completamente!")
            else:
                print("Você não tem moedas de ouro suficientes para comprar a Poção de Cura.")
        elif opcao == '2':
            break
        elif opcao.lower() == 'sair':
            break
        else:
            print("Opção inválida!")


print("Bem-vindo(a) ao RPGzinho!")
nome_personagem = input("Digite o nome do seu personagem: ")
print("Escolha a classe do seu personagem:")
print("1 - Guerreiro")
print("2 - Mago")
print("3 - Ladino")
classe_escolhida = input("Digite o número da classe desejada: ")

if classe_escolhida == '1':
    personagem = Personagem(nome_personagem, "Guerreiro")
elif classe_escolhida == '2':
    personagem = Personagem(nome_personagem, "Mago")
elif classe_escolhida == '3':
    personagem = Personagem(nome_personagem, "Ladino")
else:
    print("Opção inválida! Escolha novamente.")
    exit()

if classe_escolhida not in ['1', '2', '3']:
    print("Opção inválida! Escolha novamente.")
    exit()

print(f"Parabéns! Você criou um novo {personagem.classe} chamado {personagem.nome}!")

print(f"{personagem.nome} decide sair de sua cidade natal e explorar o mundo em busca de aventuras.")

print("...")

time.sleep(2)

print(f"{personagem.nome} entra na Floresta Proibida.")

print("...")

time.sleep(2)

# Primeiro inimigo
goblin = Inimigo("Goblin", vida=30, forca=8, defesa=3)
batalhar(personagem, goblin)

print(f"{personagem.nome} continua sua jornada e encontra uma trilha que o leva a uma montanha.")

print("...")

time.sleep(2)

# Segundo inimigo
lobo = Inimigo("Lobo", vida=25, forca=10, defesa=2)
batalhar(personagem, lobo)

print(f"{personagem.nome} sobreviveu às batalhas e decide retornar ao Vilarejo Inicial para descansar e se curar.")

print("...")

time.sleep(2)

# Loja
loja(personagem)

print(f"{personagem.nome} descansa na estalagem do Vilarejo Inicial e se prepara para novas aventuras.")

print("Fim da primeira jornada. O que será que o aguarda na próxima jornada?")

