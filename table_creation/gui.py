import tkinter as tk

class MyFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, background="#FFFFFF")

        self.parent = parent

def start():
    window = tk.Tk()
    MyFrame(window)
    window.mainloop()
