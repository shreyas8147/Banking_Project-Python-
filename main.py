from auth.login import login
from auth.register import registration_details
from home import open_account, list_services
from utils.mysql_conn import connect

conn = connect()


def start():
    choice = int(input(" Enter 1. Login 2.Registration                "))



    if choice == 1:
        init_login()
    elif choice == 2:
        registration_details()
    else:
        print("Thanks for coming!")


def init_login():
    login_stat = 1

    while True:
        if login_stat == 1:
            print("Please enter your login credentials")
            uid = int(input("User id: "))
            pwd = input("Password: ")
            login_stat = login(uid, pwd)

        elif login_stat == 2:
            registration_details()
        elif login_stat == 3:
            list_services()
        else:
            print("Invalid")
            break



start()
