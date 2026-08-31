import random
from dataclasses import dataclass, field

from src.poke.storage import TYPE_CHART


@dataclass
class AttackStepResult:
    attacker_name: str
    move_name: str
    damage: int | None
    effectiveness_message: str
    defender_new_hp: int
    defender_fainted: bool


@dataclass
class TurnResult:
    steps: list[AttackStepResult] = field(default_factory=list)
    battle_over: bool = False
    winner: "Trainer | None" = None


class Battle:
    def __init__(self, trainer1, trainer2, on_message=None, on_faint=None, on_battle_end=None):
        self.attacker = trainer1
        self.defender = trainer2
        self.atk_pokemon = None
        self.def_pokemon = None
        self.on_message = on_message or (lambda msg: None)
        self.on_faint = on_faint or (lambda pokemon: None)
        self.on_battle_end = on_battle_end or (lambda winner: None)

    def begin_battle(self):
        self.atk_pokemon = self.attacker.choose()
        self.def_pokemon = self.defender.choose()

    def get_active_moves(self):
        return self.atk_pokemon.moves

    def resolve_turn(self, move_index):
        """Resolves one full turn (both sides' attacks, in speed order) and
        returns a TurnResult. Raises IndexError for an out-of-range move_index."""
        atkpokemon = self.atk_pokemon
        defpokemon = self.def_pokemon

        atk1 = atkpokemon.moves[move_index]
        atk2 = random.choice(defpokemon.moves)

        if atkpokemon.speed > defpokemon.speed:
            self.on_message(f"\n⚡ {atkpokemon.name} é mais rápido!\n")
            order = [(atkpokemon, defpokemon, atk1), (defpokemon, atkpokemon, atk2)]
        else:
            self.on_message(f"\n⚡ {defpokemon.name} é mais rápido!\n")
            order = [(defpokemon, atkpokemon, atk2), (atkpokemon, defpokemon, atk1)]

        steps = []
        for atker, dfder, move in order:
            step = self._execute_single_attack(atker, dfder, move)
            steps.append(step)
            if step.defender_fainted:
                break

        return self._resolve_faints(steps)

    def _execute_single_attack(self, atker, dfder, move):
        effect_message = move.apply_effect(atker, dfder)
        if effect_message:
            self.on_message(effect_message)

        type_multiplier = self.get_type_multiplier(move.move_type, dfder.poke_types)
        dmg = self.calculate_dmg(atker, dfder, move, type_multiplier)
        effectiveness_message = self.get_type_message(type_multiplier)

        if dmg is not None:
            self.on_message(f"💥 {atker.name} usou {move.name} e causou {dmg} de dano!")
            if effectiveness_message:
                self.on_message(effectiveness_message)
            dfder.hp -= dmg
            self.on_message(f"❤️ {dfder.name} agora tem {dfder.hp} HP")

        return AttackStepResult(
            attacker_name=atker.name,
            move_name=move.name,
            damage=dmg,
            effectiveness_message=effectiveness_message,
            defender_new_hp=dfder.hp,
            defender_fainted=dfder.hp <= 0,
        )

    def _resolve_faints(self, steps):
        battle_over = False
        winner = None

        if self.atk_pokemon.hp <= 0:
            self.on_message(f"\n❌ {self.atk_pokemon.name} desmaiou!")
            self.on_faint(self.atk_pokemon)
            self.attacker.team.remove(self.atk_pokemon)
            if not self.attacker.team:
                battle_over = True
                winner = self.defender
            else:
                self.atk_pokemon = self.attacker.choose()

        if not battle_over and self.def_pokemon.hp <= 0:
            self.on_message(f"\n❌ {self.def_pokemon.name} desmaiou!")
            self.on_faint(self.def_pokemon)
            self.defender.team.remove(self.def_pokemon)
            if not self.defender.team:
                battle_over = True
                winner = self.attacker
            else:
                self.def_pokemon = self.defender.choose()

        if battle_over:
            self.on_battle_end(winner)

        return TurnResult(steps=steps, battle_over=battle_over, winner=winner)

    def start_battle(self):
        self.begin_battle()
        self.attack(self.atk_pokemon, self.def_pokemon)

    def attack(self, atkpokemon=None, defpokemon=None):
        """Legacy terminal entry point. Thin wrapper around resolve_turn()/
        begin_battle() that drives a blocking input() loop and prints every
        message, kept so the terminal game (src/main.py) behaves exactly as
        before while sharing the same rules engine as the GUI."""
        if atkpokemon is not None:
            self.atk_pokemon = atkpokemon
        if defpokemon is not None:
            self.def_pokemon = defpokemon
        self.on_message = print

        while True:
            print("\n" + "=" * 40)
            print(f"⚔️  {self.atk_pokemon.name}  VS  {self.def_pokemon.name}")
            print("=" * 40)
            print(f"❤️ {self.atk_pokemon.name}: {self.atk_pokemon.hp} HP")
            print(f"❤️ {self.def_pokemon.name}: {self.def_pokemon.hp} HP\n")

            print("📜 Escolha um golpe:")
            for i, move in enumerate(self.get_active_moves()):
                print(f"{i} - {move.name} ({move.category})")

            try:
                option = int(input("👉 > "))
                result = self.resolve_turn(option)
            except IndexError:
                print("⚠️ Golpe inválido, tente novamente.")
                continue
            except ValueError:
                print("⚠️ Entrada inválida, tente novamente.")
                continue

            if result.battle_over:
                print("ATACANTE GANHOU" if result.winner is self.attacker else "DEFENSOR GANHOU")
                return

    def get_type_message(self, multiplier):
        if multiplier == 0:
            return "It doesn't affect..."
        elif multiplier >= 2:
            return "It's super effective!"
        elif multiplier < 1:
            return "It's not very effective..."
        return ""

    def get_type_multiplier(self, move_type, def_types):
        multiplier = 1

        if isinstance(def_types, str):
            multiplier *= TYPE_CHART.get(move_type, {}).get(def_types, 1)
            return multiplier

        for poke_type in def_types:
            multiplier *= TYPE_CHART.get(move_type, {}).get(poke_type, 1)

        return multiplier

    def get_stage_multiplier(self, stage):
        if stage >= 0:
            return (2 + stage) / 2
        return 2 / (2 - stage)

    def calculate_dmg(self, atker, dfder, move, type_multiplier=1.0):
        if move.power == 0 or move.category == "status":
            return None

        if move.category == "physical":
            A = atker.atk * self.get_stage_multiplier(atker.atk_stage)
            D = dfder.def_ * self.get_stage_multiplier(dfder.def_stage)
        else:
            A = atker.sp_atk * self.get_stage_multiplier(atker.sp_atk_stage)
            D = dfder.sp_def * self.get_stage_multiplier(dfder.sp_def_stage)

        damage = (((2 * atker.lvl / 5 + 2) * move.power * A / D) / 50) + 2

        stab = 1.0
        if move.move_type in atker.poke_types:
            stab = 1.5

        critical = 1.5 if random.random() < 0.1 else 1.0
        random_factor = random.uniform(0.85, 1.0)

        modifier = stab * type_multiplier * critical * random_factor

        return int(damage * modifier)


class Trainer:
    def __init__(self, team):
        self.team = team

    def choose(self):
        return random.choice(self.team)
