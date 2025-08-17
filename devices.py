
from tkinter import *
from tkinter import messagebox, Toplevel, ttk
import sqlite3
import FI_Page



def create_connection():
    conn = sqlite3.connect('ps_number_of_device.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS ps_device(id INTEGER PRIMARY KEY AUTOINCREMENT, device TEXT, type_ TEXT)''')
    conn.commit()
    conn.close()

create_connection()


def select_device():
    conn = sqlite3.connect('ps_number_of_device.db')
    c = conn.cursor()
    c.execute('SELECT * FROM ps_device ORDER BY id DESC')
    devices = c.fetchall()
    conn.close()
    return devices

def select_type_of_device(device_name):
    conn = sqlite3.connect('ps_number_of_device.db')
    c = conn.cursor()
    c.execute('SELECT type_ FROM ps_device WHERE device=? ORDER BY id DESC', (device_name,))
    device_types = c.fetchall()
    conn.close()
    return device_types


def insert_device(Device, Type):
    conn = sqlite3.connect('ps_number_of_device.db')
    c = conn.cursor()
    c.execute('INSERT INTO ps_device VALUES (null,?,?)', (Device, Type))
    conn.commit()
    conn.close()


def delete_r(id):
    conn = sqlite3.connect('ps_number_of_device.db')
    c = conn.cursor()
    c.execute('DELETE FROM ps_device WHERE id=?', (id,))
    conn.commit()
    conn.close()


def update_r(id, Device, Type):
    conn = sqlite3.connect('ps_number_of_device.db')
    c = conn.cursor()
    c.execute('UPDATE ps_device SET device=? , type_=? WHERE id=?', (Device, Type,id))
    conn.commit()
    conn.close()



