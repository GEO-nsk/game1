from tkinter import *
from tkinter import ttk
import random
import ru_local as ru


quest_text = [ru.quest_spy, ru.quest_farmers]
random_quest = random.randint(0, 1)

game = Tk()  # creating window
game.title('The game')  # give name to window
game.geometry('1600x900')  # window size


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

    quest_frame_style = ttk.Style()
    quest_frame_style.configure('quest.TFrame', background='white', foreground='black')

    answer_button_style = ttk.Style()
    answer_button_style.configure('answer.TButton', font=('Arial', 16))

    quest_frame = ttk.Frame(game, style='quest.TFrame')
    quest_frame.place(relx=0.5, rely=0.35, anchor=CENTER, height=400, width=800)

    game_text = ttk.Label(quest_frame, text=quest_text[random_quest], wraplength=800,
                          background='white', foreground='black', font=('Arial', 26))
    game_text.place(relx=0.01, rely=0.01, anchor=NW)

    first_answer_button = ttk.Button(text='Answer 1', style='answer.TButton')
    first_answer_button.place(relx=0.5, rely=0.595, anchor=CENTER, height=35, width=805)

    second_answer_button = ttk.Button(text='Answer 2', style='answer.TButton')
    second_answer_button.place(relx=0.5, rely=0.638, anchor=CENTER, height=35, width=805)

    third_answer_button = ttk.Button(text='Answer 3', style='answer.TButton')
    third_answer_button.place(relx=0.5, rely=0.681, anchor=CENTER, height=35, width=805)

    back_to_menu_button()

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
