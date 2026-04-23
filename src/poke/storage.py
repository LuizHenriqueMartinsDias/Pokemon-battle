import random

from src.poke.pokemon import Pokemon,Move
class Stats:
    def __init__(self,base_hp,base_speed,base_atk,base_def,base_sp_atk,base_sp_def):
        self.base_hp = base_hp
        self.base_speed = base_speed
        self.base_atk = base_atk
        self.base_def = base_def
        self.base_sp_atk = base_sp_atk
        self.base_sp_def = base_sp_def

        self.iv_hp = random.randint(0,31)
        self.iv_speed = random.randint(0,31)
        self.iv_atk = random.randint(0,31)
        self.iv_def = random.randint(0,31)
        self.iv_sp_atk = random.randint(0,31)
        self.iv_sp_def = random.randint(0,31)

        self.ev_hp = random.randint(0,31)
        self.ev_speed = random.randint(0,31)
        self.ev_atk = random.randint(0,31)
        self.ev_def = random.randint(0,31)
        self.ev_sp_atk = random.randint(0,31)
        self.ev_sp_def = random.randint(0,31)


    def calc_hp(self, lvl: int):
        return int((((2 * self.base_hp + self.iv_hp + (self.ev_hp // 4)) * lvl) / 100) + lvl + 10)

    def calc_atk(self, lvl: int):
        return int((((2 * self.base_atk + self.iv_atk + (self.ev_atk // 4)) * lvl) / 100) + 5)

    def calc_def(self, lvl: int):
        return int((((2 * self.base_def + self.iv_def + (self.ev_def // 4)) * lvl) / 100) + 5)

    def calc_sp_atk(self, lvl: int):
        return int((((2 * self.base_sp_atk + self.iv_sp_atk + (self.ev_sp_atk // 4)) * lvl) / 100) + 5)

    def calc_sp_def(self, lvl: int):
        return int((((2 * self.base_sp_def + self.iv_sp_def + (self.ev_sp_def // 4)) * lvl) / 100) + 5)

    def calc_speed(self, lvl: int):
        return int((((2 * self.base_speed + self.iv_speed + (self.ev_speed // 4)) * lvl) / 100) + 5)

# MOVES
# Electric
thunderbolt = Move("Thunderbolt", "Electric", "special", 90, 100)
spark = Move("Spark", "Electric", "physical", 65, 100)

# Normal
quick_attack = Move("Quick Attack", "Normal", "physical", 40, 100)
slash = Move("Slash", "Normal", "physical", 70, 100)
strength = Move("Strength", "Normal", "physical", 80, 100)

# Steel
iron_tail = Move("Iron Tail", "Steel", "physical", 100, 75)
metal_claw = Move("Metal Claw", "Steel", "physical", 50, 95)

# Fire
flamethrower = Move("Flamethrower", "Fire", "special", 90, 100)
fire_blast = Move("Fire Blast", "Fire", "special", 110, 85)

# Flying
wing_attack = Move("Wing Attack", "Flying", "physical", 60, 100)
aerial_ace = Move("Aerial Ace", "Flying", "physical", 60, 100)

# Water
surf = Move("Surf", "Water", "special", 90, 100)
hydro_pump = Move("Hydro Pump", "Water", "special", 110, 80)

# Ice
ice_beam = Move("Ice Beam", "Ice", "special", 90, 100)

# Dark
bite = Move("Bite", "Dark", "physical", 60, 100)
dark_pulse = Move("Dark Pulse", "Dark", "special", 80, 100)
crunch = Move("Crunch", "Dark", "physical", 80, 100)

# Grass
energy_ball = Move("Energy Ball", "Grass", "special", 90, 100)
razor_leaf = Move("Razor Leaf", "Grass", "physical", 55, 95)
vine_whip = Move("Vine Whip", "Grass", "physical", 45, 100)
solar_beam = Move("Solar Beam", "Grass", "special", 120, 100)

# Psychic
psychic = Move("Psychic", "Psychic", "special", 90, 100)
psybeam = Move("Psybeam", "Psychic", "special", 65, 100)

# Ghost
shadow_ball = Move("Shadow Ball", "Ghost", "special", 80, 100)

# Fairy
dazzling_gleam = Move("Dazzling Gleam", "Fairy", "special", 80, 100)
moonblast = Move("Moonblast", "Fairy", "special", 95, 100)
play_rough = Move("Play Rough", "Fairy", "physical", 90, 90)

# Ground
earthquake = Move("Earthquake", "Ground", "physical", 100, 100)
dig = Move("Dig", "Ground", "physical", 80, 100)

# Dragon
dragon_claw = Move("Dragon Claw", "Dragon", "physical", 80, 100)

# Rock
rock_slide = Move("Rock Slide", "Rock", "physical", 75, 90)

# Fighting
close_combat = Move("Close Combat", "Fighting", "physical", 120, 100)
brick_break = Move("Brick Break", "Fighting", "physical", 75, 100)

#Pokemons
pikachu = Pokemon(
    Stats(35, 55, 40, 50, 50, 90),
    "Pikachu",
    [thunderbolt, quick_attack, iron_tail, spark],
    "Electric",
    50
)

charizard = Pokemon(
    Stats(78, 84, 78, 109, 85, 100),
    "Charizard",
    [flamethrower, fire_blast, slash, wing_attack],
    "Fire/Flying",
    50
)

blastoise = Pokemon(
    Stats(79, 83, 100, 85, 105, 78),
    "Blastoise",
    [surf, hydro_pump, ice_beam, bite],
    "Water",
    50
)

venusaur = Pokemon(
    Stats(80, 82, 83, 100, 100, 80),
    "Venusaur",
    [energy_ball, razor_leaf, vine_whip, solar_beam],
    "Grass/Poison",
    50
)

alakazam = Pokemon(
    Stats(55, 50, 45, 135, 95, 120),
    "Alakazam",
    [psychic, psybeam, shadow_ball, dazzling_gleam],
    "Psychic",
    50
)

garchomp = Pokemon(
    Stats(108, 130, 95, 80, 85, 102),
    "Garchomp",
    [earthquake, dragon_claw, rock_slide, dig],
    "Dragon/Ground",
    50
)

pidgeot = Pokemon(
    Stats(83, 80, 75, 70, 70, 101),
    "Pidgeot",
    [wing_attack, slash, quick_attack, aerial_ace],
    "Normal/Flying",
    50
)

umbreon = Pokemon(
    Stats(95, 65, 110, 60, 130, 65),
    "Umbreon",
    [bite, dark_pulse, crunch, quick_attack],
    "Dark",
    50
)

gardevoir = Pokemon(
    Stats(68, 65, 65, 125, 115, 80),
    "Gardevoir",
    [psychic, moonblast, dazzling_gleam, shadow_ball],
    "Psychic/Fairy",
    50
)

lucario = Pokemon(
    Stats(70, 110, 70, 115, 70, 90),
    "Lucario",
    [close_combat, brick_break, metal_claw, dragon_claw],
    "Fighting/Steel",
    50
)

machamp = Pokemon(
    Stats(90, 130, 80, 65, 85, 55),
    "Machamp",
    [close_combat, brick_break, strength, rock_slide],
    "Fighting",
    50
)

sylveon = Pokemon(
    Stats(95, 65, 65, 110, 130, 60),
    "Sylveon",
    [moonblast, dazzling_gleam, play_rough, quick_attack],
    "Fairy",
    50
)

pokemon_list = [
    pikachu,
    charizard,
    blastoise,
    venusaur,
    alakazam,
    garchomp,
    pidgeot,
    umbreon,
    gardevoir,
    lucario,
    machamp,
    sylveon
]