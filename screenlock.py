from time import sleep
from subprocess import run

from tkinter import *

def change_color():
    current_color = box.cget("background")
    next_color = "blue" if current_color == "yellow" else "yellow"
    box.config(background=next_color)
    root.after(1000, change_color)


while True:
    hour = 0
    while hour < 3:
        sleep(9000)
        root = Tk()
        box = Text(root, background="blue")
        box.pack()
        change_color()
        root.mainloop()
        hour += 1
    run("i3lock", shell=True, check=True)
