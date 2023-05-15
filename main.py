"""
Title: The game

Group:
Gagol Egor
Tarlo Evgeny
Karpenko Nikolay
"""

import tkinter

army = 50
budget = 50
loyalty = 50
tech = 50
ecology = 50
quests = []  # Events list

from tkinter import *
from tkinter import ttk
import random
import ru_local as ru


game = Tk()  # creating window
game.title('The game')  # give name to window
game.geometry('1600x900')  # window size


def quest_spy():
    quest_frame_style = ttk.Style()
    quest_frame_style.configure('quest_frame.TFrame', background='white', foreground='black')

    quest_frame = ttk.Frame(game, style='quest_frame.TFrame')
    quest_frame.place(relx=0.5, rely=0.35, anchor=CENTER, height=400, width=800)

    game_text = ttk.Label(quest_frame, text=ru.quest_spy, wraplength=800,
                          background='white', foreground='black', font=('Arial', 26))
    game_text.place(relx=0.01, rely=0.01, anchor=NW)

    answer_button_style = ttk.Style()
    answer_button_style.configure('answer_frame.TButton', font=('Arial', 16))

    first_answer_button = ttk.Button(text=ru.quest_answer_spy_1, style='answer_frame.TButton')
    first_answer_button.place(relx=0.5, rely=0.6, anchor=CENTER, height=45, width=805)

    second_answer_button = ttk.Button(text=ru.quest_answer_spy_2, style='answer_frame.TButton')
    second_answer_button.place(relx=0.5, rely=0.651, anchor=CENTER, height=45, width=805)

def quest_farmers():
    quest_frame_style = ttk.Style()
    quest_frame_style.configure('quest_frame.TFrame', background='white', foreground='black')

    quest_frame = ttk.Frame(game, style='quest_frame.TFrame')
    quest_frame.place(relx=0.5, rely=0.35, anchor=CENTER, height=400, width=800)

    game_text = ttk.Label(quest_frame, text=ru.quest_farmers, wraplength=800,
                          background='white', foreground='black', font=('Arial', 26))
    game_text.place(relx=0.01, rely=0.01, anchor=NW)

    answer_button_style = ttk.Style()
    answer_button_style.configure('answer_frame.TButton', font=('Arial', 16))

    first_answer_button = ttk.Button(text=ru.quest_answer_farmers_1, style='answer_frame.TButton')
    first_answer_button.place(relx=0.5, rely=0.6, anchor=CENTER, height=45, width=805)

    second_answer_button = ttk.Button(text=ru.quest_answer_farmers_2, style='answer_frame.TButton')
    second_answer_button.place(relx=0.5, rely=0.651, anchor=CENTER, height=45, width=805)

    third_answer_button = ttk.Button(text=ru.quest_answer_farmers_3, style='answer_frame.TButton')
    third_answer_button.place(relx=0.5, rely=0.702, anchor=CENTER, height=45, width=805)

def quest_high_water():
    quest_frame_style = ttk.Style()
    quest_frame_style.configure('quest_frame.TFrame', background='white', foreground='black')

    quest_frame = ttk.Frame(game, style='quest_frame.TFrame')
    quest_frame.place(relx=0.5, rely=0.35, anchor=CENTER, height=400, width=800)

    game_text = ttk.Label(quest_frame, text=ru.quest_high_water, wraplength=800,
                          background='white', foreground='black', font=('Arial', 26))
    game_text.place(relx=0.01, rely=0.01, anchor=NW)

    answer_button_style = ttk.Style()
    answer_button_style.configure('answer_frame.TButton', font=('Arial', 16))

    first_answer_button = ttk.Button(text=ru.quest_answer_high_water_1, style='answer_frame.TButton')
    first_answer_button.place(relx=0.5, rely=0.6, anchor=CENTER, height=45, width=805)

    second_answer_button = ttk.Button(text=ru.quest_answer_high_water_2, style='answer_frame.TButton')
    second_answer_button.place(relx=0.5, rely=0.651, anchor=CENTER, height=45, width=805)

