
import errors
import back_page
from tkinter import *
import funcs
from tkinter import ttk, messagebox
import pass_page
import history_back
import jdatetime
import notebook_page
import devices
import FI_Page
import time
import threading
import history_del_back
import time_page



#**********************setting**********************
window = Tk()
window.geometry('1050x650')
window.resizable(False, False)
window.title('Ps App')
window.configure(bg='#ECEBDE')

#********************ttk_style*********************
style = ttk.Style(window)
style.configure("Custom.Treeview", font=('Arial', 13))
style.configure('Custom.Treeview.Heading', font=('Arial', 14))


# ******************************* register game *****************
# line = Canvas(window, width=1050, height=3, bg='#0F044C')
# line.grid(row=4, column=0, columnspan=6, pady=10)

device_info = Button(window, text='اطلاعات دستگاه ها', cursor='hand2', borderwidth=3, font=('Arial', 13, 'bold'),fg='#EEEEEE',bg='#5A6C57', command= lambda :pass_page.pass_window('FI_page'))
device_info.place(x=890, y=5, width=140, height=30)

creat_device = Button(window, text='ایجاد دستگاه', cursor='hand2', borderwidth=3, font=('Arial', 13, 'bold'),fg='#EEEEEE',bg='#5A6C57', command= lambda :pass_page.pass_window('devices'))
creat_device.place(x=735, y=5, width=140, height=30)

history = Button(window, text = 'تاریخچه', cursor='hand2', font=('Arial', 13, 'bold'), borderwidth=3, fg='#EEEEEE', bg='#5A6C57', command= lambda :pass_page.pass_window('history') )
history.place(x=580, y=5, width=140, height=30)

frame2 = Label(window, borderwidth=5, relief='groove', bg='#ECEBDE', highlightcolor='green')
frame2.place(x=18, y=60, width=1017, height=170)

label_start = Label(window, text='شروع بازی', font=('Arial', 15, 'bold'),bg='#ECEBDE',fg='green')
label_start.place(x=785, y=45, width=85)

#-------------------------device------------------------
def erase(val):
    val.set('')

l5 = Button(window,text='شماره دستگاه', cursor='hand2', font=('Arial', 15, 'bold'),fg='#EEEEEE',bg='#85A98F', relief='sunken', command= lambda :erase(device_num))
l5.place(x=885, y=80, width=140, height=33)

value_list = []
device_num = ttk.Combobox(window, values=value_list, font=('Arial', 15, 'bold'), justify='center')
device_num.place(x=500, y=80, width=270, height=30)

show_lable = Label(window, text='', font=('Arial', 13, 'bold'), bg='#ECEBDE', fg='black')
show_lable.place(x=320, y=80, width=150)

def device_exists():
    value_list = []
    device_created = devices.select_device()
    for i in device_created:
        value_list.append(i[1])
    device_num['values'] = value_list

show_table = 0

def while_device_num():
    global row
    show_specialy = False
    name_taken = ''

    while True:
        global show_table
        device_exists()
        if device_num.get():
            show_lable['text'] = devices.select_type_of_device(device_num.get())

            available_devices = back_page.select_open_games()
            name = ''
            for i in available_devices:
                if i[0] == device_num.get():
                    show_specialy = True
                    name = i[0]
                    break
                else:
                    show_specialy = False

            if device_num.get() != name_taken:
                if show_specialy == True and show_table != 1:
                    view(True, name)
                    show_table = 1
                elif show_specialy == False and show_table != 0:
                    view()
                    show_table = 0
                name_taken = device_num.get()
                show_table = 2
        else:
            show_lable['text'] = devices.select_type_of_device(device_num.get())
            name_taken = device_num.get()
            if show_table != 0:
                view()
                show_table = 0

        time.sleep(0.5)


task1 = threading.Thread(target=while_device_num)
task2 = threading.Thread(target=time_page.supervision, args=(window,))
task1.start()
task2.start()


#----------------------users------------------------------
l6 = Button(window, text='تعداد دسته ها', cursor='hand2', font=('Arial', 13, 'bold'),width=13,fg='#EEEEEE',bg='#85A98F', relief='sunken', command= lambda :erase(users))
l6.place(x=885, y=130)

