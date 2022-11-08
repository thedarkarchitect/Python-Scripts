from tkinter import *
import pandas as pd
from random import *

BACKGROUND_COLOR = "#B1DDC6"
FONT = "Ariel"
current_card = {}
to_learn={}

try:
#This reads the csv data
    words = pd.read_csv("flasH Cards\data\words_to_learn.csv")
except FileNotFoundError:
    original_data = pd.read_csv("data/french_Words.csv")
    #This turns the csv into a dict that stores rows as dict in a list
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = words.to_dict(orient="records")


def is_known():
    #This is going to remove the card from the cards of list to learn
    to_learn.remove(current_card)
    #This turns the to_learn list to a dataframe of words that must be learned 
    data = pd.DataFrame(to_learn)
    #Index=False removes the dataframe index from the csv so they are not added when added to new csv 
    data.to_csv("flasH Cards\data\words_to_learn.csv", index=False)

    #This flips tp another word but without the card that user knows
    next_card()


def next_card():
    """Gets the french words from the csv"""
    #We need to change fills and bg color when method is called so that they change for user on next card
    global current_card, flip_timer
    #The timer is canceled when the function is called 
    window.after_cancel(flip_timer)
    current_card = choice(to_learn)
    canvas.itemconfig(lang, text="French", fill="black")
    canvas.itemconfig(trans, text=current_card['French'], fill="black")
    canvas.itemconfig(card, image=ft_card)

    #Every after we call the function on click we need to call after so that card changes cuz after only happens when window is created
    #but there is will be called every time the function is called
    #This will also let the timer start only when we land on a card we want to be revealed
    flip_timer = window.after(3000, func=flip_card)

def flip_card():
    """changes the cardfrom french to english"""
    #When method is called we need to change the fill of the canvas to another color
    canvas.itemconfig(lang, text="English", fill="white")
    canvas.itemconfig(trans, text=current_card['English'], fill="white")
    canvas.itemconfig(card, image=bk_card)
    
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)

ft_card = PhotoImage(file="flasH Cards\images\card_front.png")
bk_card = PhotoImage(file="flasH Cards\images\card_back.png")

card = canvas.create_image(400, 263, image=ft_card)
lang = canvas.create_text(400,150, text="", font=(FONT, 40, "italic"))
trans = canvas.create_text(400,263, text="", font=(FONT, 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

#Buttons
right_img = PhotoImage(file="flasH Cards\images\ght.png")
right_button = Button(image=right_img, command=is_known, highlightthickness=0)
right_button.grid(column=1, row=1)

wrong_img = PhotoImage(file="flasH Cards\images\wrong.png")
wrong_button = Button(image=wrong_img, command=next_card, highlightthickness=0)
wrong_button.grid(column=0, row=1)

next_card()

window.mainloop()