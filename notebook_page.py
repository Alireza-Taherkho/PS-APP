
from tkinter import *
from tkinter import messagebox, Toplevel, ttk
import sqlite3




def create_connection():
    conn = sqlite3.connect('ps_notebook.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS ps_nb(id INTEGER PRIMARY KEY AUTOINCREMENT, name_ TEXT, phone TEXT, description TEXT)''')
    conn.commit()
    conn.close()

create_connection()


def insert_info(Name, Description, Phone_Number='_'):
    if Phone_Number == '' or Phone_Number == None or Phone_Number == False or Phone_Number == ' ':
        Phone_Number = '_'
    conn = sqlite3.connect('ps_notebook.db')
    c = conn.cursor()
    c.execute('INSERT INTO ps_nb VALUES(null,?,?,?)', (Name, Phone_Number, Description))
    conn.commit()
    conn.close()

def delete_r(id):
    conn = sqlite3.connect('ps_notebook.db')
    c = conn.cursor()
    c.execute('DELETE FROM ps_nb WHERE id=?', (id,))
    conn.commit()
    conn.close()


def show():
    conn = sqlite3.connect('ps_notebook.db')
    c = conn.cursor()
    c.execute('SELECT * FROM ps_nb ORDER BY id DESC')
    rows = c.fetchall()
    conn.close()
    return rows

def update_r(id, Name, Description, Phone_Number):
    conn = sqlite3.connect('ps_notebook.db')
    c = conn.cursor()
    c.execute('UPDATE ps_nb SET name_=?, phone=? , description=? WHERE id=?', (Name, Phone_Number, Description,id))
    conn.commit()
    conn.close()


def note_book_window():
    nb = Toplevel()
    nb.geometry('1040x505')
    nb.resizable(False, False)
    nb.title('NoteBook')
    nb.configure(bg='#ECEBDE')

    style = ttk.Style(nb)
    style.configure("Custom.Treeview", font=('Arial', 12))
    style.configure('Custom.Treeview.Heading', font=('Arial', 13))

    # -------------------list box-----------------------------

    def get_selection(event):
        global row
        selected_item = nb_list.selection()
        if selected_item:
            row = nb_list.item(selected_item[0], 'values')

    nb_list = ttk.Treeview(nb, columns=( 'Description', 'Phone', 'Name', 'id'),show='headings', style='Custom.Treeview', height=18)

    nb_list.heading('Description', text='توضیحات')
    nb_list.heading('Phone', text='شماره تلفن')
    nb_list.heading('Name', text='نام و نام خانوادگی')
    nb_list.heading('id', text='#')

    nb_list.column('Description', width=10, anchor='center')
    nb_list.column('Phone', width=10, anchor='center')
    nb_list.column('Name', width=10, anchor='center')
    nb_list.column('id', width=10, anchor='center')

    nb_list.bind('<<TreeviewSelect>>', get_selection)
    nb_list.place(x=18, y=15, width=973, height=350)

    history_scrol = ttk.Scrollbar(nb, orient=VERTICAL, command=nb_list.yview)
    nb_list.configure(yscrollcommand=history_scrol.set)
    history_scrol.place(x=1000, y=15, width=20, height=350)

    nb_list.tag_configure('evenrow', background='#b0b0b0')
    nb_list.tag_configure('oddrow', background='#e8e8e8')


    def clear_list():
        for i in nb_list.get_children():
            nb_list.delete(i)

    def view():
        clear_list()
        table = show()

        list_info = []
        list_index = []
        index_num = 0
        for i in table:
            list_index.append(index_num)
            list_info.append(i)
            index_num += 1

        for index, info in list(zip(list_index, list_info)):
            if index % 2 == 0:
                nb_list.insert('', END, values=(info[3],info[2],info[1],info[0]), tags=('evenrow',))
            if index % 2 != 0:
                nb_list.insert('', END, values=(info[3],info[2],info[1],info[0]), tags=('oddrow',))

    view()


    btn1 = Button(nb, text='ایجاد یاداشت', bg='#5A6C57',fg='white', borderwidth=4 ,font=('Arial', 15, 'bold'),cursor='hand2', command= lambda :insert_btn())
    btn1.place(x=890, y=380, width=100, height=30)

    def insert_btn():
        insert_info(name.get(), desc.get(), phone.get())
        view()
        name.set('')
        desc.set('')
        phone.set('')


    btn2 = Button(nb, text='بروز رسانی', bg='#5A6C57',fg='white', borderwidth=4 ,font=('Arial', 15, 'bold'),cursor='hand2', command= lambda : update_btn())
    btn2.place(x=770, y=380, width=100, height=30)

    def update_btn():
        global row
        l = []
        listnum = [2, 1, 0]
        n = 0
        val_list = [name.get(), phone.get(), desc.get()]
        for i in range(len(val_list)):
            if val_list[i] == 0 or val_list[i] == '' or val_list[i] == '0' and i != 2:
                l.append(row[listnum[n]])
            else:
                l.append(val_list[i])
            n += 1

        update_r(row[3], l[0], l[2], l[1])
        view()
        name.set('')
        phone.set('')
        desc.set('')

        try:
            row = list(row)
            row[3] = 0
        except NameError:
            pass




    btn3 = Button(nb, text='حذف کردن', bg='#cc5959',fg='white', borderwidth=4 ,font=('Arial', 15, 'bold'),cursor='hand2', command= lambda: delete_btn())
    btn3.place(x=18, y=380, width=100, height=30)

    def delete_btn():
        result = messagebox.askquestion('.؟.', 'آیا میخواهید این یاداشت را حذف کنید؟')
        if result == 'yes':
            try:
                delete_r(row[3])
            except NameError:
                messagebox.showerror('ارور', 'موردی انتخاب نشده است')
            view()

#----------------------------labels and entries------------------------------

    lbl1 = Label(nb, text='نام و نام خانوادگی', fg='black', bg='#ECEBDE', font=('Arial', 13, 'bold'))
    lbl1.place(x=847, y=430, width=140, height=30)

    lbl2 = Label(nb, text='شماره تلفن', width=8, bg='#ECEBDE', fg='black', font=('Arial', 13, 'bold'))
    lbl2.place(x=688, y=430, width=100, height=30)

    lbl3 = Label(nb, text='توضیحات', width=8, bg='#ECEBDE', fg='black', font=('Arial', 13, 'bold'))
    lbl3.place(x=407, y=430, width=100, height=30)

    name = StringVar()
    en1 = Entry(nb, textvariable=name, font=('Arial', 13, 'bold'), cursor='hand2', bg='white', fg='#000000', justify='center')
    en1.place(x=842, y=460, width=150, height=30)

    phone = StringVar()
    en2 = Entry(nb, textvariable=phone, font=('Arial', 13, 'bold'), cursor='hand2', bg='white', fg='#000000', justify='center')
    en2.place(x=657, y=460, width=150, height=30)

    desc = StringVar()
    en3 = Entry(nb, textvariable=desc, font=('Arial', 13, 'bold'), cursor='hand2', bg='white', fg='#000000', justify='center')
    en3.place(x=287, y=460, width=330, height=30)

    nb.mainloop()

