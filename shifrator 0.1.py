from tkinter import *
import random

def seed(seed=4826493):
    if seed.isnumeric() == False:
        seed = 4826493
    random.seed(seed) 
    letters = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п',
               'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я', ' ',
               '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ',', '.', '!', '?', '-', '(', ')',
               'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q',
               'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
               '', '', '', '', '', '', '', '', '', '', '', '', '', '']
    while letters[0] != '':
        random.shuffle(letters)
    d = {i : letters[i] for i in range(len(letters))}
    items = d.items()
    return items

def zashifr(text, items):
    shifr = ''
    for letter in text:
        for j in items:
            if letter.lower() == j[1]:
                kod = ''
                a = j[0]
                
                for i in range(10):
                    c = a/(10-i)
                    if a > 9:
                        b = round(c)
                    else: b = a
                    
                    if letter.isupper() and i==0:
                        if b%2 != 0:
                            b -= 1
                    elif letter.islower() and i==0:
                        if a > 9:
                            if b%2 == 0:
                                b +=1
                        else:
                            b=(a//2)
                            if b%2==0:
                                b+=1
                    a -= b
                    kod += str(b)

                kodrand = list(kod)[1::]
                random.shuffle(kodrand)
                
                shifr += kod[0]
                shifr += ''.join(kodrand)
                break
    return shifr

def razshifr(shifr, items):
    text = ''
    kods = []
    kod = []
    for i in range(len(shifr)):
        number = shifr[i]
        kod += [number]
        if len(kod) == 10:
            kods += [kod]
            kod = []

    for kod in kods:
        a = 0
        for i in kod:
            a += int(i)
            
        for i in items:
            if a == i[0]:
                if int(kod[0])%2 == 0:
                    text += i[1].upper()
                else:
                    text += i[1]
                break
    return text


while True:
    window = Tk()
    window.title("Шифратор")
    window.geometry("1200x400")

    #seed

    def clicked_seed():
        lb_seed.configure(text = vvod_seed.get())
        if lb_seed['text'] == '666':
            lb_seed.configure(bg='Black', fg='red')
        elif lb_seed['text'].isnumeric():
            if int(lb_seed['text'])%111 == 0:
                lb_seed.configure(bg='blue', fg='white')
        else:
            lb_seed.configure(bg='White', fg='Black')

    def clicked_seed_umolch():
        lb_seed.configure(text = "???")
        lb_seed.configure(bg='White', fg='Black')
        print(lb_seed['text'])
        
    lb_seed = Label(window, font=("Arial bold", 15), text="???", bg='white', fg='black')
    lb_seed.grid(column = 0, row = 0)

    btn_seed = Button(window, font=("Arial bold", 15), text=" Установить сид", bg="black", fg="orange", command=clicked_seed)
    btn_seed.grid(column = 2, row = 0)

    btn_seed_umolch = Button(window, font=("Arial bold", 15), text=" Установить сид по умолчанию", bg="black", fg="orange", command=clicked_seed_umolch)
    btn_seed_umolch.grid(column = 3, row = 0)

    vvod_seed = Entry(window, width=30)
    vvod_seed.grid(column=1, row=0)

    #zashifr

    def clicked_zashifr():
        nseed = lb_seed['text']
        txt = zashifr(vvod_zashifr.get(), seed(nseed))
        lb_zashifr.configure(text = txt)

    def clicked_zashifr_bufer_v():
        vvod_zashifr.delete(0, END)
        vvod_zashifr.insert(0, window.clipboard_get())

    def clicked_zashifr_bufer_s():
        window.clipboard_clear()
        window.clipboard_append(lb_zashifr['text'])
        
    lb_zashifr = Label(window, font=("Arial bold", 10), text="", bg='white', fg='black')
    lb_zashifr.grid(column=0, row=3)

    btn_zashifr = Button(window, font=("Arial bold", 15), text=" Зашифровать", bg="black", fg="orange", command=clicked_zashifr)
    btn_zashifr.grid(column = 0, row = 1)

    vvod_zashifr = Entry(window, width=20)
    vvod_zashifr.grid(column=0, row=2)

    btn_zashifr_bufer_v = Button(window, font=("Arial bold", 15), text=" Вставить текст из буфера обмена", bg="black", fg="orange", command=clicked_zashifr_bufer_v)
    btn_zashifr_bufer_v.grid(column = 2, row = 1)

    btn_zashifr_bufer_s = Button(window, font=("Arial bold", 15), text=" Скопировать шифр в буфер обмена", bg="black", fg="orange", command=clicked_zashifr_bufer_s)
    btn_zashifr_bufer_s.grid(column = 1, row = 1)

    #razshifr

    def clicked_razshifr():
        nseed = lb_seed['text']
        txt = razshifr(vvod_razshifr.get(), seed(nseed))
        lb_razshifr.configure(text = txt)

    def clicked_razshifr_bufer_v():
        vvod_razshifr.delete(0, END)
        vvod_razshifr.insert(0, window.clipboard_get())

    def clicked_razshifr_bufer_s():
        window.clipboard_clear()
        window.clipboard_append(lb_razshifr['text'])

    lb_razshifr = Label(window, font=("Arial bold", 10), text="", bg='white', fg='black')
    lb_razshifr.grid(column=0, row=6)

    btn_razshifr = Button(window, font=("Arial bold", 15), text=" Расшифровать", bg="black", fg="orange", command=clicked_razshifr)
    btn_razshifr.grid(column = 0, row = 4)

    vvod_razshifr = Entry(window, width=20)
    vvod_razshifr.grid(column=0, row=5)

    btn_razshifr_bufer_v = Button(window, font=("Arial bold", 15), text=" Вставить шифр из буфера обмена", bg="black", fg="orange", command=clicked_razshifr_bufer_v)
    btn_razshifr_bufer_v.grid(column = 1, row = 4)

    btn_razshifr_bufer_s = Button(window, font=("Arial bold", 15), text=" Скопировать текст в буфер обмена", bg="black", fg="orange", command=clicked_razshifr_bufer_s)
    btn_razshifr_bufer_s.grid(column = 2, row = 4)



    window.mainloop()
