from tkinter import scrolledtext
from tkinter import ttk
import tkinter as tk
import webbrowser
import random

def seed(nseed='482649'):
    random.seed(int(nseed))
    letters = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и',
               'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т',
               'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь',
               'э', 'ю', 'я',
               'А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ё', 'Ж', 'З', 'И',
               'Й', 'К', 'Л', 'М', 'Н', 'О', 'П', 'Р', 'С', 'Т',
               'У', 'Ф', 'Х', 'Ц', 'Ч', 'Ш', 'Щ', 'Ъ', 'Ы', 'Ь',
               'Э', 'Ю', 'Я',
               'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
               'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
               'u', 'v', 'w', 'x', 'y', 'z',
               'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
               'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
               'U', 'V', 'W', 'X', 'Y', 'Z',
               ' ', '0', '1', '2', '3', '4', '5', '6', '7', '8',
               '9',
               ',', '.', '!', '?', '(', ')', '[', ']', '<', '>',
               '№', '~', '"', "'", '`', '-', '@', '#', '$', '%',
               '^', '&', '*', '_', '+', '=', ';', ':', '/', '|',
               '\\']
    
    for i in range(random.randint(10, 100)):
        random.shuffle(letters)
    d = {i : letters[i-10] for i in range(10, len(letters)+10)}
    items = d.items()
    return items

def zashifr(text, items): 
    shifr = ''
    for letter in range(len(text)):
        for j in items:
            if text[letter] == j[1]:
                kod = ''
                a = j[0]

                
                for i in range(20):
                    c = a/(20-i)
                    if a > 9:
                        b = round(c)
                    else: b = a
                    a -= b
                    kod += str(b)

                kodrand = list(kod)
                random.shuffle(kodrand)
                shifr += ''.join(kodrand)
                break
    return shifr

def razshifr(shifr, items):
    text = """"""
    kods = []
    kod = []
    for i in range(len(shifr)):
        number = shifr[i]
        kod += [number]
        if len(kod) == 20:
            kods += [kod]
            kod = []

    for k in range(len(kods)):
        a = 0
        for i in kods[k]:
            a += int(i)
            
        for i in items:
            if a == i[0]:
                text += i[1]
                break
    return text


#root

root = tk.Tk()
root["bg"] = "#fffaf2"
root.title("Шифратор")

w = root.winfo_screenwidth()
h = root.winfo_screenheight()
w = w//2
h = h//2 
w = w - 300 - 30
h = h - 250 - 20
root.geometry('600x500+{}+{}'.format(w, h))
root.resizable(False, False)

style = ttk.Style()

style.theme_create( "yummy", parent="alt", settings={
        "TNotebook": {"configure": {"tabmargins": [2, 5, 2, 0] } },
        "TNotebook.Tab": {
            "configure": {"padding": [5, 1], "background": '#ffe0f9' },
            "map":       {"background": [("selected", '#f5ceed')],
                          "expand": [("selected", [1, 1, 1, 0])] } } } )

style.theme_use("yummy")

tab_control = tk.ttk.Notebook(root)
ttk.Style().configure("TNotebook", background= '#f7feff')
tab1 = tk.ttk.Frame(tab_control)
tab2 = tk.ttk.Frame(tab_control)
ttk.Style().configure("TFrame", background= '#fffaf2')
tab_control.add(tab1, text='  Зашифровать  ')  
tab_control.add(tab2, text='  Расшифровать  ')

#ssilka

def callback(event):
    webbrowser.open_new(event.widget.cget("text"))

lb = tk.Label(root, text = 'Связь:', bg = "#f7feff")
lb.place(x = 400, y = 3)

lbl = tk.Label(root, text=r"https://vk.com/griffin_john", bg = "#f7feff", fg="#d05f8b", cursor="hand2")
lbl.place(x = 440, y = 3)
lbl.bind("<Button-1>", callback)

#zashifr

def clicked_zashifr():
    #Сначала шифрует на рандомном сиде
    nseed = random.randint(100000, 999999)
    text = zashifr(txt_zashifr.get(1.0, tk.END), seed(nseed))
    txt_zashifr.delete(1.0, tk.END)
    #Потом расшифровывает на сиде * 10 и добавляет в начало номер сида
    text = str(nseed) + ' ' + razshifr(text, seed(nseed*10))
    root.clipboard_clear()
    root.clipboard_append(text)

txt_zashifr = scrolledtext.ScrolledText(tab1, font=("Arial Bold", 14), bg = '#f7ffff', fg = 'black', selectbackground = '#ffc080', selectforeground = 'black', wrap = tk.WORD)  
txt_zashifr.place(x = 10, y = 80, width = 590, height = 375)
txt_zashifr.focus()

btn_zashifr = tk.Button(tab1, font=("Arial bold", 15), text="Зашифровать и скопировать в буфер обмена", bg="black", fg="#f5a2e4", cursor="hand2",
                        activebackground = 'black', activeforeground = '#e87bd2', command=clicked_zashifr)
btn_zashifr.place(x = 77, y = 30, width = 440, height = 40)

#razshifr

def clicked_razshifr():
    #Определяет сид и зашифровывает на сиде * 10
    try:
        nseed = int(root.clipboard_get()[0:6])
    except:
        return
    txt = root.clipboard_get()[7::]
    text = zashifr(txt, seed(nseed*10))
    #Расшифровывает на сиде
    text = razshifr(text, seed(nseed))
    txt_razshifr.delete(1.0, tk.END)
    txt_razshifr.insert(tk.INSERT, text)

txt_razshifr = scrolledtext.ScrolledText(tab2, font=("Arial Bold", 14), bg = '#f7ffff', fg = 'black', selectbackground = '#ffc080', selectforeground = 'black', wrap = tk.WORD)   
txt_razshifr.place(x = 10, y = 80, width = 590, height = 375)
txt_razshifr.focus()

btn_razshifr = tk.Button(tab2, font=("Arial bold", 15), text="Расшифровать текст из буфера обмена", bg="black", fg="#f5a2e4", cursor="hand2",
                        activebackground = 'black', activeforeground = '#e87bd2', command=clicked_razshifr)
btn_razshifr.place(x = 77, y = 30, width = 440, height = 40)

#The end

tab_control.pack(expand=1, fill='both')
root.mainloop()

