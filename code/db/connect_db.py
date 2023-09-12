from sqlite3 import connect

# создание баззы данных

def connect_():
    connection = connect("data_base.db")
    return connection
def connect_db():
    connection = connect_()
    connection.cursor().execute('''
CREATE TABLE IF NOT EXISTS Users (
user_id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL
)
''')
    connection.commit()
if __name__ == "__main__":
    connect_db()