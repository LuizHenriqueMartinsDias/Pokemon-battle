import random

class Battle:
    def __init__(self,trainer1,trainer2):
        self.attacker = trainer1
        self.defender = trainer2
    def start_battle(self):
        atk_pokemon = self.attacker.choose()
        def_pokemon = self.defender.choose()
        self.attack(atk_pokemon,def_pokemon)
    #def get_modifier(self,atkpokemon,defpokemon):
    #    if atkpokemon.type =

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

                dmg = self.calculate_dmg(atkpokemon, defpokemon, atk1)
                print(f"💥 {atkpokemon.name} usou {atk1.name} e causou {dmg} de dano!")
                defpokemon.hp -= dmg
                print(f"❤️ {defpokemon.name} agora tem {defpokemon.hp} HP")

                if not (defpokemon.hp <= 0):
                    dmg = self.calculate_dmg(defpokemon, atkpokemon, atk2,calc_type_multiplier)
                    print(f"\n💥 {defpokemon.name} contra-atacou com {atk2.name} causando {dmg}!")
                    atkpokemon.hp -= dmg
                    print(f"❤️ {atkpokemon.name} agora tem {atkpokemon.hp} HP")

                    self.attack(atkpokemon, defpokemon)
                else:
                    print(f"\n❌ {defpokemon.name} desmaiou!")
                    self.defender.team.remove(defpokemon)
                    self.attack(atkpokemon, self.defender.choose())

            else:
                print(f"\n⚡ {defpokemon.name} é mais rápido!\n")

                dmg = self.calculate_dmg(defpokemon, atkpokemon, atk2)
                print(f"💥 {defpokemon.name} usou {atk2.name} e causou {dmg} de dano!")
                atkpokemon.hp -= dmg
                print(f"❤️ {atkpokemon.name} agora tem {atkpokemon.hp} HP")

                if not (atkpokemon.hp <= 0):
                    dmg = self.calculate_dmg(atkpokemon, defpokemon, atk1)
                    print(f"\n💥 {atkpokemon.name} respondeu com {atk1.name} causando {dmg}!")
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
            A = dfder.sp_atk
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