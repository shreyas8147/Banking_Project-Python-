import re

from utils.mysql_conn import connect


def get_conn():
    return connect()


def registration_details():
    conn = get_conn()

    user_id = get_user_id()

    password = check_password()
    data = (user_id, password)
    query = 'Insert into Registration1 (user_id, password) values (%s,%s)'
    db_cursor = conn.cursor()

    try:
        db_cursor.execute(query, data)
        conn.commit()
        print('Data Entered successfully')
    except Exception as e:
        print("SQL error: ", e)


def regex_checker(pattern, password):
    if re.match(pattern=pattern, string=password):
        return True
    else:
        print(
            "Password must contain 1  letter in upper case, 1 letter in lower case, a number and a special character. "
            "Please enter again!")
        return False


def check_password():
    regex = '^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!%*#?&]{8,}$'
    regex_pattern = re.compile(regex)

    password = ""

    flag: bool = False

    while not flag:
        password = str(input("Enter password : "))
        flag = regex_checker(regex_pattern, password)
    return password


def get_user_id():

    flag = False

    while(flag == False):

        user_id = int(input("\nEnter user_id:"))
        flag = check_userid(user_id)

    return user_id


def check_userid(user_id):
    conn = get_conn()

    query = 'Select * from Registration1 where user_id = %s'
    db_cursor = conn.cursor()
    db_cursor.execute(query, (user_id,))

    result = db_cursor.fetchall()

    if len(result) > 0:
        print("Account with the given user_id already exists, try again!")
        return False
    return True
