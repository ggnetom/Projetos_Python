from pokemon import *
from pessoa import *


def escolher_pokeom_inicial(player):
    print(" Olá {}!\n Qual pokemon irá te acompanhar nessa jornada!".format(player))

    pokemon1 = PokemonFogo("Charmander", level=1)
    pokemon2 = PokemonPlanta("Bulbassauro", level=1)
    pokemon3 = PokemonAgua("Squirtle", level=1)

    print("1 -", pokemon1)
    print("2 -", pokemon2)
    print("3 -", pokemon3)

    while True:
        escolha = input("Escolha um: ")

        if escolha == "1":
            player.capturar(pokemon1)
            break
        elif escolha == "2":
            player.capturar(pokemon2)
            break
        elif escolha == "3":
            player.capturar(pokemon3)
            break
        else:
            print("Escolha invalida")


player = Player("geraldino")

player.mostrar_gold()

player.capturar(PokemonFogo("Charmander", level=60))



inimigo1 = Inimigo()

player.batalhar(inimigo1)
