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
    def attack(self,atkpokemon,defpokemon):
        for i,move in enumerate(atkpokemon.moves):
            print(i,move)
        option = int(input("choose move"))
        atk1 = atkpokemon.moves[option]
        atk2 = random.choice(defpokemon.moves)
        #modifier = get_modifier()
        if atkpokemon.speed > defpokemon.speed:
            damage = ((((2*atkpokemon.lvl/5)+2*atk1.power*atkpokemon.atk/defpokemon.def_)/50)+2)
            print(defpokemon.hp)
            print(damage)
            defpokemon.hp -= damage
            print(defpokemon.hp)
class Trainer:
    def __init__(self,team):
        self.team = team
    def choose(self):
        return random.choice(self.team)