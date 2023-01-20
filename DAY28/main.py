from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps=0
timing = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timing)
    canvas.itemconfig(timer_text, text="00:00")
    #timer_text.config(text="00:00") (X)
    timer.config(text="Timer")
    check.config(text="")
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps+=1

    work_min = WORK_MIN * 60
    short_break_sec= SHORT_BREAK_MIN * 60
    long_break_min = LONG_BREAK_MIN * 60


    if reps%8==0:
        count_down(long_break_min)
        timer.config(text="Break", fg=RED)
    elif reps%2==1:
        count_down(work_min)
        timer.config(text="Work", fg=GREEN)
    else:
        count_down(short_break_sec)
        timer.config(text="Break", fg=PINK)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(count):

    count_min = math.floor(count/60)
    count_sec = count % 60
    if count_sec<10:
        #count_sec = '0'+str(count_sec)
        count_sec =f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count>0 :
        global timing
        timing = window.after(1000, count_down, count - 1)
    else:
        start_timer() # 주의
        marks = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            marks += "💮"
        check.config(text=marks)

# ---------------------------- UI SETUP -------------------------------
window = Tk()
window.title("Pomodoro")
window.config(padx=30, pady=10,bg=YELLOW)


canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")

canvas.create_image(100,112,image=tomato_img)
timer_text = canvas.create_text(100,130,text="00:00", fill="white",font=(FONT_NAME,35,"bold"))
canvas.grid(row=1,column=1)


# Label
timer = Label(text = "Timer", font=(FONT_NAME,40,"bold"),fg=GREEN,bg=YELLOW,)
timer.grid(row=0, column=1)

check = Label(fg=RED, bg=YELLOW)
check.grid(row=3, column=1)
# Button

start = Button(text="Start", highlightthickness=0, command=start_timer)
start.grid(row=2, column=0)

reset = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset.grid(row=2, column=2)




window.mainloop()


# Canvas
# -> tkinter의 캔버스 위젯 : 다른 것들 위에다가 층층 쌓기
# 토마토 그림 위에다가 텍스트
# PhotoImage
# canvas.create_image
# canvas.create_text
# window.after
# canvas.itemconfig
# window.after_cancel

