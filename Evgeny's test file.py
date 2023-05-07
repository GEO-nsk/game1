from tkinter import *
from tkinter import ttk


game = Tk()  # creating window
game.title('The game')  # give name to window
game.geometry('1600x900')  # window size


def widgetclear(frame_name):
    for widget in frame_name.winfo_children():
        widget.destroy()

def callmainmenu():
    widgetclear(game)

    label_menu = ttk.Label(text='Main Menu')
    label_menu.pack(anchor=N, expand=True)

    quit_button = ttk.Button(text='Quit', command=game.quit)
    quit_button.pack(anchor=S, expand=True)


callmainmenu()


game.mainloop()
