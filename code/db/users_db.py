
from .connect_db import connect_

class Create_user:
    def create_user(user_id: int, username: str, email: str):
        connection = connect_()
        connection.cursor().execute("INSERT OR REPLACE INTO Users(user_id, username, email) VALUES (?, ?, ?);", (user_id, username, email))
        connection.commit()
    def update(user_id: int, item: dict):
        connection = connect_()
        connection.cursor().execute(f"""
UPDATE OR REPLACE INTO Users({','.join(item.keys())}) 
WHERE user_id == {user_id} values 
({','.join(["?" for i in item.values()])});""",
(",".join(item.values())))
        connection.commit()
class Collect:
    def collect_user(user_id: int, *args):
        # собирает данные в формате id, фото и все нужное
        connection = connect_()
        result = connection.cursor().execute(f"""SELECT {','.join([i for i in args])} FROM Users WHERE user_id == {user_id}""")
        return result