def quest_wedding():
    quest_frame_style = ttk.Style()
    quest_frame_style.configure('quest_frame.TFrame', background='white', foreground='black')

    quest_frame = ttk.Frame(game, style='quest_frame.TFrame')
    quest_frame.place(relx=0.5, rely=0.35, anchor=CENTER, height=400, width=800)

    game_text = ttk.Label(quest_frame, text=ru.quest_wedding, wraplength=800,
                          background='white', foreground='black', font=('Arial', 26))
    game_text.place(relx=0.01, rely=0.01, anchor=NW)

    answer_button_style = ttk.Style()
    answer_button_style.configure('answer_frame.TButton', font=('Arial', 16))

    first_answer_button = ttk.Button(text=ru.quest_answer_wedding_1, style='answer_frame.TButton')
    first_answer_button.place(relx=0.5, rely=0.6, anchor=CENTER, height=45, width=805)

    second_answer_button = ttk.Button(text=ru.quest_answer_wedding_2, style='answer_frame.TButton')
    second_answer_button.place(relx=0.5, rely=0.651, anchor=CENTER, height=45, width=805)

    third_answer_button = ttk.Button(text=ru.quest_answer_wedding_3, style='answer_frame.TButton')
    third_answer_button.place(relx=0.5, rely=0.702, anchor=CENTER, height=45, width=805)

def quest_scientist():
    quest_frame_style = ttk.Style()
    quest_frame_style.configure('quest_frame.TFrame', background='white', foreground='black')

    quest_frame = ttk.Frame(game, style='quest_frame.TFrame')
    quest_frame.place(relx=0.5, rely=0.35, anchor=CENTER, height=400, width=800)

    game_text = ttk.Label(quest_frame, text=ru.quest_scientist, wraplength=800,
                          background='white', foreground='black', font=('Arial', 26))
    game_text.place(relx=0.01, rely=0.01, anchor=NW)

    answer_button_style = ttk.Style()
    answer_button_style.configure('answer_frame.TButton', font=('Arial', 16))

    first_answer_button = ttk.Button(text=ru.quest_answer_scientist_1, style='answer_frame.TButton')
    first_answer_button.place(relx=0.5, rely=0.6, anchor=CENTER, height=45, width=805)

    second_answer_button = ttk.Button(text=ru.quest_answer_scientist_2, style='answer_frame.TButton')
    second_answer_button.place(relx=0.5, rely=0.651, anchor=CENTER, height=45, width=805)

def quest_rallies():
    quest_frame_style = ttk.Style()
    quest_frame_style.configure('quest_frame.TFrame', background='white', foreground='black')

    quest_frame = ttk.Frame(game, style='quest_frame.TFrame')
    quest_frame.place(relx=0.5, rely=0.35, anchor=CENTER, height=400, width=800)

    game_text = ttk.Label(quest_frame, text=ru.quest_rallies, wraplength=800,
                          background='white', foreground='black', font=('Arial', 26))
    game_text.place(relx=0.01, rely=0.01, anchor=NW)

    answer_button_style = ttk.Style()
    answer_button_style.configure('answer_frame.TButton', font=('Arial', 16))

    first_answer_button = ttk.Button(text=ru.quest_answer_rallies_1, style='answer_frame.TButton')
    first_answer_button.place(relx=0.5, rely=0.6, anchor=CENTER, height=45, width=805)

    second_answer_button = ttk.Button(text=ru.quest_answer_rallies_2, style='answer_frame.TButton')
    second_answer_button.place(relx=0.5, rely=0.651, anchor=CENTER, height=45, width=805)

    third_answer_button = ttk.Button(text=ru.quest_answer_rallies_3, style='answer_frame.TButton')
    third_answer_button.place(relx=0.5, rely=0.702, anchor=CENTER, height=45, width=805)

