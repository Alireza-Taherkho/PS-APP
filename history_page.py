from adodbapi import OperationalError
from tkinter import *
from tkinter import ttk, Toplevel, messagebox
import history_back
import history_delete


def history_window():
    history = Toplevel()
    history.geometry('1050x525')
    history.resizable(False, False)
    history.title('History')
    history.configure(bg='#ECEBDE')

    style = ttk.Style(history)
    style.configure("Custom.Treeview", font=('Arial', 12))
    style.configure('Custom.Treeview.Heading', font=('Arial', 13))

#-------------------list box-----------------------------

    def get_selection(event):
        global row
        selected_item = history_list.selection()
        if selected_item:
            row = history_list.item(selected_item[0],'values')



    history_list = ttk.Treeview(history, columns=('Sum_price','Description','End_T','Start_T','Users','Device','Day','Month','Year','id'),
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

    history_scrol = ttk.Scrollbar(history, orient=VERTICAL, command=history_list.yview)
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
        table = history_back.show()

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

    btn1 = Button(history, text='حذف کردن', bg='#cc5959',fg='white', borderwidth=4 ,font=('Arial', 15, 'bold'),cursor='hand2', command= lambda: delete_btn())
    btn1.place(x=18, y=380, width=100, height=30)
    def delete_btn():
        result = messagebox.askquestion('.؟.', 'آیا میخواهید این بازی را حذف کنید؟')
        if result == 'yes':
            try:
                history_back.delete_r(row[9])
            except NameError:
                messagebox.showerror('ارور', 'موردی انتخاب نشده است')
            view()


    btn2 = Button(history, text='مشاهده همه', bg='#5A6C57',fg='white', borderwidth=4 ,font=('Arial', 15, 'bold'),cursor='hand2', command= lambda : view_btn())
    btn2.place(x=890, y=380, width=100, height=30)

    def view_btn():
        global row
        view()

        try:
            row = list(row)
            row[9] = 0
        except NameError:
            pass

    btn3 = Button(history, text='تراکنش ها', bg='#5A6C57', fg='white', borderwidth=4, font=('Arial', 15, 'bold'),cursor='hand2',command=lambda : transaction_page())
    btn3.place(x=770, y=380, width=100, height=30)

    btn4 = Button(history, text='جست و جو', bg='#5A6C57',fg='white', borderwidth=4 ,font=('Arial', 15, 'bold'),cursor='hand2', command= lambda: search_btn())
    btn4.place(x=650, y=380, width=100, height=30)

    btn5 = Button(history, text='تاریخچه حذفیات', bg='#5A6C57', fg='white', borderwidth=4, font=('Arial', 15, 'bold'),cursor='hand2', command=lambda: history_delete.delete_history_window())
    btn5.place(x=500, y=380, width=125, height=30)


    line = Canvas(history, bg='green')
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
        rows = history_back.search(year.get().strip(), month.get().strip(), day.get().strip(), device.get().strip(), users.get().strip(), description.get().strip(), main.strip())

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


    def transaction_page():
        transaction = Toplevel()
        transaction.geometry('600x200')
        transaction.resizable(False, False)
        transaction.title('Transactions')
        transaction.configure(bg='#ECEBDE')

        l = []
        row = history_back.uniqe_year()
        for i in row:
            l.append(str(i[1]))

        Label1 = Label(transaction, text='سال', width=9, font=('Arial', 16, 'bold'), bg='#5A6C57', fg='white')
        Label1.place(x=10, y=10)

        year_val = StringVar()
        combo_year = ttk.Combobox(transaction, width=17, height=4, textvariable=year_val)
        combo_year['values'] = l
        combo_year.configure(values=combo_year['values'])
        combo_year.place(x=10, y=50)


        Label2 = Label(transaction, text='ماه', width=9, font=('Arial', 16, 'bold'), bg='#5A6C57', fg='white')
        Label2.place(x=160, y=10)

        month_val = StringVar()
        combo_month = ttk.Combobox(transaction, width=17,height=12, textvariable=month_val)
        combo_month['values'] = [None,'1','2','3','4','5','6','7','8','9','10','11','12']
        combo_month.configure(values=combo_month['values'])
        combo_month.place(x=160, y=50)


        Label3 = Label(transaction, text='روز', width=9, font=('Arial', 16, 'bold'), bg='#5A6C57', fg='white')
        Label3.place(x=305, y=10)

        day_val = StringVar()
        combo_day = ttk.Combobox(transaction, width=17, height=32, textvariable=day_val)
        combo_day['values'] = [None,'1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31']
        combo_day.configure(values=combo_day['values'])
        combo_day.place(x=305, y=50)


        button = Button(transaction, text='تراکنش', width=10,height=2, font=('Arial', 14, 'bold'),cursor='hand2', bg='#5A6C57', fg='white', command= lambda :trans_btn())
        button.place(x=450, y=10)

        def trans_btn():
            if year_val.get() == '' or month_val.get() == '' or day_val.get() == '':
                messagebox.showerror('.!.','همه مقادیر را انتخاب کنید')
                return 'Error'

            l = []
            number = ''
            year = year_val.get()
            month = month_val.get()
            day = day_val.get()

            if month == 'None':
                month = None
            if day == 'None':
                day = None

            row = history_back.transaction_calc(year, month, day)
            for i in row:
                if len(i[-1]) > 3:
                    for j in i[-1]:
                        if j != ',':
                            number += j
                    l.append(int(number))
                    number = ''

            if l == []:
                messagebox.showerror('.!.','هیچ نتیجه ای یافت نشد')
                return 'Error'

            sum_price = 0
            for i in l:
                sum_price += i

            show(sum_price)
            result['text'] = main


        result = Label(transaction, text='', width=32, font=('Arial', 16, 'bold'),bg='#9ABF80' ,fg='black')
        result.place(x=10, y=100)


        transaction.mainloop()

    #-----------------------search featurs--------------------------
    #*********labels*********
    lbl1 = Label(history, text='سال', fg='black',bg='#ECEBDE', font=('Arial', 13, 'bold'))
    lbl1.place(x=840, y=440, width=100, height=30)

    lbl2 = Label(history, text='ماه', width=8, bg='#ECEBDE', fg='black', font=('Arial', 13, 'bold'))
    lbl2.place(x=720, y=440, width=100, height=30)

    lbl3 = Label(history, text='روز', width=8, bg='#ECEBDE', fg='black', font=('Arial', 13, 'bold'))
    lbl3.place(x=600, y=440, width=100, height=30)

    lbl4 = Label(history, text='دستگاه', width=8, bg='#ECEBDE', fg='black', font=('Arial', 13, 'bold'))
    lbl4.place(x=480, y=440, width=100, height=30)

    lbl5 = Label(history, text='تعداد دسته ها', width=8, bg='#ECEBDE', fg='black', font=('Arial', 13, 'bold'))
    lbl5.place(x=360, y=440, width=100, height=30)

    lbl6 = Label(history, text='توضیحات', width=8, bg='#ECEBDE', fg='black', font=('Arial', 13, 'bold'))
    lbl6.place(x=190, y=440, width=150, height=30)

    lbl7 = Label(history, text='مجموع', width=8, bg='#ECEBDE', fg='black', font=('Arial', 13, 'bold'))
    lbl7.place(x=65, y=440, width=100, height=30)



    #*********entries********
    year = StringVar()
    en1 = Entry(history, textvariable=year, font=('Arial', 13, 'bold'), cursor='hand2', bg='white',fg='#000000', justify='center')
    en1.place(x=840, y=480, width=100, height=30)

    month = StringVar()
    en2 = Entry(history, textvariable=month, font=('Arial', 13, 'bold'), cursor='hand2',bg='white',fg='#000000', justify='center')
    en2.place(x=720, y=480, width=100, height=30)

    day = StringVar()
    en3 = Entry(history, textvariable=day, font=('Arial', 13, 'bold'), cursor='hand2',bg='white',fg='#000000', justify='center')
    en3.place(x=600, y=480, width=100, height=30)

    device = StringVar()
    en4 = Entry(history, textvariable=device, font=('Arial', 13, 'bold'), cursor='hand2', bg='white',fg='#000000', justify='center')
    en4.place(x=480, y=480, width=100, height=30)

    users = StringVar()
    en5 = Entry(history, textvariable=users, font=('Arial', 13, 'bold'), cursor='hand2', bg='white',fg='#000000', justify='center')
    en5.place(x=360, y=480, width=100, height=30)

    description = StringVar()
    en6 = Entry(history, textvariable=description, font=('Arial', 13, 'bold'), cursor='hand2',bg='white',fg='#000000', justify='center')
    en6.place(x=190, y=480, width=150, height=30)

    sum_price = StringVar()
    en7 = Entry(history, textvariable=sum_price, font=('Arial', 13, 'bold'), cursor='hand2',bg='white',fg='#000000', justify='center')
    en7.place(x=65, y=480, width=100, height=30)