users = StringVar()
r5 = Radiobutton(window, text='تک دسته', variable=users, value='1', cursor='hand2', font=('Arial', 14, 'bold'),width=8, borderwidth=4, bg='#5A6C57', indicator=0,fg='#d4d4d4').place(x=660, y=130)
r6 = Radiobutton(window, text='دو دسته', variable=users, value='2', cursor='hand2', font=('Arial', 14, 'bold'),width=8, borderwidth=4, bg='#5A6C57', indicator=0,fg='#d4d4d4').place(x=500, y=130)
r7 = Radiobutton(window, text='سه دسته', variable=users, value='3', cursor='hand2', font=('Arial', 14, 'bold'),width=8, borderwidth=4, bg='#5A6C57', indicator=0,fg='#d4d4d4').place(x=340, y=130)
r8 = Radiobutton(window, text='چهار دسته', variable=users, value='4', cursor='hand2', font=('Arial', 14, 'bold'),width=8, borderwidth=4, bg='#5A6C57', indicator=0,fg='#d4d4d4').place(x=180, y=130)
#-----------------------discription-------------

l7 = Button(window, text='توضیحات', cursor='hand2', font=('Arial', 13, 'bold'),width=13,fg='#EEEEEE',bg='#85A98F', relief='sunken', command= lambda :erase(disc))
l7.place(x=885, y=180)

add_disc = Button(window, text='اضافه کردن', cursor='hand2', font=('Arial', 14, 'bold'),width=8, borderwidth=4,fg='#EEEEEE',bg='#5A6C57', command= lambda :add_disc())
add_disc.place(x=660, y=180, height=34)

disc = StringVar()
e5 = Entry(window, textvariable=disc, font=('Arial', 15, 'bold'), cursor='hand2',bg='white',fg='#000000', justify='center')
e5.place(x=180, y=180, width=432, height=36)
#---------------------------start------------------
btn2 = Button(window, text='شروع', cursor='hand2', borderwidth=4, font=('Arial', 14, 'bold'),fg='#000000',bg='#9ABF80', command= lambda :Start_Btn())
btn2.place(x=50, y=130, width=100, height=37)
#--------------------------------functions-------------------------------------------
def clear_list():
    for i in list1.get_children():
        list1.delete(i)

def view(specialy=False, arge=''):
    clear_list()
    table = back_page.show()

    list_info = []
    list_index = []
    index_num = 0
    for i in table:
        list_index.append(index_num)
        list_info.append(i)
        index_num += 1
    if specialy == False:
        for index, info in list(zip(list_index, list_info)):
            if index % 2 == 0:
                list1.insert('', END, values=(info[7], info[6], info[5], info[4], info[3], info[2], info[1], info[0]), tags=('evenrow',))
            if index % 2 != 0:
                list1.insert('', END, values=(info[7], info[6], info[5], info[4], info[3], info[2], info[1], info[0]), tags=('oddrow',))
    else:
        for index, info in list(zip(list_index, list_info)):
            if info[6] != 'باز' or info[1] != arge:
                if index % 2 == 0:
                    list1.insert('', END, values=(info[7], info[6], info[5], info[4], info[3], info[2], info[1], info[0]), tags=('evenrow',))
                if index % 2 != 0:
                    list1.insert('', END, values=(info[7], info[6], info[5], info[4], info[3], info[2], info[1], info[0]), tags=('oddrow',))
            else:
                list1.insert('', END, values=(info[7], info[6], info[5], info[4], info[3], info[2], info[1], info[0]),tags=('openrow',))


def Start_Btn():
    open_devices = back_page.select_open_games()
    device_number = device_num.get()

    devices_info = devices.select_device()
    device_math = False
    for i in devices_info:
        if i[1] == device_number:
            device_math = True

    if device_math == False:
        messagebox.showerror('.!.', '!نام دستگاه ناشناخته است')
        return 'stop'


    for i in open_devices:
        if i[0] == device_number:
            question = messagebox.askquestion('.?.',f'''           {i[0]} درحال اجرا است
آیا میخواهید بازی جدید را اضافه کنید؟''')
            if question == 'yes':
                back_page.start(device_number, users.get(), disc.get())
                view()
                device_num.set('')
                users.set(0)
                disc.set('')
                return 'continue'
            else:
                view()
                device_num.set('')
                users.set(0)
                disc.set('')
                return 'stop'

    sentence = disc.get().strip()
    if sentence != '':
        if sentence[0] == '-':
            sentence = '0' + sentence
        if sentence[0] == '*' or sentence[0] == '/':
            messagebox.showinfo('...', 'از لحاظ منطقی نمیتوانید عملگر های ضرب و تقسیم را فقط با یک عدد انجام بدید')
            sentence = sentence[1:]

    back_page.start(device_number, users.get(), sentence)
    view()
    device_num.set('')
    users.set(0)
    disc.set('')

