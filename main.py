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
reps = 0
marks="✔️"
stop_start=None

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")


w = window.winfo_screenwidth()
h = window.winfo_screenheight()
window.config(pady=0.1*h,padx=0.05*w,bg=YELLOW)

l1=Label(text="Pomodoro Timer",fg=GREEN,font=(FONT_NAME,35,"bold"),bg=YELLOW)
l1.grid(row=0,column=1)

canvas = Canvas(width=200,height=224,bg=YELLOW,highlightthickness=0)
tomato=PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato)
a=canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME,35,"bold"))


def counting(count):
    global stop_start
    if count>=0:
        sec=count%60
        if sec<10:
            sec=f"0{sec}"
        min = count//60
        if min<10:
            min=f"0{min}"
        canvas.itemconfig(a, text=f"{min}:{sec}")
        stop_start=window.after(1000, counting,count-1)
    else:
        timer()




def timer():
    global reps
    global marks
    reps += 1
    work = WORK_MIN*60
    short = SHORT_BREAK_MIN*60
    long = LONG_BREAK_MIN*60
    if reps==8:
        counting(long)
        l1.config(text='Break',fg=RED)
        l2.config(text=marks)
    elif reps%2==0:
        counting(short)
        l1.config(text='Break', fg=PINK)
        l2.config(text=marks)
        marks+="✔️"
    else:
        counting(work)
        l1.config(text='Work', fg=GREEN)


def resett():
    global reps
    reps=0
    window.after_cancel(stop_start)
    l1.config(text="Pomodoro Timer",fg=GREEN)
    l2.config(text="")
    canvas.itemconfig(a, text="00:00")



canvas.grid(row=1, column=1)
start = Button(text="Start",highlightthickness=0,command=timer)
start.grid(row=2,column=0)

l2=Label(text="",fg=GREEN,bg=YELLOW)
l2.grid(row=2,column=1)

reset = Button(text="Reset",highlightthickness=0,command=resett)
reset.grid(row=2,column=2)
window.mainloop()


