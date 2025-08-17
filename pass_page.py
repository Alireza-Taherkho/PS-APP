from tkinter import *
from tkinter import messagebox, Toplevel
import sqlite3
import history_page
import FI_Page
import devices


def create_connection():
    conn = sqlite3.connect('ps_kk.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS ps_pass(id INTEGER PRIMARY KEY AUTOINCREMENT, password TEXT)''')
    conn.commit()
    conn.close()

create_connection()


def insert_pass(password):
    conn = sqlite3.connect('ps_kk.db')
    c = conn.cursor()
    c.execute('INSERT INTO ps_pass VALUES (null,?)', (password,))
    conn.commit()
    conn.close()


def select_pass():
    conn = sqlite3.connect('ps_kk.db')
    c = conn.cursor()
    c.execute('SELECT password FROM ps_pass')
    passwords = c.fetchall()
    conn.close()
    return passwords


def pass_window(func):
    password = select_pass()

    pas = Toplevel()
    pas.geometry('550x200')
    pas.resizable(False, False)
    pas.title('Password')
    pas.configure(bg='#ECEBDE')

    label1 = Label(pas, text='رمز را وارد کنید', bg='#ECEBDE', font=('Arial', 25, 'bold'))
    label1.place(x=175, y=10, width=200, height=50)

    check_pas = StringVar()
    entry1 = Entry(pas, font=('Arial', 20, 'bold'), textvariable=check_pas, bg='white', width=30, show='*', justify='center')
    entry1.place(x=47, y=80)

    button1 = Button(pas, text='تایید', font=('Arial', 16, 'bold'), bg='green', width=10, activebackground='#9ABF80',cursor='hand2', command=lambda: recognise_pas())
    button1.place(x=47, y=150)

    button1 = Button(pas, text='ایجاد رمز', font=('Arial', 13, 'bold'), bg='orange', width=8,
                     activebackground='#ffbf76', cursor='hand2', command=lambda: creat_pass_page())
    button1.place(x=230, y=155)

    button3 = Button(pas, text='برگشت', font=('Arial', 16, 'bold'), bg='red', width=10, activebackground='#ff7676',cursor='hand2', command=lambda: pas.destroy())
    button3.place(x=360, y=150)

    if password == []:
        messagebox.showinfo('...', '.به دلیل وجود نداشتن هیچ رمزی ابتدا یک رمز بسازید')

    def recognise_pas():
        try:
            if password[-1][0] != check_pas.get():
                messagebox.showerror('.!.', '!رمز اشتباه است')
            else:
                pas.destroy()
                if func == 'history':
                    history_page.history_window()
                elif func == 'devices':
                    devices.Device_window()
                elif func == 'FI_page':
                    FI_Page.Financial_information_window()

        except IndexError:
            messagebox.showerror('ارور','!هیچ رمزی وجود ندارد')

    def creat_pass_page():

        pas_creat = Toplevel()
        pas_creat.geometry('550x450')
        pas_creat.resizable(False, False)
        pas_creat.title('Creat Password')
        pas_creat.configure(bg='#ECEBDE')
        if password != []:
            label1 = Label(pas_creat, text='رمز قبلی را وارد کنید', bg='#ECEBDE', font=('Arial', 25, 'bold'))
            label1.place(x=130, y=10, width=300, height=50)

            old_pas = StringVar()
            entry1 = Entry(pas_creat, font=('Arial', 20, 'bold'), textvariable=old_pas, bg='white', width=30, show='*', justify='center')
            entry1.place(x=47, y=60)

        label2 = Label(pas_creat, text='رمز جدید را وارد کنید', bg='#ECEBDE', font=('Arial', 25, 'bold'))
        label2.place(x=130, y=130, width=300, height=50)

        new_pas = StringVar()
        entry2 = Entry(pas_creat, font=('Arial', 20, 'bold'), textvariable=new_pas, bg='white', width=30, show='*', justify='center')
        entry2.place(x=47, y=180)

        label3 = Label(pas_creat, text='رمز جدید را دوباره تکرار کنید', bg='#ECEBDE', font=('Arial', 25, 'bold'))
        label3.place(x=80, y=250, width=400, height=50)

        reapet_pas = StringVar()
        entry3 = Entry(pas_creat, font=('Arial', 20, 'bold'), textvariable=reapet_pas, bg='white', width=30, show='*', justify='center')
        entry3.place(x=47, y=300)

        button1 = Button(pas_creat, text='تایید', font=('Arial', 16, 'bold'), bg='green', width=10,
                         activebackground='#9ABF80', cursor='hand2', command=lambda: accept_btn(password))
        button1.place(x=47, y=400)

        button2 = Button(pas_creat, text='برگشت', font=('Arial', 16, 'bold'), bg='red', width=10,
                         activebackground='#ff7676', cursor='hand2', command=lambda: pas_creat.destroy())
        button2.place(x=360, y=400)

        def accept_btn(password):
            if password != []:
                password = password[-1][0]
                if password != old_pas.get():
                    messagebox.showerror('.!.', '!رمز اشتباه وارد شده است')
                    label1['fg'] = '#ff7676'
                    old_pas.set('')
                    return 'Error'
                else:
                    label1['fg'] = '#9ABF80'

            if new_pas.get() == '':
                messagebox.showerror('.!.','!هیچ چیزی دریافت نشد')
                return 'Error'
            if new_pas.get().isspace() == True:
                messagebox.showerror('.!.','!هیچ چیزی دریافت نشد')
                return 'Error'
            for i in '~`÷×!@#$%^&*()+={[]};:\'"|\\/*-<>,.?/ًٌٍ،؛َُِّۀآ«»ةيؤإأء':
                if i in new_pas.get():
                    messagebox.showerror('ارور','!از اشکال یا علامت ها استفاده نکنید به غیر از ( _ )')
                    return 'Error'
            for i in 'ضصثقفغعهخحجچشسیبلاتنمکگپظطزژرذدئو':
                if i in new_pas.get():
                    messagebox.showerror('ارور','!از حروف فارسی استفاده نکنید')
                    return 'Error'

            if new_pas.get() != reapet_pas.get():
                messagebox.showerror('.!.', '!رمز تکرار شده با رمز جدید مغایرت دارد')
                label3['fg'] = '#ff7676'
                reapet_pas.set('')
                return 'Error'
            else:
                insert_pass(new_pas.get())
                pas_creat.destroy()
                messagebox.showinfo('...','صفحه password را ببندید و دوباره آن را اجرا کنید')

        pas_creat.mainloop()

    pas.mainloop()