def add_disc():
    global row
    if row[1] == 'بسته' :
        messagebox.showerror('.!.','!بازی بسته شده است')
        return 'Error'


    link = disc.get().strip()
    if link[0] == '#':
        error = errors.desc_hand(link[1:], False)
        if error[0] == False:
            return 'Error'

        table_rows = back_page.show()
        for i in table_rows:
            if i[0] == int(link[1:]):
                if i[6] == 'بسته':
                    back_page.select_price(link[1:],row[7])
                    disc.set('')
                    view()
                else:
                    messagebox.showerror('.!.', f'بازی شماره{link[1:]} هنوز بسته نشده')

        return 'Link'


    try:
        sentence = row[2]
    except NameError:
        messagebox.showerror('.!.','!هیچ ردیفی انتخاب نشده است')
        return 'Error'

    disc.set(disc.get().strip())
    index = 0
    num = '0123456789'
    for i in disc.get():
        if i not in num:
            index += 1
        else:break

    last_index = 0
    last_index_ident = disc.get()
    for i in last_index_ident[::-1]:
        if i not in num:
            last_index -= 1
            print(i)
        else:break

    if sentence != '':
        if disc.get()[0] == '-':
            if last_index != 0:
                sentence +=  ' - ' + last_index_ident[index:last_index]
            else:
                sentence +=  ' - ' + last_index_ident[index:]

        elif disc.get()[0] == '+':
            if last_index != 0:
                sentence += ' + ' + last_index_ident[index:last_index]
            else:
                sentence += ' + ' + last_index_ident[index:]

        elif disc.get()[0] == '*':
            if last_index != 0:
                sentence += ' * ' + last_index_ident[index:last_index]
            else:
                sentence += ' * ' + last_index_ident[index:]

        elif disc.get()[0] == '/':
            if last_index != 0:
                sentence += ' / ' + last_index_ident[index:last_index]
            else:
                sentence += ' / ' + last_index_ident[index:]

        else:
            if last_index != 0:
                sentence += ' + ' + last_index_ident[:last_index]
            else:
                sentence += ' + ' + last_index_ident
    else:
        if last_index != 0:
            if disc.get()[0] == '-':
                sentence += '0' + ' - ' + last_index_ident[index:last_index]
            else:
                sentence += last_index_ident[index:last_index]
        else:
            if disc.get()[0] == '-':
                sentence += '0' + ' - ' + last_index_ident[index:]
            else:
                sentence += last_index_ident[index:]
    disc.set('')
    back_page.up_disc(row[7], sentence)
    view()
    row = list(row)
    row[7] = 0

#****************************work with list **********************

def get_selection_row(event):
    global row
    selected_item = list1.selection()
    if selected_item:
        row = list1.item(selected_item[0],'values')
        if row[1] != 'بسته':
            finish_btn()
            l9_btn()
        else:
            l9['text'] = ''
            l8['text'] = ''


list1 = ttk.Treeview(window, columns=('Sum_price', 'Status', 'Description', 'End', 'Start', 'Users', 'Device', 'id'), show='headings', style='Custom.Treeview')
list1.heading('Sum_price', text='مجموع')
list1.heading('Status', text='وضعیت')
list1.heading('Description', text='توضیحات')
list1.heading('End', text='پایان')
list1.heading('Start', text='شروع')
list1.heading('Users', text='دسته ها')
list1.heading('Device', text='دستگاه')
list1.heading('id', text='#')

list1.column('Sum_price', width=10, anchor='center')
list1.column('Status', width=10, anchor='center')
list1.column('Description', width=5, anchor='center')
list1.column('End', width=5, anchor='center')
list1.column('Start', width=5, anchor='center')
list1.column('Users', width=30, anchor='center')
list1.column('Device', width=10, anchor='center')
list1.column('id', width=10, anchor='center')

