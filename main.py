from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

title_label = Label(text="Timer", font=(FONT_NAME, 30, "bold"), fg=GREEN, bg=YELLOW)
title_label.grid(column=1, row=0)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
image = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=image)
canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 24, "bold"))
canvas.grid(column=1, row=1)

start_button = Button(text="Start", font=(FONT_NAME, 12, "normal"))
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", font=(FONT_NAME, 12, "normal"))
reset_button.grid(column=2, row=2)

check_label = Label(text="✓", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 16, "bold"))
check_label.grid(column=1, row=2)

# All code before main loop
window.mainloop()
