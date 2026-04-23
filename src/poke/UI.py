import random

from src.poke.battle import Trainer, Battle
from src.poke.storage import pokemon_list


class UserInterface:
    def choose_pokemon(self):
        team = []
        while len(team) < 3:
            print("Choose a pokemon")
            for i,pokemon in enumerate(pokemon_list):
                print(i,pokemon)
            option = int(input())
            team.append(pokemon_list[option])
            pokemon_list.pop(option)

        trainer = Trainer(team)
        for pokemon in trainer.team:
            print(pokemon.name)
        opponent = []

        while len(opponent) < 3:
            poke = random.choice(pokemon_list)
            pokemon_list.remove(poke)
            opponent.append(poke)
        defender = Trainer(opponent)
        for pokemon in defender.team:
            print(pokemon.name)
        pokemon = trainer.choose()

        battle = Battle(trainer,defender)
        battle.start_battle()
