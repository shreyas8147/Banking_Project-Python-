from utils.mysql_conn import connect

conn = connect()

def beneficiary_services():

    flag = False

    while not flag:

        flag = True
        print('''
                1.Add beneficiary

                2.Beneficiary Details
        ''')
        choice = input('Enter the  task: ')
        if choice == '1':
            add_beneficiary()
        elif choice == '2':
            details()
        else:
            print('Invalid choice! Please try again')

def add_beneficiary():
    acc_no = input('Enter Account number: ')
    beneficiary_name = input('Enter the Beneficiary name: ')
    transfer_amt = int(input('Enter transfer amount: '))
    data1 = (acc_no, beneficiary_name, transfer_amt)

    sql1 = 'Insert into Beneficiary values (%s, %s, %s)'

    db_cursor = conn.cursor()
    db_cursor.execute(sql1, data1)
    conn.commit()
    print('Data Entered successfully')


def details():
    acc_no = input('Enter the Account number: ')
    a = 'select * from Beneficiary where acc_no = %s'
    data = (acc_no, )
    db_cursor = conn.cursor()
    db_cursor.execute(a, data)
    result = db_cursor.fetchone()
    for i in result:
        print(i)




