from utils.mysql_conn import connect

conn = connect()


def credit_services():
    flag = False

    while not flag:

        flag = True
        print('''
        1.Add Credit Card

        2.Display Details
        ''')
        choice = input('Enter task to perform: ')
        if choice == '1':
            add_creditcard()
        elif choice == '2':
            details()
        else:
            print('Invalid')


def add_creditcard():
    acc_no = input('Enter Account number: ')
    card_no = input('Enter the Card number(8 digit): ')
    pin = input('Enter Pin: ')
    cvv = int(input('Enter Cvv: '))
    data = (acc_no, card_no, pin, cvv)

    sql1 = 'Insert into Creditcard_info values (%s, %s, %s, %s)'

    db_cursor = conn.cursor()
    db_cursor.execute(sql1, data)
    conn.commit()
    print('Data Entered successfully')


def details():
    acc_no = input('Enter the account number: ')
    a = 'select acc_no,card_no,pin,cvv from Creditcard_info where acc_no=%s'
    data = (acc_no,)
    db_cursor = conn.cursor()
    db_cursor.execute(a, data)
    result = db_cursor.fetchone()
    print("\n\n")
    for i in range(0, len(result)):
        if i == 0:
            print("Account Number :   \t\t", result[i])
        elif i == 1:
            print("Credit Card Number :\t\t", result[i])
        elif i == 2:
            print("PIN Number :      \t\t", result[i])
        else:
            print("CVV :\t\t\t\t", result[i])
