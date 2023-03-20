from home.benificiary_management import beneficiary_services
from home.credit_card import credit_services
from home.debit_card import debit_services
from utils.mysql_conn import connect


conn = connect()

def list_services():

    flag = False

    while not flag:

        flag = True
        print('''
                1.open new account 
                2.deposit amount 
                3.withdraw amount 
                4.balance enquiry 
                5.display customer details 
                6.close an account 
                7.manage beneficiaries 
                8.apply for credit card 
                9.apply for debit card 
            ''')
        choice = input("Enter task no: ")
        if choice == '1':
            open_account()
        elif choice == '2':
            deposite_amt()
        elif choice == '3':
            withdraw_amt()
        elif choice == '4':
            balance()
        elif choice == '5':
            disp_customer_details()
        elif choice == '6':
            close_acc()
        elif choice == '7':
            beneficiary_services()
        elif choice == '8':
            credit_services()
        elif choice == '9':
            debit_services()
        else:
            flag = False
            print('Invalid choice! Please try again')

def open_account():
    name = input("Enter Name : ")
    acc_no = input("Enter Account No :  ")
    dob = input("Enter D.O.B : ")
    pan_no = input("Enter Pan Number : ")
    ph_no = input("Enter Phone No : ")
    address = input("Enter Address : ")
    opening_bal = int(input("Enter opening balance : "))

    data1 = (name, acc_no, dob, pan_no, ph_no, address, opening_bal)
    data2 = (name, acc_no, opening_bal)

    sql1 = 'insert into Account values(%s,%s,%s,%s,%s,%s,%s)'
    sql2 = 'insert into Amount values(%s,%s,%s)'

    db_cursor = conn.cursor()
    db_cursor.execute(sql1, data1)
    db_cursor.execute(sql2, data2)
    conn.commit()

    print("Data Entered Successfully")


def deposite_amt():
    amount = int(input("Enter Amount : "))
    acc_no = input("Enter Account No : ")
    a = "select balance from Amount where acc_no = %s"
    data = (acc_no,)
    db_cursor = conn.cursor()
    db_cursor.execute(a, data)
    my_result = db_cursor.fetchone()
    total_amt = my_result[0] + amount
    sql = "update Amount set balance =%s where acc_no = %s"
    data = (total_amt, acc_no)
    db_cursor.execute(sql, data)
    conn.commit()

    print("Amount Deposited Successfully")


def withdraw_amt():
    amount = int(input("Enter Amount :"))
    acc_no = input("Enter Account No : ")
    a = "select balance from Amount where acc_no = %s"
    data = (acc_no,)
    db_cursor = conn.cursor()
    db_cursor.execute(a, data)
    my_result = db_cursor.fetchone()
    if len(my_result) != 0:
        total_amt = my_result[0] - amount
        sql = "update Amount set balance = %s where acc_no = %s"
        d = (total_amt, acc_no)
        db_cursor.execute(sql, d)
        conn.commit()
    else:
        print("Invalid Account number!")

    print("Amount Withdrawal Successful")


def balance():
    acc_no = input("Enter Account No : ")
    a = "select balance from Amount where acc_no= %s"
    data = (acc_no, )
    db_cursor = conn.cursor()
    db_cursor.execute(a, data)
    my_result = db_cursor.fetchone()
    print("Balance for Account:", acc_no, "is", my_result[0])


def disp_customer_details():
    acc_no = input('Enter Account No : ')
    a = "select * from Account where acc_no = %s"
    data = (acc_no,)
    db_cursor = conn.cursor()
    db_cursor.execute(a, data)
    result = db_cursor.fetchone()
    #     for i in myresult:
    #         print(i)
    print("\n\n")
    for i in range(0, len(result)):
        if i == 0:
            print("Name :   \t\t", result[i])
        elif i == 1:
            print("Account Number :\t\t", result[i])
        elif i == 2:
            print("DOB :      \t\t", result[i])
        elif i == 3:
            print("Pan Number : \t\t", result[i])
        elif i == 4:
            print("Phone Number : \t\t", result[i])
        elif i == 5:
            print("Address :  \t\t", result[i])
        else:
            print("Balance : \t\t\t\t", result[i])


def close_acc():
    acc_no = input("Enter Account No : ")
    sql1 = "delete from Account where acc_no = %s"
    sql2 = "delete from Account where acc_no = %s"
    data = (acc_no,)
    db_cursor = conn.cursor()
    db_cursor.execute(sql1, data)
    db_cursor.execute(sql2, data)
    conn.commit()
