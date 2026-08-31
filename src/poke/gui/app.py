import tkinter as tk

from src.poke.gui.battle_frame import BattleFrame
from src.poke.gui.team_select_frame import TeamSelectFrame


class PokeBattleApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Pokémon Battle Simulator")
        self.root.geometry("700x500")

        container = tk.Frame(self.root)
        container.pack(fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        team_select = TeamSelectFrame(container, self)
        team_select.grid(row=0, column=0, sticky="nsew")
        self.frames["team_select"] = team_select

        battle = BattleFrame(container, self)
        battle.grid(row=0, column=0, sticky="nsew")
        self.frames["battle"] = battle

        self.show_frame("team_select")

    def show_frame(self, name):
        self.frames[name].tkraise()

    def start_battle(self, trainer, defender):
        self.frames["battle"].start(trainer, defender)
        self.show_frame("battle")

    def run(self):
        self.root.mainloop()


def run():
    PokeBattleApp().run()
