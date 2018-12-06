#!/usr/bin/env python
# Def imports
import time as t
# Welcome screen
t.sleep(0.15)
print("W E L C O M E");
print("Author: Vitaz145");
print("URL: https://vk.com/vitaz145");
print("Version: 2.3a");
t.sleep(1)
#Precise Cycle
while True:
    operation = input('''
    Control List:
    '/' for division
    '*' for multiplication
    '+' for addition
    '-' for subtraction

    'C' for mode change[Not working]
    'E' for exit
    ''')
    # Exit Check
    if operation.upper() == 'E':
        exit()
    elif operation.upper() == 'C':
        mode = int(input('''
    Choose mod:
    '1' for precise mode
    '2' for rough mode
    '''))
    #Yep, coffee.
    else:
        number_1 = int(input('Number one: '));
        number_2 = int(input('Number two: '));
        t.sleep(0.25)
        print('You typed: ');
        t.sleep(0.25)
        print(number_1, "and", number_2);
        t.sleep(0.25)
        print("")
        if operation == '+':
            print('{} + {} = '.format(number_1, number_2), number_1 + number_2);
        elif operation == '-':
            print('{} - {} = '.format(number_1, number_2), number_1 - number_2);
        elif operation == '*':
            print('{} * {} = '.format(number_1, number_2), number_1 * number_2);
        elif operation == '/':
            print('{} / {} = '.format(number_1, number_2), number_1 / number_2);
        else:
        # Error404
            print("Error. Seems like you typed wrong operator. Program will auto restart now.")
