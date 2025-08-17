
import sqlite3



def create_connection():
    conn = sqlite3.connect('ps_time.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS ps_t(id INTEGER PRIMARY KEY AUTOINCREMENT,
    device_n TEXT,
    user_n INTEGER,
    start_t TEXT,
    end_t TEXT,
    status TEXT,
    target TEXT)''')
    conn.commit()
    conn.close()
create_connection()


def start(Device_n, User_n, Start, End_t, Target):
    conn = sqlite3.connect('ps_time.db')
    c = conn.cursor()
    c.execute('INSERT INTO ps_t VALUES(null,?,?,?,?,"باز",?)', (Device_n, User_n, Start, End_t, Target))
    conn.commit()
    conn.close()


def delete_r(id):
    conn = sqlite3.connect('ps_time.db')
    c = conn.cursor()
    c.execute('DELETE FROM ps_t WHERE id=?', (id,))
    conn.commit()
    conn.close()



def update_r(id, Device_n, User_n, End_t, Target):
    conn = sqlite3.connect('ps_time.db')
    c = conn.cursor()
    c.execute('UPDATE ps_t SET device_n=?, user_n=? , end_t=? , target=? WHERE id=?', (Device_n, User_n, End_t, Target,id))
    conn.commit()
    conn.close()


def update_status(id, Status):
    conn = sqlite3.connect('ps_time.db')
    c = conn.cursor()
    c.execute('UPDATE ps_t SET status=? WHERE id=?', (Status,id))
    conn.commit()
    conn.close()



def show():
    conn = sqlite3.connect('ps_time.db')
    c = conn.cursor()
    c.execute('SELECT * FROM ps_t ORDER BY id DESC')
    rows = c.fetchall()
    conn.close()
    return rows


#---------------------------

def create_song_connection():
    conn = sqlite3.connect('ps_time.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS ps_song(id INTEGER PRIMARY KEY AUTOINCREMENT, song_addrres TEXT)''')
    conn.commit()
    conn.close()
create_song_connection()


def insert_song(adrs):
    conn = sqlite3.connect('ps_time.db')
    c = conn.cursor()
    c.execute('INSERT INTO ps_song VALUES(null,?)', (adrs,))
    conn.commit()
    conn.close()



def show_songs():
    conn = sqlite3.connect('ps_time.db')
    c = conn.cursor()
    c.execute('SELECT * FROM ps_song ORDER BY id DESC')
    rows = c.fetchall()
    conn.close()
    return rows[0][-1]



