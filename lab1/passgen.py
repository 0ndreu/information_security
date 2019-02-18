import random as r

length = int(input('enter the length of the password '))
password = ''
numbs = '1234567890'
lower_let = 'abcdefghigklmnopqrstuvyxwz'
upper_let = 'ABCDEFGHIGKLMNOPQRSTUVYXWZ'

pass_list =''

tmp = input('Will we use upper-case? ')
if tmp == 'y':
    pass_list += upper_let

tmp = input('Will we use lower-case? ')
if tmp == 'y':
    pass_list += lower_let

tmp = input('Will we use numbers? ')
if tmp == 'y':
    pass_list += numbs


for i in range(length):
    password += r.choice(pass_list)
print (password)