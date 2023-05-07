from tkinter import *
from tkinter import ttk


game = Tk()  # creating window
game.title('The game')  # give name to window
game.geometry('1600x900')  # window size


def widget_clear(frame_name):
    for widget in frame_name.winfo_children():
        widget.destroy()

def start_button_click():
    widget_clear(game)

    label_start_game = ttk.Label(text='Game started')
    label_start_game.pack(anchor=CENTER, expand=True)

    back_menu_button = ttk.Button(text='Back to the Main Menu', command=call_main_menu)
    back_menu_button.pack(anchor=S, expand=True)

def call_main_menu():
    widget_clear(game)

    label_menu = ttk.Label(text='Main Menu')
    label_menu.pack(anchor=N, expand=True)

    start_button = ttk.Button(text='Start Game', command=start_button_click)
    start_button.pack(anchor=CENTER, expand=True)

    quit_button = ttk.Button(text='Quit', command=game.quit)
    quit_button.pack(anchor=S, expand=True)


call_main_menu()


game.mainloop()