def quest_escape():
    quest_frame_style = ttk.Style()
    quest_frame_style.configure('quest_frame.TFrame', background='white', foreground='black')

    quest_frame = ttk.Frame(game, style='quest_frame.TFrame')
    quest_frame.place(relx=0.5, rely=0.35, anchor=CENTER, height=400, width=800)

    game_text = ttk.Label(quest_frame, text=ru.quest_escape, wraplength=800,
                          background='white', foreground='black', font=('Arial', 26))
    game_text.place(relx=0.01, rely=0.01, anchor=NW)

    answer_button_style = ttk.Style()
    answer_button_style.configure('answer_frame.TButton', font=('Arial', 16))

    first_answer_button = ttk.Button(text=ru.quest_answer_escape_1, style='answer_frame.TButton')
    first_answer_button.place(relx=0.5, rely=0.6, anchor=CENTER, height=45, width=805)

    second_answer_button = ttk.Button(text=ru.quest_answer_escape_2, style='answer_frame.TButton')
    second_answer_button.place(relx=0.5, rely=0.651, anchor=CENTER, height=45, width=805)

    third_answer_button = ttk.Button(text=ru.quest_answer_escape_3, style='answer_frame.TButton')
    third_answer_button.place(relx=0.5, rely=0.702, anchor=CENTER, height=45, width=805)

def quest_homeless():
    quest_frame_style = ttk.Style()
    quest_frame_style.configure('quest_frame.TFrame', background='white', foreground='black')

    quest_frame = ttk.Frame(game, style='quest_frame.TFrame')
    quest_frame.place(relx=0.5, rely=0.35, anchor=CENTER, height=400, width=800)

    game_text = ttk.Label(quest_frame, text=ru.quest_homeless, wraplength=800,
                          background='white', foreground='black', font=('Arial', 26))
    game_text.place(relx=0.01, rely=0.01, anchor=NW)

    answer_button_style = ttk.Style()
    answer_button_style.configure('answer_frame.TButton', font=('Arial', 16))

    first_answer_button = ttk.Button(text=ru.quest_answer_homeless_1, style='answer_frame.TButton')
    first_answer_button.place(relx=0.5, rely=0.6, anchor=CENTER, height=45, width=805)

    second_answer_button = ttk.Button(text=ru.quest_answer_homeless_2, style='answer_frame.TButton')
    second_answer_button.place(relx=0.5, rely=0.651, anchor=CENTER, height=45, width=805)

    third_answer_button = ttk.Button(text=ru.quest_answer_homeless_3, style='answer_frame.TButton')
    third_answer_button.place(relx=0.5, rely=0.702, anchor=CENTER, height=45, width=805)

def quest_earthquake():
    quest_frame_style = ttk.Style()
    quest_frame_style.configure('quest_frame.TFrame', background='white', foreground='black')

    quest_frame = ttk.Frame(game, style='quest_frame.TFrame')
    quest_frame.place(relx=0.5, rely=0.35, anchor=CENTER, height=400, width=800)

    game_text = ttk.Label(quest_frame, text=ru.quest_earthquake, wraplength=800,
                          background='white', foreground='black', font=('Arial', 26))
    game_text.place(relx=0.01, rely=0.01, anchor=NW)

    answer_button_style = ttk.Style()
    answer_button_style.configure('answer_frame.TButton', font=('Arial', 16))

    first_answer_button = ttk.Button(text=ru.quest_answer_earthquake_1, style='answer_frame.TButton')
    first_answer_button.place(relx=0.5, rely=0.6, anchor=CENTER, height=45, width=805)

    second_answer_button = ttk.Button(text=ru.quest_answer_earthquake_2, style='answer_frame.TButton')
    second_answer_button.place(relx=0.5, rely=0.651, anchor=CENTER, height=45, width=805)

    third_answer_button = ttk.Button(text=ru.quest_answer_earthquake_3, style='answer_frame.TButton')
    third_answer_button.place(relx=0.5, rely=0.702, anchor=CENTER, height=45, width=805)

