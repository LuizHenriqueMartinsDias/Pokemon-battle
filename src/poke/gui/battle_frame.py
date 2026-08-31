import tkinter as tk

from src.poke.battle import Battle


class BattleFrame(tk.Frame):
    def __init__(self, parent, app):
        super().__init__(parent)
        self.app = app
        self.battle = None

        header = tk.Frame(self)
        header.pack(pady=10)
        self.player_label = tk.Label(header, text="", font=("Segoe UI", 12, "bold"))
        self.player_label.grid(row=0, column=0, padx=20)
        self.opponent_label = tk.Label(header, text="", font=("Segoe UI", 12, "bold"))
        self.opponent_label.grid(row=0, column=1, padx=20)

        self.log_label = tk.Label(self, text="", justify="left", anchor="w", wraplength=650)
        self.log_label.pack(pady=10, fill="x", padx=20)

        self.moves_frame = tk.Frame(self)
        self.moves_frame.pack(pady=10)
        self.move_buttons = []

    def start(self, trainer, defender):
        self.battle = Battle(
            trainer,
            defender,
            on_message=self._log,
            on_faint=self._on_faint,
            on_battle_end=self._on_battle_end,
        )
        self.battle.begin_battle()
        self.log_label.config(text="")
        self._render_state()

    def _log(self, message):
        current = self.log_label.cget("text")
        new_text = f"{current}\n{message}" if current else message
        self.log_label.config(text=new_text)

    def _on_faint(self, pokemon):
        pass

    def _on_battle_end(self, winner):
        self._clear_move_buttons()

    def _render_state(self):
        atk = self.battle.atk_pokemon
        dfd = self.battle.def_pokemon
        self.player_label.config(text=f"{atk.name}\n{atk.hp}/{atk.max_hp} HP")
        self.opponent_label.config(text=f"{dfd.name}\n{dfd.hp}/{dfd.max_hp} HP")
        self._render_move_buttons()

    def _clear_move_buttons(self):
        for button in self.move_buttons:
            button.destroy()
        self.move_buttons = []

    def _render_move_buttons(self):
        self._clear_move_buttons()
        for i, move in enumerate(self.battle.get_active_moves()):
            button = tk.Button(
                self.moves_frame,
                text=f"{move.name} ({move.category})",
                command=lambda index=i: self._on_move_click(index),
            )
            button.grid(row=i // 2, column=i % 2, padx=5, pady=5, sticky="ew")
            self.move_buttons.append(button)

    def _on_move_click(self, move_index):
        result = self.battle.resolve_turn(move_index)
        if result.battle_over:
            self.player_label.config(
                text=f"{self.battle.atk_pokemon.name}\n{self.battle.atk_pokemon.hp}/{self.battle.atk_pokemon.max_hp} HP"
            )
            self.opponent_label.config(
                text=f"{self.battle.def_pokemon.name}\n{self.battle.def_pokemon.hp}/{self.battle.def_pokemon.max_hp} HP"
            )
            return
        self._render_state()
