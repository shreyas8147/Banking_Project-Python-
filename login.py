from utils.mysql_conn import connect

conn = connect()

def login(user_id, password):
    query = "select password from Registration1 where user_id = %s and password = %s"
    data = (user_id, password)
    db_cursor = conn.cursor()
    db_cursor.execute(query, data)
    if len(db_cursor.fetchall()) != 0:
        print("ok")
        return 3
    else:
        print("Invalid Login credentials, please try again!")
        flag = False

        while flag == False:
            choice = int(input("Please enter your choice(1 or 2)"))
            if choice in [1, 2]:
                flag = True
        return choice
