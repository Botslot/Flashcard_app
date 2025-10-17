from tkinter import *
import pandas  as pd
from random import choice
BACKGROUND_COLOR = "#B1DDC6"

to_learn = {}
current_card = {}
try:
    data = pd.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pd.read_csv("data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")

# ---------------------------- Button click ------------------------------- #

def next_card():
    global flip_timer,current_card
    current_card = choice(to_learn)
    window.after_cancel(flip_timer)
    canvas.itemconfig(title,text="French",fill="black")
    canvas.itemconfig(word,text=current_card["French"],fill="black")
    canvas.itemconfig(card, image=front_image)
    flip_timer=window.after(3000, func=flip_card)

def flip_card():
    canvas.itemconfig(card,image=back_image)
    canvas.itemconfig(title,text="English",fill="white")
    canvas.itemconfig(word,text=current_card["English"],fill="white")

def is_known():
    to_learn.remove(current_card)
    data = pd.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv",index=False)
    next_card()



# ---------------------------- UI SETUP ------------------------------- #

window =Tk()
window.title("Flashy")
window.config(padx=50,pady=50,bg=BACKGROUND_COLOR)

flip_timer=window.after(3000, func=flip_card)

canvas = Canvas(width=800,height=526,bg=BACKGROUND_COLOR)
front_image = PhotoImage(file ="images/card_front.png")
back_image = PhotoImage(file="images/card_back.png")
card=canvas.create_image(400,263,image=front_image)
canvas.config(highlightthickness=0)
canvas.grid(row=0,column=0,columnspan=2)



title = canvas.create_text(400,150,text="",fill="black",font=("Ariel",40,"italic"))
word = canvas.create_text(400,263,text="",fill="black",font=("Ariel",60,"bold"))
cross_image = PhotoImage(file="images/wrong.png")
check_image = PhotoImage(file="./images/right.png")

unknown_button = Button(image=cross_image,highlightthickness=0,bd=0,activebackground=BACKGROUND_COLOR,command=next_card)
unknown_button.grid(row=1,column=0)

known_button = Button(image=check_image,highlightthickness=0,bd=0,activebackground=BACKGROUND_COLOR,command=is_known)
known_button.grid(row=1,column=1)





next_card()

window.mainloop()
