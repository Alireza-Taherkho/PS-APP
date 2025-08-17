

import sqlite3
import jdatetime
from adodbapi import OperationalError
from tkinter import messagebox


def create_connection():
    conn = sqlite3.connect('ps_history_delete.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS ps_his_del(id INTEGER PRIMARY KEY AUTOINCREMENT,
    year_ INTEGER,
    month_ INTEGER,
    day_ INTEGER,
    device TEXT,
    users TEXT,
    start_t TEXT,
    end_t TEXT,
    description TEXT,
    sum_price TEXT)''')
    conn.commit()
    conn.close()

def start(start_t, end_t, device, users, sum_price, description='0'):
    if description == '' or description == None or description == False or description == ' ':
        description = '0'
    conn = sqlite3.connect('ps_history_delete.db')
    c = conn.cursor()
    c.execute('INSERT INTO ps_his_del VALUES(null,?,?,?,?,?,?,?,?,?)', (jdatetime.datetime.now().year, jdatetime.datetime.now().month, jdatetime.datetime.now().day,
    device, users, start_t, end_t, description, sum_price))
    conn.commit()
    conn.close()

def delete_r(id):
    conn = sqlite3.connect('ps_history_delete.db')
    c = conn.cursor()
    c.execute('DELETE FROM ps_his_del WHERE id=?', (id,))
    conn.commit()
    conn.close()

def show():
    conn = sqlite3.connect('ps_history_delete.db')
    c = conn.cursor()
    c.execute('SELECT * FROM ps_his_del ORDER BY id DESC')
    rows = c.fetchall()
    conn.close()
    return rows


def search(Year=None, Month=None, Day=None, Device=None, Users=None, Description=None, Sum_price=None):
    conn = sqlite3.connect('ps_history_delete.db')
    c = conn.cursor()

    l = [[Year, 'year_'], [Month, 'month_'], [Day, 'day_'], [Device, 'device'], [Users, 'users'], [Description, 'description'], [Sum_price, 'sum_price']]
    for i in range(len(l)):
        if l[i][0] == '' or l[i][0] == None or l[i][0] == False or l[i][0] == ' ':
            l[i][0] = 'false'

    search_text = 'SELECT * FROM ps_his_del WHERE'
    value_list = ()
    times = 1
    for i in range(len(l)):
        if l[i][0] != 'false':
            value_list += (l[i][0],)

            if times == 1:
                search_text += f' {l[i][1]} = ?'
                times += 1
            else:
                search_text += f' AND {l[i][1]} = ?'

    try:
        search_text += ' ORDER BY id DESC'
        c.execute(search_text, value_list)
    except:
        messagebox.showerror('.!.', '!هیچ چیزی جست و جو نشده است')
        return 'Error'
    rows = c.fetchall()
    conn.close()
    return rows




create_connection()


