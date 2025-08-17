
from tkinter import *
from tkinter import ttk, Toplevel, messagebox
import devices
import time
import threading
import time_back
import FI_Page
import jdatetime
from tkinter.filedialog import askopenfilename
import pygame
pygame.mixer.init()

time_w = ''


def time_window():
    global time_w
    time_w = Toplevel()
    time_w.geometry('700x550')
    time_w.resizable(False, False)
    time_w.title('Ps App')
    time_w.configure(bg='#ECEBDE')


    #--------------------------------------------------------------
    def erase(val):
        val.set('')

    frame = Label(time_w, borderwidth=5, relief='groove', bg='#ECEBDE', highlightcolor='green')
    frame.place(x=10, y=10, width=680, height=530)

    l1 = Button(time_w, text='شماره دستگاه', cursor='hand2', font=('Arial', 15, 'bold'), fg='#EEEEEE', bg='#85A98F',relief='sunken', command= lambda :erase(device_num))
    l1.place(x=530, y=30, width=140, height=33)

    value_list = []
    device_num = ttk.Combobox(time_w, values=value_list, font=('Arial', 15, 'bold'), justify='center')
    device_num.place(x=300, y=30, width=210, height=30)

    show_lable1 = Label(time_w, text='', font=('Arial', 13, 'bold'), bg='#ECEBDE', fg='black')
    show_lable1.place(x=45, y=32, width=150)

    def device_exists():
        value_list = []
        device_created = devices.select_device()
        for i in device_created:
            value_list.append(i[1])
        try:
            device_num['values'] = value_list
        except:
            try:
                pygame.mixer.music.stop()
            except:
                pass


    def while_device_num():
        while True:
            global show_table
            device_exists()
            if device_num.get():
                show_lable1['text'] = devices.select_type_of_device(device_num.get())
            else:
                show_lable1['text'] = devices.select_type_of_device(device_num.get())

            time.sleep(0.5)

    task1 = threading.Thread(target=while_device_num)
    task1.start()
    #-----------

    l2 = Button(time_w, text='تعداد دسته ها', cursor='hand2', font=('Arial', 13, 'bold'), width=13, fg='#EEEEEE',bg='#85A98F', relief='sunken', command=lambda: erase(users))
    l2.place(x=530, y=80)

    users = StringVar()
    r1 = Radiobutton(time_w, text='تک دسته', variable=users, value='1', cursor='hand2', font=('Arial', 13, 'bold'),width=8, borderwidth=4, bg='#5A6C57', indicator=0, fg='#d4d4d4').place(x=415, y=80)
    r2 = Radiobutton(time_w, text='دو دسته', variable=users, value='2', cursor='hand2', font=('Arial', 13, 'bold'),width=8, borderwidth=4, bg='#5A6C57', indicator=0, fg='#d4d4d4').place(x=300, y=80)
    r3 = Radiobutton(time_w, text='سه دسته', variable=users, value='3', cursor='hand2', font=('Arial', 13, 'bold'),width=8, borderwidth=4, bg='#5A6C57', indicator=0, fg='#d4d4d4').place(x=185, y=80)
    r4 = Radiobutton(time_w, text='چهار دسته', variable=users, value='4', cursor='hand2', font=('Arial', 13, 'bold'),width=8, borderwidth=4, bg='#5A6C57', indicator=0, fg='#d4d4d4').place(x=70, y=80)


    l3 = Button(time_w, text='پایان بر اساس قیمت', cursor='hand2', font=('Arial', 13, 'bold'), width=13, fg='#EEEEEE',bg='#85A98F', relief='sunken', command=lambda: erase(price_input))
    l3.place(x=530, y=130)
    price_input = StringVar()
    e1 = Entry(time_w, textvariable=price_input, font=('Arial', 15, 'bold'), cursor='hand2', bg='white', fg='#000000',justify='center')
    e1.place(x=300, y=130, width=210, height=36)
    show_lable2 = Label(time_w, text='به تومان', font=('Arial', 13, 'bold'), bg='#ECEBDE', fg='black')
    show_lable2.place(x=215, y=133, width=80)


    l4 = Button(time_w, text='پایان بر اساس زمان', cursor='hand2', font=('Arial', 13, 'bold'), width=13, fg='#EEEEEE',bg='#85A98F', relief='sunken', command=lambda: erase(time_input))
    l4.place(x=530, y=180)
    time_input = StringVar()
    e2 = Entry(time_w, textvariable=time_input, font=('Arial', 15, 'bold'), cursor='hand2', bg='white', fg='#000000',justify='center')
    e2.place(x=300, y=180, width=210, height=36)
    show_lable3 = Label(time_w, text='به دقیقه', font=('Arial', 13, 'bold'), bg='#ECEBDE', fg='black')
    show_lable3.place(x=217, y=183, width=80)

    btn1 = Button(time_w, text='شروع', cursor='hand2', borderwidth=4, font=('Arial', 13, 'bold'), fg='#000000',bg='#9ABF80', command=lambda :start_alarm())
    btn1.place(x=70, y=150, width=95, height=37)

    #-----------------------------------------------------------------------------------------------------------------------------------

    def get_selection_row(event):
        global row
        selected_item = list1.selection()
        if selected_item:
            row = list1.item(selected_item[0], 'values')


    list1 = ttk.Treeview(time_w,columns=('target', 'status', 'End', 'Start', 'Users', 'Device', 'id'),show='headings', style='Custom.Treeview')
    list1.heading('target', text='بازه دستور')
    list1.heading('status', text='وضعیت')
    list1.heading('End', text='پایان')
    list1.heading('Start', text='شروع')
    list1.heading('Users', text='دسته ها')
    list1.heading('Device', text='دستگاه')
    list1.heading('id', text='#')


    list1.column('target', width=5, anchor='center')
    list1.column('status', width=5, anchor='center')
    list1.column('End', width=5, anchor='center')
    list1.column('Start', width=5, anchor='center')
    list1.column('Users', width=30, anchor='center')
    list1.column('Device', width=10, anchor='center')
    list1.column('id', width=10, anchor='center')

    list1.bind('<<TreeviewSelect>>', get_selection_row)
    list1.place(x=55, y=230, width=615, height=200)

    sb1 = ttk.Scrollbar(time_w, orient=VERTICAL, command=list1.yview)
    list1.configure(yscrollcommand=sb1.set)
    sb1.place(x=18, y=230, width=20, height=200)

    list1.tag_configure('evenrow', background='#b0b0b0')
    list1.tag_configure('oddrow', background='#e8e8e8')
    #-----------------------------------------------------------------------------
    btn2 = Button(time_w, text='ویرایش', cursor='hand2', borderwidth=4, font=('Arial', 13, 'bold'), fg='#EEEEEE',bg='#5A6C57', command= lambda: edit_table())
    btn2.place(x=575, y=440, width=95, height=37)

    btn3 = Button(time_w, text='حذف', cursor='hand2', borderwidth=4, font=('Arial', 13, 'bold'), fg='white',bg='#cc5959', command= lambda: dlt_row())
    btn3.place(x=55, y=440, width=95, height=37)

    btn4 = Button(time_w, text='انتخاب زنگ', cursor='hand2', borderwidth=4, font=('Arial', 12, 'bold'), fg='#EEEEEE',bg='#5A6C57', command= lambda: open_file())
    btn4.place(x=575, y=490, width=95, height=28)

    #--------------------------------------functions------------------------------------------------------
    def clear_list():
        for i in list1.get_children():
            list1.delete(i)

    def view():
        clear_list()
        table = time_back.show()

        list_info = []
        list_index = []
        index_num = 0
        for i in table:
            list_index.append(index_num)
            list_info.append(i)
            index_num += 1

        for index, info in list(zip(list_index, list_info)):
            if index % 2 == 0:
                list1.insert('', END, values=(info[6],info[5],info[4],info[3],info[2],info[1],info[0]), tags=('evenrow',))
            if index % 2 != 0:
                list1.insert('', END, values=(info[6],info[5],info[4],info[3],info[2],info[1],info[0]), tags=('oddrow',))

    view()


    def check():
        device = device_num.get()
        check_there = False
        device_selected = devices.select_device()
        for i in device_selected:
            if i[1] == device:
                check_there = True
                break
        if check_there == False:
            messagebox.showerror('.!.', '!نام دستگاه تشخیص داده نشد')
            return 'Error'

        if users.get() == '':
            messagebox.showerror('.!.', 'تعداد دسته ها دریافت نشد')
            return 'Error'

        if price_input.get() != '' and time_input.get() != '' or price_input.get() == '' and time_input.get() == '':
            messagebox.showerror('.!.', '!فقط میتوانید یا بر اساس قیمت و یا بر اساس زمان، آلارم خود را بسازید')
            return 'Error'



    def creat_alarm_setting(device, user, price_unit, time_unit, pt, start_hour, start_minute, condition):
        devices_info = devices.select_device()
        device_number_info = []
        for i in devices_info:
            if i[1] == device:
                device_number_info = [i[1], i[2]]

        try:
            prices_info = FI_Page.select_info(device_number_info[1])
        except IndexError:
            messagebox.showerror('.!.', '!اطلاعات دستگاه ها با یکدیگر هماهنگ نیست')
            return 'Error', True, True

        new_price = ''
        for i in prices_info[int(user) - 1]:
            if i != ',':
                new_price += i

        price_per_minute = int(new_price) / prices_info[int(4)]
        if pt == True:
            final_time = int(round(price_unit / price_per_minute, 0))
            target_time = f'{price_unit}تومان '
        else:
            final_time = time_unit
            target_time = f'{time_unit}دقیقه '


        end_hour = start_hour
        end_minute = start_minute
        hour = 0
        minute = 0
        while final_time != 0:
            if final_time >= 60:
                hour += 1
                final_time -= 60
                if end_hour == 23:
                    end_hour = 0
                else:
                    end_hour += 1
            else:
                if final_time + end_minute >= 60:
                    final_time = final_time - (60 - end_minute)
                    hour += 1
                    if end_hour == 23:
                        end_hour = 0
                    else:
                        end_hour += 1
                    end_minute = final_time
                    minute = final_time
                    final_time = 0
                else:
                    end_minute += final_time
                    minute = final_time
                    final_time = 0

        if condition == True:
            return end_hour, end_minute, target_time
        else:
            return f'{end_hour} : {end_minute}', target_time



    def start_alarm():
        if check() == 'Error':
            return 'Error'

        device = device_num.get()
        user = users.get()
        if price_input.get():
            price_unit = int(price_input.get())
            time_unit = ''
            pt = True
        if time_input.get():
            time_unit = int(time_input.get())
            price_unit = ''
            pt = False

        start_hour = jdatetime.datetime.now().hour
        start_minute = jdatetime.datetime.now().minute

        end_hour, end_minute, target_time = creat_alarm_setting(device, user, price_unit, time_unit, pt, start_hour, start_minute, condition=True)

        time_back.start(device, user, f'{start_hour} : {start_minute}', f'{end_hour} : {end_minute}', target_time)
        view()
        users.set('')
        device_num.set('')
        price_input.set('')
        time_input.set('')



    def dlt_row():
        try:
            result = messagebox.askquestion('.?.', '؟آیا میخواهید این ردیف را حذف کنید')
            if result == 'yes':
                time_back.delete_r(row[6])
        except (NameError, TypeError):
            messagebox.showerror('ارور', 'موردی انتخاب نشده است')
        view()


    def edit_table():
        global row
        if price_input.get() != '' and time_input.get() != '':
            messagebox.showerror('.!.', '!فقط میتوانید یا بر اساس قیمت و یا بر اساس زمان، آلارم خود را بسازید')
            return 'Error'

        if row[1] == 'بسته':
            messagebox.showerror('.!.', 'آلارم بسته شده است')
            return 'Error'

        price_unit = ''
        time_unit = ''
        if price_input.get():
            price_unit = int(price_input.get())
            pt = True
        elif time_input.get():
            time_unit = int(time_input.get())
            pt = False
        else:
            numbers = '0123456789'
            if 'تومان' in row[0]:
                pt = True
                for i in row[0]:
                    if i in numbers:
                        price_unit += i
                price_unit = int(price_unit)

            elif 'دقیقه' in row[0]:
                pt = False
                for i in row[0]:
                    if i in numbers:
                        time_unit += i
                time_unit = int(time_unit)

        time = row[3]
        time_edited = ''
        for i in time:
            if i != ' ':
                time_edited += i

        start_hour = ''
        start_minute = ''
        tf = False
        for i in time_edited:
            if i == ':':
                tf = True
                continue
            if tf == False:
                start_hour += i
            else:
                start_minute += i
        start_hour = int(start_hour)
        start_minute = int(start_minute)

        l = []
        listnum = [4, 5]
        n = 0
        val_list = [users.get(), device_num.get()]
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

        end_t, target = creat_alarm_setting(l[1], l[0], price_unit, time_unit, pt, start_hour, start_minute, condition=False)
        time_back.update_r(row[6], l[1], l[0], end_t, target)

        device_num.set('')
        users.set('')
        price_input.set('')
        time_input.set('')
        view()

        try:
            row = list(row)
            row[6] = 0
        except NameError:
            pass



    def open_file():
        files = [('All Files', '*.mp3*')]
        file = askopenfilename(filetypes=files, defaultextension='.mp3')
        time_back.insert_song(str(file))


    time_w.mainloop()


