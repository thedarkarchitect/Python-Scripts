from tkinter import *


window = Tk()
window.title("Mile to Km Converter")

window.config(padx=20, pady=20)

def result():
    miles = mile_entry.get()
    km = int(miles) * 1.60934
    answer_L.config(text=f"{round(km, 2)}")


mile_entry = Entry(width = 10)
mile_entry.grid(row=0, column=1)

mile_label = Label(text="Miles")
mile_label.grid(row=0, column=2)


answer_L = Label(text = " 0 ")
answer_L.grid(row =1, column=1)

km_unit = Label(text="Km")
km_unit.grid(row=1, column=2)

sentence = Label(text="is equal to ")
sentence.grid(row=1, column=1)

cal_button = Button(text="Calculate", command= result)
cal_button.grid(row=2, column=1)

window.mainloop()