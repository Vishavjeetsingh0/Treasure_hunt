import random 
import sys


row1 = ['🐶', '🐶', '🐶']
row2 = ['🐶', '🐶', '🐶']
row3 = ['🐶', '🐶', '🐶']
map = [row1, row2, row3]
print(f'{row1}\n{row2}\n{row3}')

computer_choice = random.choice([11,12,13,21,22,23,31,32,33])

u_input = input("Enter 1st choice:")
row = int(u_input[0])-1
column = int(u_input[1])-1
if int(u_input) == computer_choice:
    print("you won!")
    map[row][column] = '🚀'
    print(f'{row1}\n{row2}\n{row3}')
    sys.exit()


# marking user's 1st choice
map[row][column] = '🐱'
print(f'{row1}\n{row2}\n{row3}')


u_input = input("Enter 2nd choice:")
row = int(u_input[0])-1
column = int(u_input[1])-1
if int(u_input) == computer_choice:
    print("you won!")
    map[row][column] = '🚀'
    print(f'{row1}\n{row2}\n{row3}')
    sys.exit()

# marking user's 2nd choice
map[row][column] = '🐱'
print(f'{row1}\n{row2}\n{row3}')



u_input = input("Enter 2nd choice:")
row = int(u_input[0])-1
column = int(u_input[1])-1
if int(u_input) == computer_choice:
    print("you won!")
    map[row][column] = '🚀'
    print(f'{row1}\n{row2}\n{row3}')
    sys.exit()

# marking user's 3rd choice
map[row][column] = '🐱'
print(f'{row1}\n{row2}\n{row3}')

