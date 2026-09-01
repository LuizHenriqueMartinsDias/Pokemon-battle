import tkinter as tk

from src.poke.gui.battle_frame import BattleFrame
from src.poke.gui.result_frame import ResultFrame
from src.poke.gui.team_select_frame import TeamSelectFrame


class PokeBattleApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Pokémon Battle Simulator")
        self.root.geometry("700x500")

        self.container = tk.Frame(self.root)
        self.container.pack(fill="both", expand=True)
        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        self._add_team_select_frame()

        battle = BattleFrame(self.container, self)
        battle.grid(row=0, column=0, sticky="nsew")
        self.frames["battle"] = battle

        result = ResultFrame(self.container, self)
        result.grid(row=0, column=0, sticky="nsew")
        self.frames["result"] = result

        self.show_frame("team_select")

    def _add_team_select_frame(self):
        team_select = TeamSelectFrame(self.container, self)
        team_select.grid(row=0, column=0, sticky="nsew")
        self.frames["team_select"] = team_select

    def show_frame(self, name):
        self.frames[name].tkraise()

    def start_battle(self, trainer, defender):
        self.frames["battle"].start(trainer, defender)
        self.show_frame("battle")

    def show_result(self, player_won):
        self.frames["result"].show(player_won)
        self.show_frame("result")

    def restart(self):
        self.frames["team_select"].destroy()
        self._add_team_select_frame()
        self.show_frame("team_select")

    def run(self):
        self.root.mainloop()


def run():
    PokeBattleApp().run()
