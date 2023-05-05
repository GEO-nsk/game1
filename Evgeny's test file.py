import tkinter
from tkinter import ttk


game = tkinter.Tk()  # creating window
game.title('The game')  # give name to window
game.geometry('1920x1080')  # window sizes

btn = ttk.Button(text='Test Click')  # creating test button
btn.pack()

quitButton = ttk.Button(text='Quit', command=game.quit)  # creating quit button
quitButton.place(x=1650, y=900)  # placing quit button

game.mainloop()
