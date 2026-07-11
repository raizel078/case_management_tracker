import sqlite3

def create_connection():
    conn = sqlite3.connect('cases.db')
    return conn

def create_table(conn):
    cursor = conn.cursor()
    cursor.execute('''
          CREATE TABLE IF NOT EXISTS client (
          id INTEGER PRIMARY KEY AUTOINCREMENT,
          client TEXT
             )
    ''')
    cursor.execute('''
          CREATE TABLE IF NOT EXISTS cases(
          id INTEGER PRIMARY KEY AUTOINCREMENT,
          client_id INTEGER,    
          title TEXT,
          status TEXT,
          date TEXT,
          FOREIGN KEY (client_id) REFERENCES client(id)
          )''')
    cursor.execute('''
          CREATE TABLE IF NOT EXISTS updates(
          id INTEGER PRIMARY KEY AUTOINCREMENT,
          case_id INTEGER,
          note TEXT,
          date TEXT,
          FOREIGN KEY (case_id) REFERENCES cases(id))''')
    conn.commit()


def add_case(conn, client, title, status, date):
    cursor = conn.cursor()
    #now checking if id exists
    cursor.execute('SELECT id FROM client WHERE client=?', (client,))
    row =cursor.fetchone()

    #now if the row not exists (means) id.
    if row is not None:
        client_id = row[0]
    else:
        cursor.execute('INSERT INTO client (client) VALUES (?)',(client,))
        client_id = cursor.lastrowid

    cursor.execute('''
    INSERT INTO cases (client_id, title, status, date) VALUES(?,?,?,?)''', (client_id,title,status,date))

    conn.commit()

def get_cases(conn, status='All status', search=''):
    cursor = conn.cursor()
    query = '''
        SELECT cases.id, client.client, cases.title, cases.status, 0
        FROM cases
        JOIN client ON cases.client_id = client.id
    '''
    conditions = []
    params = []

    if status != 'All status':
        conditions.append('cases.status = ?')
        params.append(status)

    if search:
        conditions.append('(cases.title LIKE ? OR client.client LIKE ?)')
        params.append('%' + search + '%')
        params.append('%' + search + '%')

    if conditions:
        query += ' WHERE ' + ' AND '.join(conditions)

    cursor.execute(query, params)
    return cursor.fetchall()

def get_stats(conn):
    cursor = conn.cursor()
    cursor.execute('SELECT COUNT(*) FROM cases')
    total = cursor.fetchone()[0]
    cursor.execute("SELECT COUNT(*) FROM cases WHERE status = 'Open'")
    open_count = cursor.fetchone()[0]
    cursor.execute("SELECT COUNT(*) FROM cases WHERE status = 'Closed'")
    closed = cursor.fetchone()[0]
    return total, open_count, closed

# new
def get_updates(conn, case_id):
    cursor = conn.cursor()
    cursor.execute('''
    SELECT id, note, date FROM updates WHERE case_id=? ORDER BY id DESC''',(case_id,))
    return cursor.fetchall()

def add_update(conn, case_id, note, date):
    cursor = conn.cursor()
    cursor.execute('''
    INSERT INTO updates (case_id, note, date) VALUES (?,?,?)''',(case_id, note, date))
    conn.commit()


