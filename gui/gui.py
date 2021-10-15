import tkinter as tk
import random
import string
import time

letter_list = string.ascii_lowercase

rounds = **user input
final_score = **final final_score
starttime = 50

def countdown_clock():
    global starttime
    if starttime > 0:
        starttime -= 1
        timeGUI.config(text = f"Time: {starttime}")
        time.sleep(1)
        timeGUI.after(countdown_clock)

def new_letter():
    random.shuffle(letter_list)
    global starttime
    global final_score
    if starttime > 0:
        userinput.focus_set()
        if userinput.


root = tk.Tk()

root.title("The Input Game")
canvas = tk.Canvas(root, width=600, height = 600)
canvas.grid(columnspan = 3)

instructions = tk.Label(root, text = "Type in the letter that you see(sizing doesnt matter)", font="Raleway")
instructions.grid(columnspan=1, column=0, row=0)

timeGUI = tk.Label(root, text = f"Time: {starttime}", font = "Raleway")
timeGUI.grid(columnspan=1, column=2, row=3)


game_start_text = tk.StringVar()
game_start_text.set("Start Game")
game_start_button = tk.Button(root, textvariable=game_start_text, command=lambda:"here is the function", font="Raleway", height = 2, width = 15, bg = "black", fg = "white")
game_start_button.grid(column=1, row=2)

game_display_box = tk.Text(root, height = 12, width = 12, padx=18, pady=18)
game_display_box.insert(1.0, )
game_display_box.tag_configure("center", justify="center")
game_display_box.tag_add("center", 1.0, "end")
game_display_box.grid(column=1, row=3)






root.mainloop()