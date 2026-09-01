import tkinter as tk
from tkinter import ttk

from src.poke.battle import Battle


class BattleFrame(tk.Frame):
    def __init__(self, parent, app):
        super().__init__(parent)
        self.app = app
        self.battle = None
        self.player_trainer = None

        header = tk.Frame(self)
        header.pack(pady=10, fill="x", padx=20)

        player_col = tk.Frame(header)
        player_col.grid(row=0, column=0, padx=20, sticky="w")
        self.player_name_label = tk.Label(player_col, text="", font=("Segoe UI", 12, "bold"))
        self.player_name_label.pack(anchor="w")
        self.player_hp_bar = ttk.Progressbar(player_col, length=200, mode="determinate")
        self.player_hp_bar.pack(anchor="w")
        self.player_hp_label = tk.Label(player_col, text="")
        self.player_hp_label.pack(anchor="w")

        opponent_col = tk.Frame(header)
        opponent_col.grid(row=0, column=1, padx=20, sticky="e")
        self.opponent_name_label = tk.Label(opponent_col, text="", font=("Segoe UI", 12, "bold"))
        self.opponent_name_label.pack(anchor="w")
        self.opponent_hp_bar = ttk.Progressbar(opponent_col, length=200, mode="determinate")
        self.opponent_hp_bar.pack(anchor="w")
        self.opponent_hp_label = tk.Label(opponent_col, text="")
        self.opponent_hp_label.pack(anchor="w")

        log_frame = tk.Frame(self)
        log_frame.pack(pady=10, fill="both", expand=True, padx=20)
        scrollbar = tk.Scrollbar(log_frame)
        scrollbar.pack(side="right", fill="y")
        self.log_text = tk.Text(log_frame, height=12, wrap="word", state="disabled", yscrollcommand=scrollbar.set)
        self.log_text.pack(side="left", fill="both", expand=True)
        scrollbar.config(command=self.log_text.yview)

        self.moves_frame = tk.Frame(self)
        self.moves_frame.pack(pady=10)
        self.move_buttons = []

    def start(self, trainer, defender):
        self.player_trainer = trainer
        self.battle = Battle(
            trainer,
            defender,
            on_message=self._log,
            on_faint=self._on_faint,
            on_battle_end=self._on_battle_end,
        )
        self.battle.begin_battle()
        self._clear_log()
        self._render_state()

    def _clear_log(self):
        self.log_text.config(state="normal")
        self.log_text.delete("1.0", tk.END)
        self.log_text.config(state="disabled")

    def _log(self, message):
        self.log_text.config(state="normal")
        self.log_text.insert(tk.END, message + "\n")
        self.log_text.config(state="disabled")
        self.log_text.see(tk.END)

    def _on_faint(self, pokemon):
        pass

    def _on_battle_end(self, winner):
        self._clear_move_buttons()
        self.app.show_result(winner is self.player_trainer)

    def _render_state(self):
        atk = self.battle.atk_pokemon
        dfd = self.battle.def_pokemon
        self._update_hp_display(atk, dfd)
        self._render_move_buttons()

    def _update_hp_display(self, atk, dfd):
        self.player_name_label.config(text=atk.name)
        self.player_hp_bar.config(maximum=atk.max_hp, value=max(atk.hp, 0))
        self.player_hp_label.config(text=f"{max(atk.hp, 0)}/{atk.max_hp} HP")

        self.opponent_name_label.config(text=dfd.name)
        self.opponent_hp_bar.config(maximum=dfd.max_hp, value=max(dfd.hp, 0))
        self.opponent_hp_label.config(text=f"{max(dfd.hp, 0)}/{dfd.max_hp} HP")

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
            self._update_hp_display(self.battle.atk_pokemon, self.battle.def_pokemon)
            return
        self._render_state()
