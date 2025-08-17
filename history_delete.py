from adodbapi import OperationalError
from tkinter import *
from tkinter import ttk, Toplevel, messagebox
import history_del_back



def delete_history_window():
    delete_page = Toplevel()
    delete_page.geometry('1050x525')
    delete_page.resizable(False, False)
    delete_page.title('Delete_History')
    delete_page.configure(bg='#ECEBDE')

    style = ttk.Style(delete_page)
    style.configure("Custom.Treeview", font=('Arial', 12))
    style.configure('Custom.Treeview.Heading', font=('Arial', 13))

#-------------------list box-----------------------------

    def get_selection(event):
        global row
        selected_item = history_list.selection()
        if selected_item:
            row = history_list.item(selected_item[0],'values')



    history_list = ttk.Treeview(delete_page, columns=('Sum_price','Description','End_T','Start_T','Users','Device','Day','Month','Year','id'),
    show='headings', style='Custom.Treeview', height=18)

    history_list.heading('Sum_price', text='مجموع')
    history_list.heading('Description', text='توضیحات')
    history_list.heading('End_T', text='پایان')
    history_list.heading('Start_T', text='شروع')
    history_list.heading('Users', text='دسته ها')
    history_list.heading('Device', text='دستگاه')
    history_list.heading('Day', text='روز')
    history_list.heading('Month', text='ماه')
    history_list.heading('Year', text='سال')
    history_list.heading('id', text='#')

    history_list.column('Sum_price', width=10, anchor='center')
    history_list.column('Description', width=10, anchor='center')
    history_list.column('End_T', width=10, anchor='center')
    history_list.column('Start_T', width=5, anchor='center')
    history_list.column('Users', width=5, anchor='center')
    history_list.column('Device', width=5, anchor='center')
    history_list.column('Day', width=5, anchor='center')
    history_list.column('Month', width=5, anchor='center')
    history_list.column('Year', width=30, anchor='center')
    history_list.column('id', width=10, anchor='center')

    history_list.bind('<<TreeviewSelect>>', get_selection)
    history_list.place(x=18, y=15, width=973, height=350)

    history_scrol = ttk.Scrollbar(delete_page, orient=VERTICAL, command=history_list.yview)
    history_list.configure(yscrollcommand=history_scrol.set)
    history_scrol.place(x=1000, y=15, width=20, height=350)

    history_list.tag_configure('evenrow', background='#b0b0b0')
    history_list.tag_configure('oddrow', background='#e8e8e8')
