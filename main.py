"""
Title: The game

Group:
Gagol Egor 55
Tarlo Evgeny 64
Karpenko Nikolay 40
"""

from tkinter import *
from tkinter import ttk
import random
import ru_local as ru


# Functions-answers for answer buttons
def first_spy_answer():
    stats_change(-10, -15, -5, 0, 5)
    check_stats()
    quest_anw_frame_style = ttk.Style()
    quest_anw_frame_style.configure('quest_anw_frame.TFrame', background='white', foreground='black')
    quest_anw_frame = ttk.Frame(game, style='quest_anw_frame.TFrame')
    quest_anw_frame.place(relx=0.5, rely=0.4, anchor=CENTER, height=500, width=805)

    game_anw_text = ttk.Label(quest_anw_frame, text=ru.quest_anw_spy, wraplength=800,
                          background='white', foreground='black', font=('Arial', 26))
    game_anw_text.place(relx=0.01, rely=0.01, anchor=NW)
    first_anw_button = ttk.Button(text='OK', style='answer_frame.TButton', command=start_random_quest)
    first_anw_button.place(relx=0.5, rely=0.65, anchor=CENTER, height=50, width=805)
    win_check()

def second_spy_answer():
    stats_change(0, 5, 0, 5, 0)
    check_stats()
    start_random_quest()
    win_check()


def first_farmers_answer():
    stats_change(0, 0, 20, 0, 0)
    check_stats()
    start_random_quest()
    win_check()

def second_farmers_answer():
    stats_change(0, 20, -10, 0, 0)
    check_stats()
    start_random_quest()
    win_check()


def first_high_water_answer():
    stats_change(-5, 15, -10, 0, 5)
    check_stats()
    start_random_quest()
    win_check()

def second_high_water_answer():
    stats_change(0, -15, 0, 0, -10)
    check_stats()
    start_random_quest()
    win_check()


def first_wedding_answer():
    stats_change(10, 0, 10, 5, 0)
    check_stats()
    start_random_quest()
    win_check()

def second_wedding_answer():
    stats_change(-5, -15, -10, 0, 0)
    check_stats()
    start_random_quest()
    win_check()


def first_scientist_answer():
    stats_change(0, 20, -15, 10, -15)
    check_stats()
    start_random_quest()
    win_check()

def second_scientist_answer():
    stats_change(0, -20, 5, -15, 0)
    check_stats()
    start_random_quest()
    win_check()


def first_rallies_answer():
    stats_change(0, -15, 10, 0, 0)
    check_stats()
    start_random_quest()
    win_check()

def second_rallies_answer():
    stats_change(-10, -5, -10, 0, 0)
    check_stats()
    start_random_quest()
    win_check()


def first_escape_answer():
    stats_change(-10, -15, 5, 0, 0)
    check_stats()
    start_random_quest()
    win_check()

def second_escape_answer():
    stats_change(0, 0, -15, 0, 0)
    check_stats()
    win_check()
    start_random_quest()


def first_homeless_answer():
    stats_change(-5, -10, 10, 0, 0)
    check_stats()
    start_random_quest()
    win_check()

def second_homeless_answer():
    stats_change(-15, -10, -10, 0, 0)
    check_stats()
    start_random_quest()
    win_check()


def first_earthquake_answer():
    stats_change(-10, -5, -10, 0, 0)
    check_stats()
    start_random_quest()
    win_check()

def second_earthquake_answer():
    stats_change(-10, -5, +5, 0, 0)
    check_stats()
    start_random_quest()
    win_check()


def first_strike_answer():
    stats_change(-5, -10, -10, -15, -15)
    check_stats()
    start_random_quest()
    win_check()

def second_strike_answer():
    stats_change(5, -5, 10, -10, 10)
    check_stats()
    start_random_quest()
    win_check()


def first_minerals_answer():
    stats_change(0, 15, -15, 15, -25)
    check_stats()
    start_random_quest()
    win_check()

def second_minerals_answer():
    stats_change(0, -10, -5, -10, 5)
    check_stats()
    start_random_quest()
    win_check()


