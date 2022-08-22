from tkinter import *
import math

# Utilizar api para chamar palavras
# mostrar as palavras
# aceitar um input para as letras do jogador
# contar as letras certas e os erros
# finalizar o contador

# ------------- CODE FOR TIMER ------------

PREPARE_TIME = 5
TYPE_TIME = 60
reps = 0
timer = None

def reset_timer():
    global reps
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    tittle_label.config(text="Timer")
    reps = 0

def start_timer():
    global reps
    reps += 1
    wait_sec = PREPARE_TIME
    typing_time = TYPE_TIME

    if reps == 1:
        count_down(wait_sec)
        tittle_label.config(text="PREPARE...")
    else:
        count_down(typing_time)
        tittle_label.config(text="TYPE IT")

def count_down(count):
    global timer
    count_min = math.floor(count / 60)
    count_sec = round(count % 60, 2)
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()

window = Tk()
window.title("Typing Speed Test")
window.config(padx=100, pady=100)

tittle_label = Label(text="Typing Speed Test")
tittle_label.grid(column=1, row=0)

canvas = Canvas(width=100, height=100, highlightthickness=0)
timer_text = canvas.create_text(
    50, 50, text="00:00", fill='green', font=('sans-serif', 20, "bold"))
canvas.grid(column=1, row=1)

start_button = Button(text="Start", command=start_timer, highlightthickness=0)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_button.grid(column=2, row=2)

# ------------- END OF TIMER ------------

window.mainloop()