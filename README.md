
# ⚔️ Pokémon Battle Simulator (Python)

A turn-based Pokémon battle simulator built in Python, featuring core battle mechanics such as stat calculation, move categories, and type effectiveness.

---

## 🚀 Features

- 🔢 **Stat System**
  - Base stats, IVs, and EVs
  - Automatic stat calculation based on level

- ⚔️ **Battle System**
  - Turn-based combat
  - Speed determines attack order
  - Recursive battle flow

- 🧠 **Move Mechanics**
  - Physical vs Special moves
  - Power and accuracy system
  - Random opponent move selection

- 🌍 **Type Effectiveness**
  - Full type chart implementation
  - Supports dual-type Pokémon
  - Super effective / not effective / immunity

- 👥 **Trainer System**
  - Player selects a team of 3 Pokémon
  - Opponent team generated randomly

---

## 🏗️ Project Structure

```bash
src/
│
├── poke/
│   ├── pokemon.py     # Pokemon, Stats and Move classes
│   ├── battle.py      # Battle and Trainer logic
│   ├── storage.py     # Pokémon instances, moves and type chart
│   ├── UI.py          # User interaction
│
├── main.py            # Entry point
````

---

## 🧩 Core Classes

### `pokemon.py`

#### `Pokemon`

Represents a Pokémon with:

* Name
* Type
* Moves
* Level
* Current HP
* Calculated stats (HP, Attack, Defense, etc.)

#### `Stats`

Handles:

* Base stats
* IVs (randomized or defined)
* EVs (default or customizable)
* Final stat calculation based on level

#### `Move`

Represents a move with:

* Name
* Type
* Category (`physical` or `special`)
* Power
* Accuracy

---

## ⚙️ Damage Formula

```text
Damage = (((2 * Level / 5 + 2) * Power * A / D) / 50 + 2) * Modifier
```

---

## 🎮 How to Play

Run commands from the project root (not from inside `src/`):

**Terminal version:**
```bash
python -m src.main
```

**Graphical version (Tkinter):**
```bash
python -m src.main_gui
```

1. Choose 3 Pokémon for your team

3. Battle begins:

   * Select moves each turn
   * Faster Pokémon attacks first
   * Continue until one team is defeated

---

## 📄 License

This project is for educational purposes.

---

## 👨‍💻 Author

Developed by Luiz Henrique

```
```