list1.bind('<<TreeviewSelect>>', get_selection_row)
list1.place(x=55, y=304, width=980, height=250)

sb1 = ttk.Scrollbar(window, orient=VERTICAL, command=list1.yview)
list1.configure(yscrollcommand=sb1.set)
sb1.place(x=18, y=304, width=20, height=250)

list1.tag_configure('evenrow', background='#b0b0b0')
list1.tag_configure('oddrow', background='#e8e8e8')
list1.tag_configure('openrow', background='#b7ffaf')

#***************************special buttons*******************************
view()

view_btn = Button(window, text='آلارم',borderwidth=4, cursor='hand2', font=('Arial', 13, 'bold'), width=8, bg='#5A6C57',fg='#EEEEEE', command= lambda : time_page.time_window())
view_btn.place(x=940, y=250, height=40)

notebook_btn = Button(window, text='دفترچه',borderwidth=4, cursor='hand2', font=('Arial', 13, 'bold'), width=8, bg='#5A6C57',fg='#EEEEEE', command= lambda : notebook_page.note_book_window())
notebook_btn.place(x=710, y=250, height=40)

def until_btn():
    v1, v2, v3, v4 = '', '', '', ''
    devices_info = devices.select_device()
    device_number_info = []
    for i in devices_info:
        if i[1] == row[6]:
            device_number_info = [i[1], i[2]]

    try:
        prices_info = FI_Page.select_info(device_number_info[1])
    except IndexError:
        messagebox.showerror('.!.', '!اطلاعات دستگاه ها با یکدیگر هماهنگ نیست')
        return 'Error', True, True

    l = []
    for i, j in [[v1, prices_info[0]], [v2, prices_info[1]], [v3, prices_info[2]], [v4, prices_info[3]]]:
        for k in str(j):
            if k != ',':
                i += k
        try:
            l.append(int(i))
        except ValueError:
            messagebox.showerror('ارور', 'لطفا قسمت قیمت ها را پر کنید')
            return 'Error',True,True

        time = row[4]
        time_edited = ''
        for i in time:
            if i != ' ':
                time_edited += i

        start_h = ''
        start_m = ''
        tf = False
        for i in time_edited:
            if i == ':':
                tf = True
                continue
            if tf == False:
                start_h += i
            else:
                start_m += i

    try:
        l8['text'] = round(funcs.calcute_u_n(int(row[5]), int(start_h), int(start_m), l, prices_info[4])[0],-3)
        h = funcs.calcute_u_n(int(row[5]), int(start_h), int(start_m), l, prices_info[4])[1]
        m = funcs.calcute_u_n(int(row[5]), int(start_h), int(start_m), l, prices_info[4])[2]
    except (TypeError, ValueError):
        messagebox.showerror('ارور','!اطلاعات ناقص است')
        l9['text'] = ''
        l8['text'] = ''
        return 'Error',True,True

    result = l8['text']
    funcs.show(l8)

    l9['text'] = f'({h}ساعت : {m} دقیقه  -->  {l8["text"]})'
    return result, h, m


btn3 = Button(window, text='بروز رسانی', cursor='hand2',borderwidth=4, font=('Arial', 13, 'bold'), width=8, bg='#5A6C57',fg='#EEEEEE', command= lambda : question('u'))
btn3.place(x=825, y=250, height=40)

def update_btn():
    global row
    error = errors.desc_hand(disc)
    if error[0] == False:
        return 'Error'

    sentence = row[2]
    if disc.get() != '':
        disc.set(disc.get().strip())
        index = 0
        num = '0123456789'
        for i in disc.get():
            if i not in num:
                index += 1
            else:
                break

        last_index = 0
        last_index_ident = disc.get()
        for i in last_index_ident[::-1]:
            if i not in num:
                last_index -= 1
            else:
                break

        if disc.get()[0] == '-':
            if last_index != 0:
                sentence = '0' + ' - ' + last_index_ident[index:last_index]
            else:
                sentence = '0' + ' - ' + last_index_ident[index:]

        elif disc.get()[0] == '+' or disc.get()[0] != '+' and disc.get()[0] != '-':
            if last_index != 0:
                sentence = last_index_ident[index:last_index]
            else:
                sentence = last_index_ident[index:]

    if sentence != row[2]:
        disc.set(sentence)
    l = []
    listnum = [6,5,2]
    n = 0
    val_list = [device_num.get(), users.get(), disc.get()]
    for i in range(len(val_list)):
        if val_list[i] == 0 or val_list[i] == '' or val_list[i] == '0' and i != 2 :
            l.append(row[listnum[n]])
        else:
            l.append(val_list[i])
        n += 1

    back_page.update_r(row[7], l[0], l[1], l[2])
    view()
    device_num.set('')
    users.set('')
    disc.set('')
    l9['text'] = ''
    l8['text'] = ''
    row = list(row)
    row[7] = 0



