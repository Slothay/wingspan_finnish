from tkinter import *
from tkinter import ttk
import pandas
from random import choice

BACKGROUND_COLOR = "#B1DDC6"
LANG_FONT = ("Ariel", 40, "italic")
WORD_FONT = ("Ariel", 20, "bold")

def on_birdbox(click):
    bird = click.widget.get()
    bird_index = birds.index(bird)
    description = finnish[bird_index]
    card_frame.itemconfig(lang_text, text = bird)
    card_frame.itemconfig(word_text, text = description)

def on_bonusbox(click):
    bonus = click.widget.get()
    bonus_index = bonus_name.index(bonus)
    description = finnish[bonus_index]
    card_frame.itemconfig(lang_text, text = bonus)
    card_frame.itemconfig(word_text, text = description)

bird_names = pandas.read_csv('Wingspan_birds.csv', encoding='cp1252', sep=';')
bonus_cards = pandas.read_csv('Wingspan_bonuscards.csv', encoding='cp1252', sep=';')
birds = []
finnish = []
bonus_name = []
bonus_finnish = []
for i in range(len(bird_names)):
    birds.append(bird_names.values[i][0])
    finnish.append(bird_names.values[i][3])

for i in range(len(bonus_cards)):
    bonus_name.append(bonus_cards.values[i][0])
    bonus_finnish.append(bonus_cards.values[i][2])

#Create window
window = Tk()
window.title("Wingspan")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

card_frame = Canvas(width=800, height=526, bg='white', highlightthickness=0)
card_frame.grid(row=0, column=0, columnspan=2)

lang_text = card_frame.create_text(400, 150, text="Bird - Bird in italic", fill="black", font=LANG_FONT)
word_text = card_frame.create_text(400, 263, text="Nosta 3 bonuskorttia ja hylkää sitten 2. Voit hylätä bonuskortteja, joita et ole nostanut tällä vuorolla.", width=800, fill="black", font=WORD_FONT)

bx = StringVar()
birdbox = ttk.Combobox(window, width=50, textvariable=bx)
birdbox['values'] = birds
birdbox.grid(row=1, column=0)

bo = StringVar()
bonusbox = ttk.Combobox(window, width=50, textvariable=bx)
bonusbox['values'] = bonus_name
bonusbox.grid(row=1, column=1)

birdbox.bind('<<ComboboxSelected>>', on_birdbox)
bonusbox.bind('<<ComboboxSelected>>', on_bonusbox)


window.mainloop()