from utils.mysql_conn import connect

conn = connect()

def debit_services():

    flag = False

    while not flag:

        flag = True
        print('''
        1.Add Debit Card

        2.Display Details
        ''')
        choice = input('Enter the  task: ')
        if choice == '1':
            add_debitcard()
        elif choice == '2':
            details()
        else:
            print('Invalid ')


def add_debitcard():

    acc_no = input('Enter Account number: ')
    card_no = input('Enter the Card number: ')
    pin = input('Enter Pin: ')
    cvv = int(input('Enter Cvv: '))
    data1 = (acc_no, card_no, pin, cvv)


    query = 'Insert into Debitcard_info values (%s, %s, %s, %s)'

    db_cursor = conn.cursor()
    db_cursor.execute(query, data1)
    conn.commit()
    print('Data Entered successfully')


def details():
    acc_no = input('Enter  Account number: ')
    a = 'select * from Debitcard_info where acc_no=%s'
    data = (acc_no, )
    db_cursor = conn.cursor()
    db_cursor.execute(a, data)
    result = db_cursor.fetchone()

    print("\n\n")
    for i in range(0, len(result)):
        if i == 0:
            print("Account Number :   \t\t", result[i])
        elif i == 1:
            print("Debit Card Number :\t\t", result[i])
        elif i == 2:
            print("PIN Number :      \t\t", result[i])
        else:
            print("CVV :\t\t\t\t", result[i])
