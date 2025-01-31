from tkinter import *
import pandas
from random import choice

BACKGROUND_COLOR = "#B1DDC6"
LANG_FONT = ("Ariel", 40, "italic")
WORD_FONT = ("Ariel", 10, "bold")



#Create window
window = Tk()
window.title("Wingspan")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

card_frame = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_frame.grid(row=0, column=0, columnspan=2)

lang_text = card_frame.create_text(400, 150, text="Bird - Bird in italic", fill="black", font=LANG_FONT)
word_text = card_frame.create_text(400, 263, text="Nosta 3 bonuskorttia ja hylkää sitten 2. Voit hylätä bonuskortteja, joita et ole nostanut tällä vuorolla.", fill="black", font=WORD_FONT)

window.mainloop()



'''
try:
    word_data = pandas.read_csv(".\\data\\words_to_learn.csv")
except FileNotFoundError:
    word_data = pandas.read_csv(".\\data\\kanji_data.csv")
word_list_to_learn = word_data.to_dict(orient="records")
flashcard = {}

# ---------------------------- SAVE PROGRESS ------------------------------- #

def word_known():
    word_list_to_learn.remove(flashcard)

    df = pandas.DataFrame(word_list_to_learn)
    df.to_csv(".\\data\\words_to_learn.csv", index=False)
    generate_word()


# ---------------------------- FLIP THE CARD ------------------------------- #

def flip_card():
    card_frame.itemconfig(card_photo, image = card_back)
    card_frame.itemconfig(lang_text, text="English", fill="white")
    card_frame.itemconfig(word_text, text=flashcard["English"], fill="white")

# ---------------------------- READ WORD FROM DATA ------------------------------- #

def generate_word():
    global flashcard, flip_timer
    window.after_cancel(flip_timer)
    flashcard = choice(word_list_to_learn)
    card_frame.itemconfig(card_photo, image=card_front)
    card_frame.itemconfig(lang_text, text=LANGUAGE, fill="black")
    card_frame.itemconfig(word_text, text=flashcard[LANGUAGE], fill="black")
    flip_timer = window.after(3000,flip_card)


# ---------------------------- UI SETUP ------------------------------- #

#Create window
window = Tk()
window.title("Flashcards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

# Create Flashcard-photo
card_frame = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front = PhotoImage(file=".\\images\\card_front.png")
card_back = PhotoImage(file=".\\images\\card_back.png")
card_photo = card_frame.create_image(400, 263, image=card_front)
card_frame.grid(row=0, column=0, columnspan=2)

lang_text = card_frame.create_text(400, 150, text=LANGUAGE, fill="black", font=LANG_FONT)
word_text = card_frame.create_text(400, 263, text="Word", fill="black", font=WORD_FONT)

# Create correct-button
correct_img = PhotoImage(file=".\\images\\right.png")
correct_answer = Button(image=correct_img, highlightthickness=0, borderwidth=0, command=word_known)
correct_answer.grid(row=1,column=0)

# Create incorrect-button

incorrect_img = PhotoImage(file=".\\images\\wrong.png")
incorrect_answer = Button(image=incorrect_img, highlightthickness=0, borderwidth=0, command=generate_word)
incorrect_answer.grid(row=1,column=1)

generate_word()


window.mainloop()
'''