#.!toplevel
def separate(sentnce):
    time = sentnce
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

    return int(start_h), int(start_m)



def supervision(window):
    while True:
        all_games = time_back.show()
        if all_games != []:
            for i in all_games:
                if pygame.mixer.music.get_busy() == True:
                    continue

                if i[5] == 'باز':
                    hour_now = jdatetime.datetime.now().hour
                    minute_now = jdatetime.datetime.now().minute
                    past_hour, past_minute = separate(i[4])
                    if (hour_now == past_hour and minute_now > past_minute) or (hour_now > past_hour):
                        time_back.update_status(i[0], 'بسته')
                        continue

                    if i[4] == f'{hour_now} : {minute_now}':
                        try:
                            adrs = str(time_back.show_songs())
                        except IndexError:
                            messagebox.showerror('.!.', 'هیچ آهنگی انتخاب نکردید')

                        try:
                            pygame.mixer.music.load(r'{}'.format(adrs))
                            pygame.mixer.music.play()
                        except:
                            messagebox.showerror('.!.', 'هیچ گونه فایلی به عنوان آلارم پیدا نشد')
                        time_back.update_status(i[0], 'بسته')

                        try:
                            stop_song_btn = Button(time_w, text='قطع زنگ', cursor='hand2', borderwidth=4, font=('Arial', 12, 'bold'),fg='white', bg='#cc5959', command=lambda: stop_btn())
                            stop_song_btn.place(x=475, y=490, width=70, height=28)
                        except TclError:
                            stop_song_btn = Button(window, text='قطع زنگ', cursor='hand2', borderwidth=4,font=('Arial', 12, 'bold'), fg='white', bg='#cc5959', command=lambda: stop_btn())
                            stop_song_btn.place(x=22, y=5, width=70, height=28)


                        def stop_btn():
                            stop_song_btn.place_forget()
                            try:
                                pygame.mixer.music.stop()
                            except:
                                pass


        time.sleep(5)


