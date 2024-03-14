from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
# ___________________Picking French Words___________________________________#
to_learn = {} #создали пустой dict
current_card = {} #создали пустой dict

try: #пробуем
    data = pandas.read_csv("data/words_to_learn.csv") #читаем csv файл используя библиотеку pandas, которого может не быть
except FileNotFoundError: #если возникла ошибка файл не существует
    original_data = pandas.read_csv("data/french_words.csv") #если файла из секции try не существует, используем другой оригинальный файл
    to_learn = original_data.to_dict(orient="records") #в dict to learn записываем данные из оригинального csv файла,
                                                # records позволяет получить данные в виде листа с вложенными словарями
else: # если в секции try все нормально%
    to_learn = data.to_dict(orient="records") #в dict to learn записываем данные из файла в секции try csv файла,
                                                # records позволяет получить данные в виде листа с вложенными словарями

def next_card():
    global current_card, card_changer
    window.after_cancel(card_changer) #отменяем показ перевода, если была вызвана эта функция

    current_card = random.choice(to_learn) #выбираем случайную пару словаря из листа to learn

    canvas.delete("word")
    canvas.delete("title")

    canvas.create_image(410, 263, image=card_front_img)

    canvas.create_text(400, 263, text=current_card["French"], font=("Ariel", 60, "bold"), tags="word") #подставляем значение ключа French из словаря current_card
    canvas.create_text(400, 150, text="French", font=("Ariel", 40, "italic"), tags="title")
    card_changer = window.after(3000, switching_card) #запускаем показ перевода по новой, посредством вызова функции switching_card, которая меняет француское слово на английский перевод

def is_known():
    to_learn.remove(current_card) #удаляем словарь с парой Фрунцуский-Анлийский добавленную в строке 24
    print(len(to_learn))
    data = pandas.DataFrame(to_learn) #создаем объект pandas и записываем в переменную data
    data.to_csv("data/words_to_learn.csv", index=False) #создаем из переменной data новый csv words_to_learn, либо редактируем этот csv если он уже существовал

    next_card() #запускаем функцию next card чтобы программа выдала новое слово


def switching_card():
    canvas.create_image(410, 263, image=card_back_img)

    current_card = random.choice(to_learn) #выбираем случайную пару словаря из листа to learn

    canvas.delete("word")
    canvas.delete("title")

    canvas.create_text(400, 150, text="English", font=("Ariel", 40, "italic"), tags="title", fill="white") #
    canvas.create_text(400, 263, text=current_card["English"], font=("Ariel", 60, "bold"), tags="word", fill="white") #подставляем значение ключа English из словаря current_card


# __________________________________GUI SETTINGS______________________________________________#
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526)
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")

old_image = canvas.create_image(410, 263, image=card_front_img)#for French words

canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"), tags="title") #создаем канвасы без текста, потому что сразу вызывается функция next card которая подставляет слова в эти поля
canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"), tags="word")#создаем канвасы без текста, потому что сразу вызывается функция next card которая подставляет слова в эти поля

canvas.config(background=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

wrong = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong, highlightthickness=0, command=next_card)
wrong_button.grid(column=0, row=1)

right = PhotoImage(file="images/right.png")
right_button = Button(image=right, highlightthickness=0, command=is_known)
right_button.grid(column=1, row=1)

card_changer = window.after(3000, switching_card)
next_card() #вызываем функцию, которая подставит слово и язык в канвасы на строчке 67 и 68


window.mainloop()
