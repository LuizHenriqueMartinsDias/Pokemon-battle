
import random

from src.poke.battle import Trainer, Battle
from src.poke.storage import pokemon_list


class UserInterface:
    def choose_pokemon(self):
        print("\n" + "="*50)
        print("🎮 WELCOME TO POKÉMON BATTLE SIMULATOR")
        print("="*50 + "\n")

        team = []

        while len(team) < 3:
            print("\n📜 Choose your Pokémon:")
            print("-"*40)

            for i, pokemon in enumerate(pokemon_list):
                print(f"{i} - {pokemon.name}")

            option = int(input("\n👉 Select a Pokémon: "))
            chosen = pokemon_list[option]

            print(f"\n✅ You chose {chosen.name}!")
            team.append(chosen)
            pokemon_list.pop(option)

            print(f"📦 Team size: {len(team)}/3")

        trainer = Trainer(team)

        print("\n" + "="*50)
        print("🧑 Your Team")
        print("="*50)
        for pokemon in trainer.team:
            print(f"• {pokemon.name}")

        opponent = []

        print("\n🎲 Generating opponent team...\n")

        while len(opponent) < 3:
            poke = random.choice(pokemon_list)
            pokemon_list.remove(poke)
            opponent.append(poke)

        defender = Trainer(opponent)

        print("="*50)
        print("🤖 Opponent Team")
        print("="*50)
        for pokemon in defender.team:
            print(f"• {pokemon.name}")

        print("\n⚔️ Battle is about to start!")
        print("="*50 + "\n")

        battle = Battle(trainer, defender)
        battle.start_battle()
