
from tkinter import *
from tkinter import messagebox, Toplevel, ttk
import sqlite3
import funcs
#----------------------------------------------------------------------------------

def create_connection():
    conn = sqlite3.connect('Financial_information.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS FI_ps(id INTEGER PRIMARY KEY AUTOINCREMENT,
    device_name TEXT,
    one_user INTEGER,
    two_user INTEGER,
    three_user INTEGER,
    four_user INTEGER,
    per_minute INTEGER
    )''')
    conn.commit()
    conn.close()
create_connection()

def add_type_of_device(Name, One_user, Two_user, Three_user, Four_user, Per_minute):
    conn = sqlite3.connect('Financial_information.db')
    c = conn.cursor()
    c.execute('INSERT INTO FI_ps VALUES(null,?,?,?,?,?,?)', (Name, One_user, Two_user, Three_user, Four_user, Per_minute))
    conn.commit()
    conn.close()


def delete_r(id):
    conn = sqlite3.connect('Financial_information.db')
    c = conn.cursor()
    c.execute('DELETE FROM FI_ps WHERE id=?', (id,))
    conn.commit()
    conn.close()


def update_r(id, Name, One_user, Two_user, Three_user, Four_user, Per_minute):
    conn = sqlite3.connect('Financial_information.db')
    c = conn.cursor()
    c.execute('UPDATE FI_ps SET device_name=?, one_user=? , two_user=?, three_user=?, four_user=?, per_minute=? WHERE id=?', (Name,One_user,Two_user,Three_user,Four_user,Per_minute,id))
    conn.commit()
    conn.close()


def show_prices():
    conn = sqlite3.connect('Financial_information.db')
    c = conn.cursor()
    c.execute('SELECT * FROM FI_ps ORDER BY id DESC')
    rows = c.fetchall()
    conn.close()
    return rows

def select_info(Name):
    conn = sqlite3.connect('Financial_information.db')
    c = conn.cursor()
    c.execute('SELECT One_user, Two_user, Three_user, Four_user, Per_minute FROM FI_ps WHERE device_name=?', (Name,))
    rows = c.fetchall()
    conn.close()
    return rows[0]

#-------------------------------------------------------------------------------------------------------------------------

def Financial_information_window():
    FI = Toplevel()
    FI.geometry('1000x355')
    FI.resizable(False, False)
    FI.title('Financial information')
    FI.configure(bg='#ECEBDE')

    style = ttk.Style(FI)
    style.configure("Custom.Treeview", font=('Arial', 12))
    style.configure('Custom.Treeview.Heading', font=('Arial', 13))
    #------------------------------------------------------------------------------------------------

    frame1 = Frame(FI, borderwidth=5, relief='groove', bg='#ECEBDE', highlightcolor='green')
    frame1.place(x=10, y=13, width=980, height=329)

    label_price = Label(FI, text='اطلاعات مالی دستگاه ها', font=('Arial', 15, 'bold'), bg='#ECEBDE', fg='green')
    label_price.place(x=415, y=0, width=170)
    #------

    l1 = Label(FI, text=':تک دسته', font=('Arial', 15, 'bold'), width=7, bg='#ECEBDE', fg='black')
    l1.place(x=890, y=30)
    one = StringVar()
    e1 = Entry(FI, textvariable=one, font=('Arial', 13, 'bold'), cursor='hand2', bg='white', width=11, fg='#000000',justify='center')
    e1.place(x=770, y=30, height=30)

    l2 = Label(FI, text=':دو دسته', font=('Arial', 15, 'bold'), width=6, bg='#ECEBDE', fg='black')
    l2.place(x=650, y=30)
    two = StringVar()
    e2 = Entry(FI, textvariable=two, font=('Arial', 13, 'bold'), cursor='hand2', bg='white', width=11, fg='#000000',justify='center')
    e2.place(x=530, y=30, height=30)

    l3 = Label(FI, text=':سه دسته', font=('Arial', 15, 'bold'), width=6, bg='#ECEBDE', fg='black')
    l3.place(x=410, y=30)
    three = StringVar()
    e3 = Entry(FI, textvariable=three, font=('Arial', 13, 'bold'), cursor='hand2', bg='white', width=11, fg='#000000',justify='center')
    e3.place(x=290, y=30, height=30)

    l4 = Label(FI, text=':چهار دسته', font=('Arial', 15, 'bold'), width=6, bg='#ECEBDE', fg='black')
    l4.place(x=150, y=30)
    four = StringVar()
    e4 = Entry(FI, textvariable=four, font=('Arial', 13, 'bold'), cursor='hand2', bg='white', width=11, fg='#000000',justify='center')
    e4.place(x=30, y=30, height=30)
    #-------

    lname = Label(FI, text=':نام دستگاه', font=('Arial', 15, 'bold'), width=7, bg='#ECEBDE', fg='black')
    lname.place(x=890, y=80)
    name = StringVar()
    ename = Entry(FI, textvariable=name, font=('Arial', 13, 'bold'), cursor='hand2', bg='white', width=20, fg='#000000',
                  justify='center')
    ename.place(x=690, y=80, height=30)

    per_m = Label(FI, text=':به ازای هر چند دقیقه', font=('Arial', 15, 'bold'), width=15, bg='#ECEBDE', fg='black')
    per_m.place(x=396, y=80)
    min_p = StringVar()
    emin = Entry(FI, textvariable=min_p, font=('Arial', 13, 'bold'), cursor='hand2', bg='white', width=11, fg='#000000',
                 justify='center')
    emin.place(x=290, y=80, height=30)

    btn1 = Button(FI, text='ثبت اطلاعات', borderwidth=3, font=('Arial', 15, 'bold'), fg='#000000', cursor='hand2',bg='#9ABF80', command=lambda:sub_btn())
    btn1.place(x=30, y=80, height=34, width=102)

    def sub_btn():
        global row

        integer_sentence = '0123456789'
        for i , mark in [[one, 'int'], [two, 'int'], [three, 'int'], [four, 'int'], [name, 'str'], [min_p, 'int']]:
            i.get().strip()
            if i == '' or i == ' ' or i == 0:
                messagebox.showerror('.!.', 'تمامی مقادیر را باید پر کنید')
                return 'Error'

            if mark == 'int':
                for j in i.get():
                    if j not in integer_sentence:
                        messagebox.showerror('.!.', 'همه قسمت ها به غیر از قسمت نام باید عددی باشند و هیچ چیزی به غیر از اعداد صفر تا نه دریافت نمی کند')
                        return 'Error'

        funcs.show_entry([one, two, three, four])


        database_list = show_prices()
        for i in database_list:
            if i[1].lower() == name.get().strip().lower():
                messagebox.showerror('.!.', 'این دستگاه با این نام در دستگاه های شما وجود دارد')
                return 'Error'

        add_type_of_device(name.get(), one.get(), two.get(), three.get(), four.get(), min_p.get())
        l = [one, two, three, four, name, min_p]
        for i in range(len(l)):
                l[i].set('')

        row = -1
        view()

    #----------------------------------------------------------------------------------------------------------------------------------


    def get_selection(event):
        global row
        selected_item = FI_list.selection()
        if selected_item:
            row = FI_list.item(selected_item[0], 'values')

    FI_list = ttk.Treeview(FI, columns=('Per_minute','Four','Three', 'Two', 'One','Name', 'id'),show='headings', style='Custom.Treeview', height=18)

    FI_list.heading('Per_minute', text='به دقیقه')
    FI_list.heading('Four', text='چهار دسته')
    FI_list.heading('Three', text='سه دسته')
    FI_list.heading('Two', text='دو دسته')
    FI_list.heading('One', text='تک دسته')
    FI_list.heading('Name', text='نام')
    FI_list.heading('id', text='#')

    FI_list.column('Per_minute', width=10, anchor='center')
    FI_list.column('Four', width=10, anchor='center')
    FI_list.column('Three', width=10, anchor='center')
    FI_list.column('Two', width=10, anchor='center')
    FI_list.column('One', width=10, anchor='center')
    FI_list.column('Name', width=10, anchor='center')
    FI_list.column('id', width=10, anchor='center')

    FI_list.bind('<<TreeviewSelect>>', get_selection)
    FI_list.place(x=30, y=130, width=920, height=150)

    FI_scrol = ttk.Scrollbar(FI, orient=VERTICAL, command=FI_list.yview)
    FI_list.configure(yscrollcommand=FI_scrol.set)
    FI_scrol.place(x=960, y=130, width=15, height=150)

    FI_list.tag_configure('evenrow', background='#b0b0b0')
    FI_list.tag_configure('oddrow', background='#e8e8e8')


    def clear_list():
        for i in FI_list.get_children():
            FI_list.delete(i)

    def view():
        clear_list()
        table = show_prices()

        list_info = []
        list_index = []
        index_num = 0
        for i in table:
            list_index.append(index_num)
            list_info.append(i)
            index_num += 1

        for index, info in list(zip(list_index, list_info)):
            if index % 2 == 0:
                FI_list.insert('', END, values=(info[6],info[5],info[4],info[3],info[2],info[1],info[0]), tags=('evenrow',))
            if index % 2 != 0:
                FI_list.insert('', END, values=(info[6],info[5],info[4],info[3],info[2],info[1],info[0]), tags=('oddrow',))

    view()

    btn2 = Button(FI, text='حذف', borderwidth=3, font=('Arial', 15, 'bold'), fg='white', cursor='hand2',bg='#cc5959', command=lambda : dlt_row())
    btn2.place(x=30, y=290, height=34, width=102)

    def dlt_row():
        global row
        try:
            result = messagebox.askquestion('.?.', '؟آیا میخواهید این ردیف را حذف کنید')
            if result == 'yes':
                delete_r(row[6])
        except (NameError, TypeError):
            messagebox.showerror('ارور', 'موردی انتخاب نشده است')
        row = -1
        view()



    btn3 = Button(FI, text='ویرایش', borderwidth=3, font=('Arial', 15, 'bold'), fg='#EEEEEE', cursor='hand2', bg='#5A6C57', command=lambda: edit_table())
    btn3.place(x=848, y=290, height=34, width=102)

    def edit_table():
        global row

        integer_sentence = '0123456789'
        for i, mark in [[one, 'int'], [two, 'int'], [three, 'int'], [four, 'int'], [name, 'str'], [min_p, 'int']]:
            if i.get() == '' or i.get().isspace():
                i.set('');continue

            if mark == 'int':
                for j in i.get():
                    if j not in integer_sentence:
                        messagebox.showerror('.!.',
                                             'همه قسمت ها به غیر از قسمت نام باید عددی باشند و هیچ چیزی به غیر از اعداد صفر تا نه دریافت نمی کند')
                        return 'Error'

        funcs.show_entry([one, two, three, four])

        l = []
        listnum = [4, 3, 2, 1, 5, 0]
        n = 0
        val_list = [one.get(), two.get(), three.get(), four.get(), name.get(), min_p.get()]
        for i in range(len(val_list)):
            if type(i) == str:
                i = i.strip()

            if val_list[i] == 0 or val_list[i] == '' or val_list[i] == '0' or val_list[i] == ' ':
                l.append(row[listnum[n]])
            else:
                l.append(val_list[i])
            n += 1

        update_r(row[6], l[4], l[0], l[1], l[2], l[3], l[5])
        l = [one, two, three, four, name, min_p]
        for i in range(len(l)):
                l[i].set('')
        row = -1
        view()


    FI.mainloop()

