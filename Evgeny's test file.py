from tkinter import *
from tkinter import ttk

game = Tk()  # creating window
game.title('The game')  # give name to window
game.geometry('1920x1080')
frame = Frame(game)
frame.pack(side=LEFT, fill=BOTH, expand=True)

quitButton = ttk.Button(text='Quit', command=game.quit)  # creating quit button
quitButton.place(relx=.5, rely=.99, anchor='s')

label1 = Label(frame, text='Привет, это метка!')
label1.pack()

entry1 = Entry(frame)
entry1.pack()

for widget in frame.winfo_children():
    widget.destroy()

label2 = Label(frame, text='Привет, это метка!')
label2.pack()

game.update()
game.mainloop()