btn4 = Button(window, text='پایان', cursor='hand2',borderwidth=4, font=('Arial', 13, 'bold'), width=8, bg='#5A6C57',fg='#EEEEEE', command= lambda : question('f'))
btn4.place(x=595, y=250, height=40)


def question(pas):
    global row
    if pas == 'f':
        try:
            if row[1] == 'باز':
                result = messagebox.askquestion('.؟.', 'آیا میخواهید این بازی را ببندید؟')
                if result == 'yes' :
                    finish_btn()
                    l9_btn()
                    sta_sum()
            else:
                messagebox.showinfo('.!.', 'بازی بسته شده است')
        except NameError:
            messagebox.showerror('.!.','!هیچ ردیفی انتخاب نشده است')
            return 'Error'

    if pas == 'd':
        if btn_del_all['bg'] == '#cc5959':
            result = messagebox.askquestion('.؟.', 'آیا میخواهید همه بازی های این صفحه را حذف کنید؟')
            if result == 'yes':

                table_results = back_page.show()
                for i in table_results:
                    if i[6] == 'باز':
                        i = list(i)
                        i.reverse()
                        row = i
                        finish_btn()
                        l9_btn()
                        sta_sum(del_mode=True)

                back_page.delete_all()
                view()
            l9['text'] = ''
            l8['text'] = ''
            btn_del_all['bg'] = 'white'
            btn_del_all['fg'] = 'black'
            btn5['text'] = 'حذف کردن'


        else:
            try:
                result = messagebox.askquestion('.؟.', 'آیا میخواهید بازی شماره {} را حذف کنید؟'.format(row[7]))
                if result == 'yes' :
                    delete_btn()
            except NameError:
                pass

    if pas == 'u':
        try:
            if row[1] == 'بسته':
                messagebox.showinfo('.!.', 'بازی بسته شده است')
                l8['text'] = ''
                l9['text'] = ''
            else:
                update_btn()
        except NameError:
            messagebox.showerror('.!.','!هیچ ردیفی انتخاب نشده است')
            return 'Error'

def finish_btn():
    if until_btn()[0] == 'Error':
        return 'Error','Error'
    price1 = int(until_btn()[0])

    try:
        price2 = int(back_page.calcute(funcs.fix_calcute(row[2])))
    except ValueError:
        return price1, '0', False

    l8['text'] = price2 + price1
    funcs.show(l8)
    return price1, row[2], price2

def l9_plus_sum():
    if until_btn()[0] == 'Error':
        return 'Error','Error'

    price1, price2 = finish_btn()[0], finish_btn()[2]

    if row[0] != '':
        sum_price = row[0]
        sum_price_edited = ''
        sum_price_list = []
        for i in range(len(sum_price)):
            if sum_price[i] != ',' and i != len(sum_price) - 1:
                if sum_price[i] != '+':
                    sum_price_edited += sum_price[i]
                else:
                    sum_price_edited += ' ' + sum_price[i] + ' '
        sum_price_list = sum_price_edited.split()

        price3 = int(back_page.calcute(sum_price_list))
        if price2 == False:
            l8['text'] = int(price3) + int(price1)
            funcs.show(l8)
        else:
            l8['text'] = int(price3) + int(price2) + int(price1)
            funcs.show(l8)

        return sum_price_edited, True, int(price1), int(price2), int(price3)
    return False, False, False, False, False

