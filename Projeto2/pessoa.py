import random

from pokemon import *


Nomes = ["Brock", "Misty", "Lt. Surge", "Erika", "Koga", "Sabrina", "Blaine",
    "Giovanni", "Jessie", "James", "Lorelei", "Bruno", "Agatha", "Lance", "Blue"]


Pokemons = [PokemonFogo("Charmander"), PokemonFogo("Vulpix"), PokemonFogo("Growlithe"), PokemonAgua("Squirtle"),
    PokemonAgua("Psyduck"), PokemonAgua("Staryu"), PokemonPlanta("Bulbasaur"), PokemonPlanta("Oddish"), PokemonPlanta("Bellsprout")]


class Pessoa:

    def __init__(self, nome=None, pokemons=[], gold=100):
        if nome:
            self.nome = nome
        else:
            self.nome = random.choice(Nomes)

        self.pokemons = pokemons
        self.gold = gold

    def __str__(self):
        return self.nome

    def mostrar_pokemons(self):
        if self.pokemons:
            print("Pokemons de {}".format(self))
            for index, pekemon in enumerate(self.pokemons):
                print("{} - {}".format(index, pekemon))
        else:
            print("{} ainda não tem pokemons!".format(self))

    def batalhar(self, pessoa):
        print("{} iniciou uma batalha com {}".format(self, pessoa))
        pessoa.mostrar_pokemons()
        pokemon_inimigo = pessoa.escolher_pokemon_aleatorio_batalha()
        pokemon = self.escolher_pokemon_batalha()
        if pokemon and pokemon_inimigo:
            while True:

                vitoria = pokemon.atacar(pokemon_inimigo)
                if vitoria:
                    print('{} ganhou a batalha'.format(self))
                    break

                vitoria_inimiga = pokemon_inimigo.atacar(pokemon)
                if vitoria_inimiga:
                    print('{} ganhou a batalha'.format(pessoa))
                    break
        else:
            print("Essa batalha não ocorreu!")
    
    def mostrar_gold(self):
        print('Você possui {} de gold'.format(self.gold))

    def ganhar_gold(self, quantidade):
        self.gold += quantidade
        print('Você ganhou {} gold'.format(quantidade))
        mostrar_gold()
            

class Player(Pessoa):
    tipo = "Player"

    def capturar(self, pokemon):
        self.pokemons.append(pokemon)
        print("{}, capturou o pokeomon {}!".format(self, pokemon))

    def escolher_pokemon_batalha(self):
        self.mostrar_pokemons()
        
        if self.pokemons:
            while True:
                escolha = input("Escolha o seu Pokemon: ")
                try:
                    escolha = int(escolha)
                    pokemon_escolhido_batalha = self.pokemons[escolha]
                    return pokemon_escolhido_batalha
                except:
                    print("Escolha invalida")
        else:
            print("Esse jogador não possui nenhum pokemon para a batalha")


class Inimigo(Pessoa):
    tipo = "Inimigo"

    def __init__(self, nome=None, pokemons=[]):
        if not pokemons:
            for i in range(random.randint(1, 3)):
                pokemons.append(random.choice(Pokemons))

        super().__init__ (nome=None, pokemons=pokemons)
    
    def escolher_pokemon_aleatorio_batalha(self):
        if self.pokemons:
            pokemon_escolhido = random.choice(self.pokemons)
            print("{} escolheu {}".format(self, pokemon_escolhido))
            return pokemon_escolhido
        else:
            print("{} não possui nenhum pokemon para a batalha".format(self))


def explorar(self):
    if random.random() <= 0.3:
        pokemon = random.choice(Pokemons)
        print('Um pokemon selvagem apareceu: {}'.format(pokemon))
    else:
        print('Nenhum pokemon encontrado')