def Device_window():
    D = Toplevel()
    D.geometry('700x345')
    D.resizable(False, False)
    D.title('Device Manager')
    D.configure(bg='#ECEBDE')

    style = ttk.Style(D)
    style.configure("Custom.Treeview", font=('Arial', 12))
    style.configure('Custom.Treeview.Heading', font=('Arial', 13))
    #------------------------------------------------------------------------------------------------

    frame1 = Frame(D, borderwidth=5, relief='groove', bg='#ECEBDE', highlightcolor='green')
    frame1.place(x=10, y=13, width=680, height=319)

    label_price = Label(D, text='دستگاه ها', font=('Arial', 15, 'bold'), bg='#ECEBDE', fg='green')
    label_price.place(x=570, y=0, width=80)
    #------

    lname = Label(D, text=':نام دستگاه', font=('Arial', 15, 'bold'), width=7, bg='#ECEBDE', fg='black')
    lname.place(x=565, y=30)
    name = StringVar()
    ename = Entry(D, textvariable=name, font=('Arial', 13, 'bold'), cursor='hand2', bg='white', width=17, fg='#000000',justify='center')
    ename.place(x=400, y=30, height=30)



    type_dev = Label(D, text=':نوع دستگاه', font=('Arial', 15, 'bold'), width=7, bg='#ECEBDE', fg='black')
    type_dev.place(x=210, y=30)

    def select_name_devices():
        name_list = []
        devices = FI_Page.show_prices()
        for i in devices:
            name_list.append(i[1])
        return name_list

    devices = select_name_devices()
    type_num = ttk.Combobox(D, values=devices, font=('Arial', 15, 'bold'), justify='center')
    type_num.place(x=30, y=30, width=170, height=30)

    btn1 = Button(D, text='ثبت اطلاعات', borderwidth=3, font=('Arial', 15, 'bold'), fg='#000000', cursor='hand2',bg='#9ABF80', command=lambda:sub_btn())
    btn1.place(x=290, y=70, height=34, width=102)

    def sub_btn():
        global row
        for i in [name, type_num]:
            i = i.get()
            if i == '' or i == ' ' or i == 0:
                messagebox.showerror('.!.', 'تمامی مقادیر را باید پر کنید')
                return 'Error'

        database_list = select_device()
        for i in database_list:
            if i[1].lower() == name.get().strip().lower():
                messagebox.showerror('.!.', 'این دستگاه با این نام در دستگاه های شما وجود دارد')
                return 'Error'


        devices = FI_Page.show_prices()
        device_match = False
        for i in devices:
            if i[1] == type_num.get():
                device_match = True

        if device_match == False:
            messagebox.showerror('.!.', '!نوع دستگاه ناشناخته است')
            return 'Error'


        insert_device(name.get(),type_num.get())
        l = [name, type_num]
        for i in range(len(l)):
            l[i].set('')
        row = -1
        view()



    #----------------------------------------------------------------------------------------------------------------------------------


    def get_selection(event):
        global row
        selected_item = D_list.selection()
        if selected_item:
            row = D_list.item(selected_item[0], 'values')

    D_list = ttk.Treeview(D, columns=('Type','Dev_Name', 'id'),show='headings', style='Custom.Treeview', height=18)

    D_list.heading('Type', text='نوع دستگاه')
    D_list.heading('Dev_Name', text='نام دستگاه')
    D_list.heading('id', text='#')


    D_list.column('Type', width=10, anchor='center')
    D_list.column('Dev_Name', width=10, anchor='center')
    D_list.column('id', width=10, anchor='center')

    D_list.bind('<<TreeviewSelect>>', get_selection)
    D_list.place(x=30, y=120, width=620, height=150)

    D_scrol = ttk.Scrollbar(D, orient=VERTICAL, command=D_list.yview)
    D_list.configure(yscrollcommand=D_scrol.set)
    D_scrol.place(x=660, y=120, width=15, height=150)

    D_list.tag_configure('evenrow', background='#b0b0b0')
    D_list.tag_configure('oddrow', background='#e8e8e8')


    def clear_list():
        for i in D_list.get_children():
            D_list.delete(i)

    def view():
        clear_list()
        table = select_device()

        list_info = []
        list_index = []
        index_num = 0
        for i in table:
            list_index.append(index_num)
            list_info.append(i)
            index_num += 1

        for index, info in list(zip(list_index, list_info)):
            if index % 2 == 0:
                D_list.insert('', END, values=(info[2],info[1],info[0]), tags=('evenrow',))
            if index % 2 != 0:
                D_list.insert('', END, values=(info[2],info[1],info[0]), tags=('oddrow',))

    view()

    btn2 = Button(D, text='حذف', borderwidth=3, font=('Arial', 15, 'bold'), fg='white', cursor='hand2',bg='#cc5959', command=lambda : dlt_row())
    btn2.place(x=30, y=280, height=34, width=102)

    def dlt_row():
        global row
        try:
            result = messagebox.askquestion('.?.', '؟آیا میخواهید این ردیف را حذف کنید')
            if result == 'yes':
                delete_r(row[2])
        except (NameError, TypeError):
            messagebox.showerror('ارور', 'موردی انتخاب نشده است')
        row = -1
        view()



    btn3 = Button(D, text='ویرایش', borderwidth=3, font=('Arial', 15, 'bold'), fg='#EEEEEE', cursor='hand2', bg='#5A6C57', command=lambda: edit_table())
    btn3.place(x=548, y=280, height=34, width=102)

    def edit_table():
        global row
        l = []
        listnum = [0, 1]
        n = 0
        val_list = [type_num.get(), name.get()]
        for i in range(len(val_list)):
            try:
                if val_list[i] == 0 or val_list[i] == '' or val_list[i] == '0' or val_list[i] == ' ':
                    l.append(row[listnum[n]])
                else:
                    l.append(val_list[i])
            except (TypeError, NameError):
                messagebox.showerror('.!.', 'هیچ موردی انتخاب نشده')
                return 'Error'
            n += 1

        update_r(row[2], l[1], l[0])
        l = [type_num, name]
        for i in range(len(l)):
            l[i].set('')
        row = -1
        view()
        row = list[row]
        row[2] = 0


    D.mainloop()