# Statistics function
def stats_text_ingame():
    stats_text = ttk.Label(game, text=ru.army, wraplength=250,
                           background='white', foreground='black', font=('Arial', 24))
    stats_text.place(relx=0.2, rely=0.001, anchor=N)

    stats_text = ttk.Label(game, text=ru.budget, wraplength=250,
                           background='white', foreground='black', font=('Arial', 24))
    stats_text.place(relx=0.35, rely=0.001, anchor=N)

    stats_text = ttk.Label(game, text=ru.loyalty, wraplength=250,
                           background='white', foreground='black', font=('Arial', 26))
    stats_text.place(relx=0.5, rely=0.001, anchor=N)
    stats_text = ttk.Label(game, text=ru.tech, wraplength=250,
                           background='white', foreground='black', font=('Arial', 26))
    stats_text.place(relx=0.65, rely=0.001, anchor=N)

    stats_text = ttk.Label(game, text=ru.ecology, wraplength=250,
                           background='white', foreground='black', font=('Arial', 26))
    stats_text.place(relx=0.8, rely=0.001, anchor=N)

# Statistics digits function
def stats_digits_ingame():
    stats_text = ttk.Label(game, text=str(army[0]), wraplength=250,
                           background='white', foreground='black', font=('Arial', 24))
    stats_text.place(relx=0.246, rely=0.001, anchor=N)

    stats_text = ttk.Label(game, text=str(budget[0]), wraplength=250,
                           background='white', foreground='black', font=('Arial', 24))
    stats_text.place(relx=0.4034, rely=0.001, anchor=N)

    stats_text = ttk.Label(game, text=str(loyalty[0]), wraplength=250,
                           background='white', foreground='black', font=('Arial', 26))
    stats_text.place(relx=0.577, rely=0.001, anchor=N)

    stats_text = ttk.Label(game, text=str(tech[0]), wraplength=250,
                           background='white', foreground='black', font=('Arial', 26))
    stats_text.place(relx=0.697, rely=0.001, anchor=N)

    stats_text = ttk.Label(game, text=str(ecology[0]), wraplength=250,
                           background='white', foreground='black', font=('Arial', 26))
    stats_text.place(relx=0.864, rely=0.001, anchor=N)