#------------------butons----------------------

    def clear_list():
        for i in history_list.get_children():
            history_list.delete(i)

    def view():

        clear_list()
        table = history_del_back.show()

        list_info = []
        list_index = []
        index_num = 0
        for i in table:
            list_index.append(index_num)
            list_info.append(i)
            index_num += 1

        for index, info in list(zip(list_index, list_info)):
            if index % 2 == 0:
                history_list.insert('', END, values=(info[9],info[8],info[7],info[6],info[5],info[4],info[3],info[2],info[1],info[0]), tags=('evenrow',))
            if index % 2 != 0:
                history_list.insert('', END, values=(info[9],info[8],info[7],info[6],info[5],info[4],info[3],info[2],info[1],info[0]), tags=('oddrow',))


    view()

    btn1 = Button(delete_page, text='حذف کردن', bg='#cc5959',fg='white', borderwidth=4 ,font=('Arial', 15, 'bold'),cursor='hand2', command= lambda: delete_btn())
    btn1.place(x=18, y=380, width=100, height=30)
    def delete_btn():
        result = messagebox.askquestion('.؟.', 'آیا میخواهید این بازی را حذف کنید؟')
        if result == 'yes':
            try:
                history_del_back.delete_r(row[9])
            except NameError:
                messagebox.showerror('ارور', 'موردی انتخاب نشده است')
            view()


    btn2 = Button(delete_page, text='مشاهده همه', bg='#5A6C57',fg='white', borderwidth=4 ,font=('Arial', 15, 'bold'),cursor='hand2', command= lambda : view_btn())
    btn2.place(x=890, y=380, width=100, height=30)

    def view_btn():
        global row
        view()

        try:
            row = list(row)
            row[9] = 0
        except NameError:
            pass

    btn3 = Button(delete_page, text='جست و جو', bg='#5A6C57',fg='white', borderwidth=4 ,font=('Arial', 15, 'bold'),cursor='hand2', command= lambda: search_btn())
    btn3.place(x=770, y=380, width=100, height=30)


    line = Canvas(delete_page, bg='green')
    line.place(x=18, y=420, width=975, height=6)

    def show(val):
        global main
        for main in [val]:
            n = 0
            st = ''
            main = str(main)
            if len(main) > 3:
                for j in range(len(main) - 1, -1, -1):
                    if n == 3:
                        st += ','
                        n = 0
                    st += main[j]
                    n += 1
                main = ''
                for j in st[::-1]:
                    main += j


    def search_btn():
        global row
        s_p =  str(sum_price.get())
        show(s_p)
        rows = history_del_back.search(year.get().strip(), month.get().strip(), day.get().strip(), device.get().strip(), users.get().strip(), description.get().strip(), main.strip())

        clear_list()
        list_info = []
        list_index = []
        index_num = 0
        for i in rows:
            list_index.append(index_num)
            list_info.append(i)
            index_num += 1

        try:
            for index, info in list(zip(list_index, list_info)):
                if index % 2 == 0:
                    history_list.insert('', END, values=(info[9],info[8],info[7],info[6],info[5],info[4],info[3],info[2],info[1],info[0]), tags=('evenrow',))
                if index % 2 != 0:
                    history_list.insert('', END, values=(info[9],info[8],info[7],info[6],info[5],info[4],info[3],info[2],info[1],info[0]), tags=('oddrow',))
        except IndexError:
            view()

        for i in [year, month, day, device, users, description, sum_price]:
            i.set('')
        try:
            row = list(row)
            row[9] = 0
        except NameError:
            pass


    #-----------------------search featurs--------------------------
    #*********labels*********
    lbl1 = Label(delete_page, text='سال', fg='black',bg='#ECEBDE', font=('Arial', 13, 'bold'))
    lbl1.place(x=840, y=440, width=100, height=30)

    lbl2 = Label(delete_page, text='ماه', width=8, bg='#ECEBDE', fg='black', font=('Arial', 13, 'bold'))
    lbl2.place(x=720, y=440, width=100, height=30)

    lbl3 = Label(delete_page, text='روز', width=8, bg='#ECEBDE', fg='black', font=('Arial', 13, 'bold'))
    lbl3.place(x=600, y=440, width=100, height=30)

    lbl4 = Label(delete_page, text='دستگاه', width=8, bg='#ECEBDE', fg='black', font=('Arial', 13, 'bold'))
    lbl4.place(x=480, y=440, width=100, height=30)

    lbl5 = Label(delete_page, text='تعداد دسته ها', width=8, bg='#ECEBDE', fg='black', font=('Arial', 13, 'bold'))
    lbl5.place(x=360, y=440, width=100, height=30)

    lbl6 = Label(delete_page, text='توضیحات', width=8, bg='#ECEBDE', fg='black', font=('Arial', 13, 'bold'))
    lbl6.place(x=190, y=440, width=150, height=30)

    lbl7 = Label(delete_page, text='مجموع', width=8, bg='#ECEBDE', fg='black', font=('Arial', 13, 'bold'))
    lbl7.place(x=65, y=440, width=100, height=30)



    #*********entries********
    year = StringVar()
    en1 = Entry(delete_page, textvariable=year, font=('Arial', 13, 'bold'), cursor='hand2', bg='white',fg='#000000', justify='center')
    en1.place(x=840, y=480, width=100, height=30)

    month = StringVar()
    en2 = Entry(delete_page, textvariable=month, font=('Arial', 13, 'bold'), cursor='hand2',bg='white',fg='#000000', justify='center')
    en2.place(x=720, y=480, width=100, height=30)

    day = StringVar()
    en3 = Entry(delete_page, textvariable=day, font=('Arial', 13, 'bold'), cursor='hand2',bg='white',fg='#000000', justify='center')
    en3.place(x=600, y=480, width=100, height=30)

    device = StringVar()
    en4 = Entry(delete_page, textvariable=device, font=('Arial', 13, 'bold'), cursor='hand2', bg='white',fg='#000000', justify='center')
    en4.place(x=480, y=480, width=100, height=30)

    users = StringVar()
    en5 = Entry(delete_page, textvariable=users, font=('Arial', 13, 'bold'), cursor='hand2', bg='white',fg='#000000', justify='center')
    en5.place(x=360, y=480, width=100, height=30)

    description = StringVar()
    en6 = Entry(delete_page, textvariable=description, font=('Arial', 13, 'bold'), cursor='hand2',bg='white',fg='#000000', justify='center')
    en6.place(x=190, y=480, width=150, height=30)

    sum_price = StringVar()
    en7 = Entry(delete_page, textvariable=sum_price, font=('Arial', 13, 'bold'), cursor='hand2',bg='white',fg='#000000', justify='center')
    en7.place(x=65, y=480, width=100, height=30)

    delete_page.mainloop()