def quest_strike():
    quest_frame_style = ttk.Style()
    quest_frame_style.configure('quest_frame.TFrame', background='white', foreground='black')

    quest_frame = ttk.Frame(game, style='quest_frame.TFrame')
    quest_frame.place(relx=0.5, rely=0.35, anchor=CENTER, height=400, width=800)

    game_text = ttk.Label(quest_frame, text=ru.quest_strike, wraplength=800,
                          background='white', foreground='black', font=('Arial', 26))
    game_text.place(relx=0.01, rely=0.01, anchor=NW)

    answer_button_style = ttk.Style()
    answer_button_style.configure('answer_frame.TButton', font=('Arial', 16))

    first_answer_button = ttk.Button(text=ru.quest_answer_strike_1, style='answer_frame.TButton')
    first_answer_button.place(relx=0.5, rely=0.6, anchor=CENTER, height=45, width=805)

    second_answer_button = ttk.Button(text=ru.quest_answer_strike_2, style='answer_frame.TButton')
    second_answer_button.place(relx=0.5, rely=0.651, anchor=CENTER, height=45, width=805)

    third_answer_button = ttk.Button(text=ru.quest_answer_strike_3, style='answer_frame.TButton')
    third_answer_button.place(relx=0.5, rely=0.702, anchor=CENTER, height=45, width=805)

def quest_minerals():
    quest_frame_style = ttk.Style()
    quest_frame_style.configure('quest_frame.TFrame', background='white', foreground='black')

    quest_frame = ttk.Frame(game, style='quest_frame.TFrame')
    quest_frame.place(relx=0.5, rely=0.35, anchor=CENTER, height=400, width=800)

    game_text = ttk.Label(quest_frame, text=ru.quest_minerals, wraplength=800,
                          background='white', foreground='black', font=('Arial', 26))
    game_text.place(relx=0.01, rely=0.01, anchor=NW)

    answer_button_style = ttk.Style()
    answer_button_style.configure('answer_frame.TButton', font=('Arial', 16))

    first_answer_button = ttk.Button(text=ru.quest_answer_minerals_1, style='answer_frame.TButton')
    first_answer_button.place(relx=0.5, rely=0.6, anchor=CENTER, height=45, width=805)

    second_answer_button = ttk.Button(text=ru.quest_answer_minerals_2, style='answer_frame.TButton')
    second_answer_button.place(relx=0.5, rely=0.651, anchor=CENTER, height=45, width=805)

    third_answer_button = ttk.Button(text=ru.quest_answer_minerals_3, style='answer_frame.TButton')
    third_answer_button.place(relx=0.5, rely=0.702, anchor=CENTER, height=45, width=805)

list_of_quests = [quest_spy, quest_farmers, quest_high_water, quest_wedding, quest_scientist,
quest_rallies, quest_escape, quest_homeless, quest_earthquake, quest_strike, quest_minerals]


# Function to start random quest
def start_random_quest():
    random_quest = random.choice(list_of_quests)
    random_quest()

    list_of_quests.remove(random_quest)


# Function for cleaning the frame
def widget_clear(frame_name):
    for widget in frame_name.winfo_children():
        widget.destroy()

# Function showing button to return to main menu
def back_to_menu_button():
    back_menu_button_style = ttk.Style()
    back_menu_button_style.configure('back_menu.TButton', font=('Arial', 12))

    back_menu_button = ttk.Button(text='Back to the Main Menu', style='back_menu.TButton', command=call_main_menu)
    back_menu_button.place(relx=0.995, rely=0.01, anchor=NE)

# Function to start the game
def start_quest():
    widget_clear(game)
    back_to_menu_button()

    start_random_quest()


# Function that calls up the main menu
def call_main_menu():
    widget_clear(game)

    menu_button_style = ttk.Style()
    menu_button_style.configure('menu.TButton', font=('Arial', 18))

    label_menu = ttk.Label(text='Main Menu', font=('Arial Black', 60))
    label_menu.place(relx=0.5, rely=0.08, anchor=CENTER)

    start_button = ttk.Button(text='Start Game', style='menu.TButton', command=start_quest)
    start_button.place(relx=0.5, rely=0.5, anchor=CENTER, height=50, width=200)

    quit_button = ttk.Button(text='Quit', style='menu.TButton', command=game.quit)
    quit_button.place(relx=0.5, rely=0.56, anchor=CENTER, height=50, width=200)


call_main_menu()

game.mainloop()