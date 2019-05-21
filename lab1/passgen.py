import random as r

while True:
    try:
        length = int(input('Enter the length of the password: '))
    except ValueError:
        continue
    password = ''
    numbs = '1234567890'
    lower_let = 'abcdefghigklmnopqrstuvyxwz'
    upper_let = 'ABCDEFGHIGKLMNOPQRSTUVYXWZ'

    pass_list =''

    tmp = input('Will we use upper-case?(y/n) ')
    if tmp == 'y':
        pass_list += upper_let

    tmp = input('Will we use lower-case?(y/n) ')
    if tmp == 'y':
        pass_list += lower_let

    tmp = input('Will we use numbers?(y/n) ')
    if tmp == 'y':
        pass_list += numbs

    if len(pass_list) == 0:
        print()
        continue

    for i in range(length):
        password += r.choice(pass_list)
    
    print()
    print (password)
    print()