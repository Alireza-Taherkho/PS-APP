
import sqlite3
import jdatetime
from tkinter import messagebox

def create_connection():
    conn = sqlite3.connect('ps.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS ps(id INTEGER PRIMARY KEY AUTOINCREMENT,
    device_n TEXT,
    user_n INTEGER,
    start_t TEXT,
    end_t TEXT,
    description TEXT,
    status TEXT,
    sum_price TEXT)''')
    conn.commit()
    conn.close()


def start(device_n, user_n, description=None):
    conn = sqlite3.connect('ps.db')
    c = conn.cursor()
    start = str(jdatetime.datetime.now().hour) + ' : ' + str(jdatetime.datetime.now().minute)
    c.execute('INSERT INTO ps VALUES(null,?,?,?,"",?,"باز","")', (device_n, user_n,start, description))
    conn.commit()
    conn.close()


def delete_r(id):
    conn = sqlite3.connect('ps.db')
    c = conn.cursor()
    c.execute('DELETE FROM ps WHERE id=?', (id,))
    conn.commit()
    conn.close()

def delete_all():
    conn = sqlite3.connect('ps.db')
    c = conn.cursor()
    c.execute('DELETE FROM ps')
    c.execute('DELETE FROM SQLITE_SEQUENCE WHERE name="ps"')

    conn.commit()
    conn.close()

def update_r(id, device_n, user_n, description):
    conn = sqlite3.connect('ps.db')
    c = conn.cursor()
    c.execute('UPDATE ps SET device_n=?, user_n=? , description=? WHERE id=?', (device_n, user_n, description,id))
    conn.commit()
    conn.close()

def show():
    conn = sqlite3.connect('ps.db')
    c = conn.cursor()
    c.execute('SELECT * FROM ps ORDER BY id DESC')
    rows = c.fetchall()
    conn.close()
    return rows

def up_disc(id, description):
    conn = sqlite3.connect('ps.db')
    c = conn.cursor()
    c.execute('UPDATE ps SET description=? WHERE id=?', (description, id))
    conn.commit()
    conn.close()

def up_status_sumprice(id, end_t, status, sum_price):
    conn = sqlite3.connect('ps.db')
    c = conn.cursor()
    c.execute('UPDATE ps SET end_t=?, status=?, sum_price=? WHERE id=?', (end_t,status, sum_price, id))
    conn.commit()
    conn.close()

def select_price(id, mainid):
    conn = sqlite3.connect('ps.db')
    c = conn.cursor()
    c.execute('SELECT sum_price FROM ps WHERE id=?', (id,))
    row = c.fetchall()
    row = row[0][0] + '+'

    c.execute('SELECT sum_price FROM ps WHERE id=?', (mainid,))
    befor_row = c.fetchall()
    befor_row = befor_row[0][0]
    befor_row += row
    try:
        c.execute('UPDATE ps SET sum_price=? WHERE id=?', (befor_row, mainid))
    except TypeError:
        messagebox.showerror('.!.','همچین موردی وجود ندارد')
        return 'Error'

    conn.commit()
    conn.close()



def select_open_games():
    conn = sqlite3.connect('ps.db')
    c = conn.cursor()
    c.execute('SELECT device_n FROM ps where status = "باز"')
    rows = c.fetchall()
    conn.close()
    return rows



def calcute(val):
    list_str = val

    while len(list_str) != 1:
        i = -1
        if '*' in list_str or '/' in list_str:
            while i != len(list_str) - 1:
                i += 1
                if list_str[i] == '*' or list_str[i] == '/':
                    if list_str[i] == '*':
                        list_str[i - 1] = int(list_str[i - 1]) * int(list_str[i + 1])
                        del list_str[i + 1]
                        del list_str[i]
                        i = len(list_str) - 1
                    else:
                        list_str[i - 1] = int(list_str[i - 1]) // int(list_str[i + 1])
                        del list_str[i + 1]
                        del list_str[i]
                        i = len(list_str) - 1


        else:
            while i != len(list_str) - 1:
                i += 1
                if list_str[i] == '+' or list_str[i] == '-':
                    if list_str[i] == '+':
                        list_str[i - 1] = int(list_str[i - 1]) + int(list_str[i + 1])
                        del list_str[i + 1]
                        del list_str[i]
                        i = len(list_str) - 1
                    else:
                        list_str[i - 1] = int(list_str[i - 1]) - int(list_str[i + 1])
                        del list_str[i + 1]
                        del list_str[i]
                        i = len(list_str) - 1

    return int(list_str[0])


create_connection()