def l9_btn():
    if finish_btn()[0] == 'Error':
        return 'Error'

    hour , minute = until_btn()[1], until_btn()[2]
    price1, price2 = finish_btn()[0], finish_btn()[1]
    sum_price, tf = l9_plus_sum()[0], l9_plus_sum()[1]
    if l8['text'] == 0 or l8['text'][0] != '-':
        if tf == True:
              l9['text'] = f'دستگاه: {row[6]}    {row[5]} دسته         ({hour} ساعت : {minute}  دقیقه  -->  {price1}) + {price2} + ({sum_price})  -->  {l8["text"]}'
        else:
            l9['text'] = f'دستگاه: {row[6]}    {row[5]} دسته         ({hour} ساعت : {minute}  دقیقه  -->  {price1}) + {price2}  -->  {l8["text"]}'
    else:
        if tf == True:
              l9['text'] = f'{l8["text"][0]}دستگاه: {row[6]}    {row[5]} دسته         ({hour} ساعت : {minute}  دقیقه  -->  {price1}) + {price2} + ({sum_price})  -->  {l8["text"][1:]}'
        else:
            l9['text'] = f'{l8["text"][0]}دستگاه: {row[6]}    {row[5]} دسته         ({hour} ساعت : {minute}  دقیقه  -->  {price1}) + {price2}  -->  {l8["text"][1:]}'

def sta_sum(del_mode=False):
    if finish_btn()[0] == 'Error':
        return 'Error'

    end_time = str(jdatetime.datetime.now().hour) + ' : ' + str(jdatetime.datetime.now().minute)
    if l9_plus_sum()[1] == True:
        l8['text'] = l9_plus_sum()[2] + l9_plus_sum()[3]
        funcs.show(l8)

        if del_mode == False:
            back_page.up_status_sumprice(row[7], end_time, "بسته", l8['text'])
            view()

            sum_price = l8['text']
            history_back.start(row[4], end_time, row[6], row[5], sum_price, row[2])

        else:
            if row[1] != 'بسته':
                back_page.up_status_sumprice(row[7], end_time, "باز", l8['text'])
                view()

                sum_price = l8['text']
                history_del_back.start(row[4], end_time, row[6], row[5], sum_price, row[2])

    else:
        if del_mode == False:
            back_page.up_status_sumprice(row[7], end_time, "بسته", l8['text'])
            view()

            sum_price = l8['text']
            history_back.start(row[4], end_time, row[6], row[5], sum_price, row[2])

        else:
            if row[1] != 'بسته':
                back_page.up_status_sumprice(row[7], end_time, "باز", l8['text'])
                view()

                sum_price = l8['text']
                history_del_back.start(row[4], end_time, row[6], row[5], sum_price, row[2])

    finish_btn()
    l9_plus_sum()
    l9_btn()


btn_del_all = Button(window, text='حذف همه', bg='white',fg = '#000000', font=('Arial', 11, 'bold'), width=6, borderwidth=3, height=1, command= lambda : on_off())
btn_del_all.place(x=18, y=565)

def on_off():
    if btn_del_all['bg'] == 'white' and btn_del_all['fg'] == '#000000':
        btn_del_all['bg'] = '#cc5959'
        btn_del_all['fg'] = 'white'
        btn5['text'] = 'حذف کردن همه'
    else:
        btn_del_all['bg'] = 'white'
        btn_del_all['fg'] = '#000000'
        btn5['text'] = 'حذف کردن'




btn5 = Button(window, text='حذف کردن', cursor='hand2', font=('Arial', 13, 'bold'), borderwidth=4, bg='#cc5959',fg='white', command= lambda : question('d'))
btn5.place(x=100, y=565, width=120, height=35)

def delete_btn():
    finish_btn()
    l9_btn()
    sta_sum(del_mode=True)
    try:
        back_page.delete_r(row[7])
    except NameError:
        messagebox.showerror('ارور', 'موردی انتخاب نشده است')
    view()
    l9['text'] = ''
    l8['text'] = ''
    device_num.set('')
    users.set(0)
    disc.set('')


l8 =Label(window, text='', font=('Arial', 15, 'bold'), height=1, bg='#85A98F',fg='black')
l8.place(x=821, y=565, width=215)


l9 = Label(window, text='', font=('Arial', 15, 'bold'), height=1, bg='#85A98F',fg='black')
l9.place(x=18, y=605, width=1020)


btmp = Button(window,text='پاک کردن نتیجه' ,cursor='hand2',fg='black', bg='#85A98F', font=('Arial', 10, 'bold'), height=1, command= lambda :text_del())
btmp.place(x=725, y=565, width=80, height=30)

def text_del():
    l8['text'] = ''
    l9['text'] = ''



window.mainloop()



