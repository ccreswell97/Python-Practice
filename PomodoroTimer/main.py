from tkinter import Button, Canvas, Label, PhotoImage, Tk
from math import floor

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

def reset_timer():
    win.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    timer_label.config(text="Timer")
    check_marks.config(text="")
    global reps 
    reps = 0

def start_timer():
    global reps 
    reps += 1
    if reps % 8 == 0:
        countdown(LONG_BREAK_MIN*60)
        timer_label.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        countdown(SHORT_BREAK_MIN*60)
        timer_label.config(text="Break", fg=PINK)
    else:
        countdown(WORK_MIN*60)
        timer_label.config(text="Work", fg=GREEN)

# Timer countdown
def countdown(count):
    minutes = floor(count / 60)
    seconds = count % 60
    canvas.itemconfig(timer_text, text="{:02d}:{:02d}".format(minutes, seconds))
    if count > 0:
        global timer
        timer = win.after(1000, countdown, count - 1)
    else:
        start_timer()
        
        marks = ""
        work_sessions = floor(reps/2)
        for i in range(work_sessions):
            marks += "✔"
        check_marks.config(text=marks)

win = Tk()
win.title("Pomodoro Timer")
win.config(padx=100, pady=50, bg=YELLOW)

tomato_img = PhotoImage(file="tomato.png")

reps = 0
timer = None

# Tomato pic and timer 
canvas = Canvas(width=220, height=224, bg=YELLOW, highlightthickness=0)
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)

# Start and Reset buttons
start_button = Button(text="Start", highlightthickness=0, bg=YELLOW, command=start_timer)
start_button.grid(row=2, column=0)

reset_button = Button(text="Reset", highlightthickness=0, bg=YELLOW, command=reset_timer)
reset_button.grid(row=2, column=2)

# Timer label
timer_label = Label(text="Timer", font=(FONT_NAME, 60, "normal"), fg=GREEN, bg=YELLOW)
timer_label.grid(row=0, column=1)

# Checks
check_marks = Label(text="", fg=GREEN, bg=YELLOW)
check_marks.grid(row=3, column=1)

win.mainloop()