import random
import tkinter as tk

from src.poke.battle import Trainer
from src.poke.storage import get_starting_roster


class TeamSelectFrame(tk.Frame):
    def __init__(self, parent, app):
        super().__init__(parent)
        self.app = app
        self.roster = get_starting_roster()
        self.team = []
        self.opponent = []
        self.trainer = None
        self.defender = None

        tk.Label(self, text="🎮 Choose your team (3 Pokémon)", font=("Segoe UI", 14, "bold")).pack(pady=10)

        self.listbox = tk.Listbox(self, width=40, height=12)
        self.listbox.pack(pady=5)
        self.listbox.bind("<<ListboxSelect>>", self._on_select)
        self._refresh_listbox()

        self.pick_button = tk.Button(self, text="Pick", command=self._on_pick, state="disabled")
        self.pick_button.pack(pady=5)

        self.team_label = tk.Label(self, text="Team: 0/3")
        self.team_label.pack(pady=5)

        self.team_list_label = tk.Label(self, text="", justify="left")
        self.team_list_label.pack(pady=5)

        self.opponent_label = tk.Label(self, text="", justify="left")
        self.opponent_label.pack(pady=5)

        self.start_button = tk.Button(self, text="Start Battle", command=self._start_battle, state="disabled")
        self.start_button.pack(pady=10)

    def _refresh_listbox(self):
        self.listbox.delete(0, tk.END)
        for pokemon in self.roster:
            self.listbox.insert(tk.END, pokemon.name)

    def _on_select(self, _event):
        self.pick_button.config(state="normal" if self.listbox.curselection() else "disabled")

    def _on_pick(self):
        selection = self.listbox.curselection()
        if not selection:
            return

        chosen = self.roster.pop(selection[0])
        self.team.append(chosen)
        self._refresh_listbox()
        self.pick_button.config(state="disabled")
        self.team_label.config(text=f"Team: {len(self.team)}/3")
        self.team_list_label.config(text="🧑 Your Team\n" + "\n".join(f"• {p.name}" for p in self.team))

        if len(self.team) == 3:
            self._generate_opponent()

    def _generate_opponent(self):
        while len(self.opponent) < 3:
            poke = random.choice(self.roster)
            self.roster.remove(poke)
            self.opponent.append(poke)

        self.trainer = Trainer(self.team)
        self.defender = Trainer(self.opponent)

        self.listbox.pack_forget()
        self.pick_button.pack_forget()
        self.opponent_label.config(text="🤖 Opponent Team\n" + "\n".join(f"• {p.name}" for p in self.opponent))
        self.start_button.config(state="normal")

    def _start_battle(self):
        self.app.start_battle(self.trainer, self.defender)
