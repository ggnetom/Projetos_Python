import random

class Pokemon:

    def __init__(self, especie, level=None, nome=None):
        self.especie = especie

        if level:
            self.level = level

        else:
            self.level = random.randint(1, 50)

        if nome:
            self.nome = nome

        else:
            self.nome = especie

        self.ataque = self.level * 2
        self.vida = self.level * 5 


    def __str__(self):
        return "{}({})".format(self.nome, self.level)


    def atacar(self, pokemon):
        ataque_efetivo = int((self.ataque * random.random() * 1.3))
        pokemon.vida -= ataque_efetivo

        print("{} perdeu {} pontos de vida".format(pokemon, ataque_efetivo))
        print('{} - {} pontos de vida'.format(pokemon, pokemon.vida))
        if pokemon.vida <= 0:
            print('{} foi derrotado'.format(pokemon))
            return True
    
        else:
            return False


class PokemonFogo(Pokemon):
    tipo = "Fogo"

    def atacar(self, pokemon):
        print('{} lançou chamuscar em {}'.format(self, pokemon))
        return super().atacar(pokemon)


class PokemonEletrico(Pokemon):
    tipo = "Eletrico"

class PokemonPlanta(Pokemon):
    tipo = "Planta"

class PokemonAgua(Pokemon):
    tipo = "Agua"



# class Bulbassauro(PokemonGrama):
#     especie = "Bulbassauro"

# class Charmander(PokemonFogo):
#     especie = "Charmander"

#     def atacar(self, pokemon):
#         pritn("{}, lançou chama em {}".format(self, pokemon))

