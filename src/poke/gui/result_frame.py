import tkinter as tk


class ResultFrame(tk.Frame):
    def __init__(self, parent, app):
        super().__init__(parent)
        self.app = app

        self.result_label = tk.Label(self, text="", font=("Segoe UI", 20, "bold"))
        self.result_label.pack(pady=60)

        buttons = tk.Frame(self)
        buttons.pack(pady=10)
        tk.Button(buttons, text="Play Again", command=self._play_again).grid(row=0, column=0, padx=10)
        tk.Button(buttons, text="Exit", command=self._exit).grid(row=0, column=1, padx=10)

    def show(self, player_won):
        text = "🏆 You win!" if player_won else "💀 You lose!"
        self.result_label.config(text=text)

    def _play_again(self):
        self.app.restart()

    def _exit(self):
        self.app.root.destroy()
