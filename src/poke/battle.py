import random

from src.poke.storage import TYPE_CHART


class Battle:
    def __init__(self,trainer1,trainer2):
        self.attacker = trainer1
        self.defender = trainer2
    def start_battle(self):
        atk_pokemon = self.attacker.choose()
        def_pokemon = self.defender.choose()
        self.attack(atk_pokemon,def_pokemon)

    def get_type_message(self,multiplier):
        if multiplier == 0:
            return "It doesn't affect..."
        elif multiplier >= 2:
            return "It's super effective!"
        elif multiplier < 1:
            return "It's not very effective..."
        return ""

    def get_type_multiplier(self,move_type,def_types):
        multiplier = 1
        for poke_type in def_types:
            multiplier *= TYPE_CHART.get(move_type, {}).get(poke_type, 1)
        return multiplier
    def attack(self, atkpokemon, defpokemon):
        try:
            if atkpokemon.hp <= 0:
                print(f"\n❌ {atkpokemon.name} desmaiou!")
                self.attacker.team.remove(atkpokemon)
                self.attack(self.attacker.choose(), defpokemon)
                return

            if defpokemon.hp <= 0:
                print(f"\n❌ {defpokemon.name} desmaiou!")
                self.defender.team.remove(defpokemon)
                self.attack(atkpokemon, self.defender.choose())
                return

            print("\n" + "=" * 40)
            print(f"⚔️  {atkpokemon.name}  VS  {defpokemon.name}")
            print("=" * 40)

            print(f"❤️ {atkpokemon.name}: {atkpokemon.hp} HP")
            print(f"❤️ {defpokemon.name}: {defpokemon.hp} HP\n")

            print("📜 Escolha um golpe:")
            for i, move in enumerate(atkpokemon.moves):
                print(f"{i} - {move.name} ({move.category})")

            option = int(input("👉 > "))
            atk1 = atkpokemon.moves[option]
            atk2 = random.choice(defpokemon.moves)

            print(f"\n🔥 {atkpokemon.name} escolheu {atk1.name}!")
            print(f"🎲 {defpokemon.name} escolheu {atk2.name}!")

            if atkpokemon.speed > defpokemon.speed:
                print(f"\n⚡ {atkpokemon.name} é mais rápido!\n")

                dmg = self.calculate_dmg(atkpokemon, defpokemon, atk1,self.get_type_multiplier(atk1.move_type,defpokemon.poke_types))
                message = self.get_type_message(self.get_type_multiplier(atk1.move_type,defpokemon.poke_types))

                print(f"💥 {atkpokemon.name} usou {atk1.name} e causou {dmg} de dano!")
                if message:
                    print(message)
                defpokemon.hp -= dmg
                print(f"❤️ {defpokemon.name} agora tem {defpokemon.hp} HP")

                if not (defpokemon.hp <= 0):
                    dmg = self.calculate_dmg(defpokemon, atkpokemon, atk2,self.get_type_multiplier(atk2.move_type,atkpokemon.poke_types))
                    message = self.get_type_message(self.get_type_multiplier(atk2.move_type, atkpokemon.poke_types))
                    print(f"\n💥 {defpokemon.name} contra-atacou com {atk2.name} causando {dmg}!")
                    if message:
                        print(message)
                    atkpokemon.hp -= dmg
                    print(f"❤️ {atkpokemon.name} agora tem {atkpokemon.hp} HP")

                    self.attack(atkpokemon, defpokemon)
                else:
                    print(f"\n❌ {defpokemon.name} desmaiou!")
                    self.defender.team.remove(defpokemon)
                    self.attack(atkpokemon, self.defender.choose())

            else:
                print(f"\n⚡ {defpokemon.name} é mais rápido!\n")

                dmg = self.calculate_dmg(defpokemon, atkpokemon, atk2,self.get_type_multiplier(atk2.move_type,atkpokemon.poke_types))
                message = self.get_type_message(self.get_type_multiplier(atk2.move_type, atkpokemon.poke_types))

                print(f"💥 {defpokemon.name} usou {atk2.name} e causou {dmg} de dano!")
                if message:
                    print(message)
                atkpokemon.hp -= dmg
                print(f"❤️ {atkpokemon.name} agora tem {atkpokemon.hp} HP")

                if not (atkpokemon.hp <= 0):
                    dmg = self.calculate_dmg(atkpokemon, defpokemon, atk1,self.get_type_multiplier(atk1.move_type,defpokemon.poke_types))
                    message = self.get_type_message(self.get_type_multiplier(atk1.move_type, defpokemon.poke_types))

                    print(f"\n💥 {atkpokemon.name} respondeu com {atk1.name} causando {dmg}!")
                    if message:
                        print(message)
                    defpokemon.hp -= dmg
                    print(f"❤️ {defpokemon.name} agora tem {defpokemon.hp} HP")

                    self.attack(atkpokemon, defpokemon)
                else:
                    print(f"\n❌ {atkpokemon.name} desmaiou!")
                    self.attacker.team.remove(atkpokemon)
                    self.attack(self.attacker.choose(), defpokemon)
        except IndexError:
            if len(self.attacker.team) == 0:
                print("DEFENSOR GANHOU")
            else:
                print("ATACANTE GANHOU")

    def calculate_dmg(self,atker,dfder,move,type_multiplier=1.0):

        if move.category == "physical":
            A = atker.atk
            D = dfder.def_
        else:
            A =atker.sp_atk
            D =dfder.sp_def

        damage = (((2 * atker.lvl / 5 + 2) * move.power * A / D) / 50) + 2
        stab = 1.0
        if move.move_type in atker.poke_types:
            stab = 1.5
        critical = 1.5 if random.random() < 0.1 else 1.0


        random_factor = random.uniform(0.85, 1.0)

        modifier = stab * type_multiplier * critical * random_factor
        return int(damage * modifier)

class Trainer:
    def __init__(self,team):
        self.team = team
    def choose(self):
        return random.choice(self.team)