# Quests functions
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

    first_answer_button = ttk.Button(text=ru.quest_answer_spy_1, style='answer_frame.TButton', command=first_spy_answer)
    first_answer_button.place(relx=0.5, rely=0.6, anchor=CENTER, height=45, width=805)

    second_answer_button = ttk.Button(text=ru.quest_answer_spy_2, style='answer_frame.TButton',
                                      command=second_spy_answer)
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

    first_answer_button = ttk.Button(text=ru.quest_answer_farmers_1, style='answer_frame.TButton',
                                     command=first_farmers_answer)
    first_answer_button.place(relx=0.5, rely=0.6, anchor=CENTER, height=45, width=805)

    second_answer_button = ttk.Button(text=ru.quest_answer_farmers_2, style='answer_frame.TButton',
                                      command=second_farmers_answer)
    second_answer_button.place(relx=0.5, rely=0.651, anchor=CENTER, height=45, width=805)


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

    first_answer_button = ttk.Button(text=ru.quest_answer_high_water_1, style='answer_frame.TButton',
                                     command=first_high_water_answer)
    first_answer_button.place(relx=0.5, rely=0.6, anchor=CENTER, height=45, width=805)

    second_answer_button = ttk.Button(text=ru.quest_answer_high_water_2, style='answer_frame.TButton',
                                      command=second_high_water_answer)
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

    first_answer_button = ttk.Button(text=ru.quest_answer_wedding_1, style='answer_frame.TButton',
                                     command=first_wedding_answer)
    first_answer_button.place(relx=0.5, rely=0.6, anchor=CENTER, height=45, width=805)

    second_answer_button = ttk.Button(text=ru.quest_answer_wedding_2, style='answer_frame.TButton',
                                     command=second_wedding_answer)
    second_answer_button.place(relx=0.5, rely=0.651, anchor=CENTER, height=45, width=805)


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

    first_answer_button = ttk.Button(text=ru.quest_answer_scientist_1, style='answer_frame.TButton',
                                     command=first_scientist_answer)
    first_answer_button.place(relx=0.5, rely=0.6, anchor=CENTER, height=45, width=805)

    second_answer_button = ttk.Button(text=ru.quest_answer_scientist_2, style='answer_frame.TButton',
                                     command=second_scientist_answer)
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

    first_answer_button = ttk.Button(text=ru.quest_answer_rallies_1, style='answer_frame.TButton',
                                     command=first_rallies_answer)
    first_answer_button.place(relx=0.5, rely=0.6, anchor=CENTER, height=45, width=805)

    second_answer_button = ttk.Button(text=ru.quest_answer_rallies_2, style='answer_frame.TButton',
                                     command=second_rallies_answer)
    second_answer_button.place(relx=0.5, rely=0.651, anchor=CENTER, height=45, width=805)

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

    first_answer_button = ttk.Button(text=ru.quest_answer_escape_1, style='answer_frame.TButton',
                                     command=first_escape_answer)
    first_answer_button.place(relx=0.5, rely=0.6, anchor=CENTER, height=45, width=805)

    second_answer_button = ttk.Button(text=ru.quest_answer_escape_2, style='answer_frame.TButton',
                                     command=second_escape_answer)
    second_answer_button.place(relx=0.5, rely=0.651, anchor=CENTER, height=45, width=805)


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

    first_answer_button = ttk.Button(text=ru.quest_answer_homeless_1, style='answer_frame.TButton',
                                     command=first_homeless_answer)
    first_answer_button.place(relx=0.5, rely=0.6, anchor=CENTER, height=45, width=805)

    second_answer_button = ttk.Button(text=ru.quest_answer_homeless_2, style='answer_frame.TButton',
                                     command=second_homeless_answer)
    second_answer_button.place(relx=0.5, rely=0.651, anchor=CENTER, height=45, width=805)


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

    first_answer_button = ttk.Button(text=ru.quest_answer_earthquake_1, style='answer_frame.TButton',
                                     command=first_earthquake_answer)
    first_answer_button.place(relx=0.5, rely=0.6, anchor=CENTER, height=45, width=805)

    second_answer_button = ttk.Button(text=ru.quest_answer_earthquake_2, style='answer_frame.TButton',
                                     command=second_earthquake_answer)
    second_answer_button.place(relx=0.5, rely=0.651, anchor=CENTER, height=45, width=805)


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

    first_answer_button = ttk.Button(text=ru.quest_answer_strike_1, style='answer_frame.TButton',
                                     command=first_strike_answer)
    first_answer_button.place(relx=0.5, rely=0.6, anchor=CENTER, height=45, width=805)

    second_answer_button = ttk.Button(text=ru.quest_answer_strike_2, style='answer_frame.TButton',
                                      command=second_strike_answer)
    second_answer_button.place(relx=0.5, rely=0.651, anchor=CENTER, height=45, width=805)

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

    first_answer_button = ttk.Button(text=ru.quest_answer_minerals_1, style='answer_frame.TButton',
                                     command=first_minerals_answer)
    first_answer_button.place(relx=0.5, rely=0.6, anchor=CENTER, height=45, width=805)

    second_answer_button = ttk.Button(text=ru.quest_answer_minerals_2, style='answer_frame.TButton',
                                     command=second_minerals_answer)
    second_answer_button.place(relx=0.5, rely=0.651, anchor=CENTER, height=45, width=805)


# Function that calls up the main menu
def call_main_menu():
    widget_clear(game)

    menu_button_style = ttk.Style()
    menu_button_style.configure('menu.TButton', font=('Arial', 18))

    label_menu = ttk.Label(text=ru.menu_head, font=('Arial Black', 60))
    label_menu.place(relx=0.5, rely=0.08, anchor=CENTER)

    start_button = ttk.Button(text=ru.start_game, style='menu.TButton', command=start_quest)
    start_button.place(relx=0.5, rely=0.5, anchor=CENTER, height=50, width=200)

    quit_button = ttk.Button(text=ru.game_quit, style='menu.TButton', command=game.quit)
    quit_button.place(relx=0.5, rely=0.56, anchor=CENTER, height=50, width=200)


