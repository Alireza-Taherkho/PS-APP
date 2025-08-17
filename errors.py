
from tkinter import messagebox


def desc_hand(val, entry_val=True):
    char = '÷×`~!@#$%^&()_<,>.?:;"\'\\{}[]qwertyuiopasdfghjklzxcvbnm«»ةيژؤإأءضصثقفغعهخحجچشسیبلاتنمکگپظطزرذدئوًٌٍ،؛َُِّۀآـ'
    tf = True
    if entry_val == False:
        value = val.lower().strip()
        for i in char:
            if i in value:
                tf = False
                return False, messagebox.showerror("ارور", "لطفا عدد وارد کنید")

        if tf == True:
            return True, True
    else:
        value = val.get()
        value = value.lower().strip()
        for i in char:
            if i in value:
                val.set('')
                tf = False
                return  False, messagebox.showerror("ارور", "لطفا عدد وارد کنید")

        if tf == True:
            return True, True



