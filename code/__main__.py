from db.users_db import Collect

def start():
    # первое вложение пути к начальной странице
    # если не зареган предложение зарегаться
    # через db
    pass  
if __name__ == "__main__":
    from db.connect_db import connect_db
    connect_db()
    Collect.collect_user(2, "email", "username")