def game_loose():
    quest_frame_style = ttk.Style()
    quest_frame_style.configure('quest_frame.TFrame', background='white', foreground='black')

    quest_frame = ttk.Frame(game, style='quest_frame.TFrame')
    quest_frame.place(relx=0.5, rely=0.35, anchor=CENTER, height=600, width=1200)

    game_text = ttk.Label(quest_frame, text=ru.loser_text, wraplength=800,
                          background='white', foreground='red', font=('Arial', 56))
    game_text.place(relx=0.5, rely=0.5, anchor=CENTER)

    lose_button_style = ttk.Style()
    lose_button_style.configure('lose_button.TButton', font=('Arial', 12))

    lose_button = ttk.Button(text=ru.lose_to_menu, style='lose_button.TButton', command=call_main_menu)
    lose_button.place(relx=0.5, rely=0.71, anchor=CENTER, height=45, width=1205)

def game_win():
    widget_clear(game)

    quest_frame_style = ttk.Style()
    quest_frame_style.configure('quest_frame.TFrame', background='white', foreground='black')

    quest_frame = ttk.Frame(game, style='quest_frame.TFrame')
    quest_frame.place(relx=0.5, rely=0.35, anchor=CENTER, height=600, width=1200)

    game_text = ttk.Label(quest_frame, text=ru.winner_text, wraplength=800,
                          background='white', foreground='green', font=('Arial', 56))
    game_text.place(relx=0.5, rely=0.5, anchor=CENTER)

    lose_button_style = ttk.Style()
    lose_button_style.configure('lose_button.TButton', font=('Arial', 12))

    lose_button = ttk.Button(text=ru.lose_to_menu, style='lose_button.TButton', command=call_main_menu)
    lose_button.place(relx=0.5, rely=0.71, anchor=CENTER, height=45, width=1205)


def check_stats():
    if (army[0] <= 0 or army[0] >= 100) or (budget[0] <= 0 or budget[0] >= 100) \
        or (loyalty[0] <= 0 or loyalty[0] >= 100) or (tech[0] <= 0 or tech[0] >= 100) \
        or (ecology[0] <= 0 or ecology[0] >= 100):
        call_main_menu()
        game_loose()
        army[0] = none
        loyalty[0] = none
        budget[0] = none
        tech[0] = none
        ecology[0] = none

def win_check():
    if len(save_list_of_quests) == 0:
        widget_clear(game)
        game_win()

# Fucntion to reset the stats values
def restart_stats():
    army[0] = 0
    loyalty[0] = 0
    budget[0] = 0
    tech[0] = 0
    ecology[0] = 0

    army[0] += 50
    loyalty[0] += 50
    budget[0] += 50
    tech[0] += 50
    ecology[0] += 50


# Function for cleaning the frame
def widget_clear(frame_name):
    for widget in frame_name.winfo_children():
        widget.destroy()


# Function to start random quest
def start_random_quest():
    stats_digits_ingame()
    random_quest = random.choice(save_list_of_quests)
    random_quest()
    save_list_of_quests.remove(random_quest)
    print(save_list_of_quests)

# Function showing button to return to main menu
def back_to_menu_button():
    back_menu_button_style = ttk.Style()
    back_menu_button_style.configure('back_menu.TButton', font=('Arial', 12))

    back_menu_button = ttk.Button(text=ru.back_to_menu, style='back_menu.TButton', command=call_main_menu)
    back_menu_button.place(relx=0.998, rely=0.995, anchor=SE)


# Function to start the game
def start_quest():
    restart_stats()
    save_list_of_quests[:] = list_of_quests
    widget_clear(game)
    back_to_menu_button()
    stats_text_ingame()
    start_random_quest()


# Function to change statistics
def stats_change(army_change, budget_change, loyalty_change, tech_change, ecology_change):
    army.append(army[0] + army_change)
    army.remove(army[0])

    budget.append(budget[0] + budget_change)
    budget.remove(budget[0])

    loyalty.append(loyalty[0] + loyalty_change)
    loyalty.remove(loyalty[0])

    tech.append(tech[0] + tech_change)
    tech.remove(tech[0])

    ecology.append(ecology[0] + ecology_change)
    ecology.remove(ecology[0])


list_of_quests = [quest_spy, quest_farmers, quest_high_water, quest_wedding, quest_scientist,
quest_rallies, quest_escape, quest_homeless, quest_earthquake, quest_strike, quest_minerals]
save_list_of_quests = []


army = [50]
budget = [50]
loyalty = [50]
tech = [50]
ecology = [50]


# Creating game window
game = Tk()
game.title('The game')
game.geometry('1600x900')


call_main_menu()

game.mainloop()
