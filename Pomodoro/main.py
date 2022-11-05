from tkinter import * 
import math

# ---------------------------- CONSTANTS -----------------------------#
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# --------------------------- TIMER RESET -------------------------#
def reset_timer():
    #This stops the after function
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    timer_label.config(text="Timer")
    check_label.config(text="")
    #This reset reps so that the timer starts from the first session again
    global reps
    reps = 0


# -----------------------TIMER MECHANISM --------------------------#
def start_timer():
    global reps
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    reps += 1

    if reps % 2 != 0:
        #worktime
        timer_label.config(text="Work", fg="GREEN")
        count_down(work_sec)
    elif reps == 8:
        timer_label.config(text="Long_Break", fg="RED")
        count_down(long_break_sec)
    else:
        timer_label.config(text="Break", fg="PINK")
        count_down(short_break_sec)

# ----------------------- COUNTDOWN MECHANISM ------------------------#
def count_down(count):
    # "01:35"
    #math.floor removes the decimal points and returns the interger
    count_min = math.floor(count/60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    
    if count_min < 10:
        count_min = f"0{count_min}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        #after(time in seconds to wait, function to run , argument of function action)
        timer = window.after(1000, count_down, count-1)
    else:
        start_timer()
        mark=""
        #2 reps are one complete work session
        work_sessions = math.floor(reps/2)
        #This will always loop the number of work sessions and add marks to the empty mark variable
        for _ in range(work_sessions):
            mark += "✔"
        check_label.config(text=mark)

#------------------------- UI SETUP ---------------------------------#
window = Tk()
window.title("Pomodoro")
window.config(padx=50, pady=50, bg=YELLOW)

#highlighthickness takes away the line on the edge of the tomato image
canvas = Canvas(width= 200, height=224, bg=YELLOW, highlightthickness=0)
#photo to be added to the canvas using PhotoImage class
veg_img = PhotoImage(file="Pomodoro\Tomato.png")
#use methods create_image() and create_text() to add text and image to canvas
canvas.create_image(100, 112, image=veg_img)
#change somthingin the canvas you must use itemconfig on a variable that contains element of canvas
timer_text = canvas.create_text(103, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column = 1)

#The fg changes the color of the text of the label 
timer_label = Label(text="Timer", font=(FONT_NAME, 40, "bold"), fg=GREEN, bg=YELLOW)
timer_label.grid(row=0, column=1)

#This starts with no text to recieve check marks after a work session
check_label = Label(fg=GREEN, bg=YELLOW)
check_label.grid(row=3, column=1)

#This button starts the clock/count down 
start_button = Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(row=2, column=0)

#This resets the clock of the GUI
reset_button = Button(text="Reset",  highlightthickness=0, command=reset_timer)
reset_button.grid(row=2, column=2)

window.mainloop()