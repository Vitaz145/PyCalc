#!/usr/bin/env python
# Def imports
import time as t
# Welcome screen
t.sleep(0.15)
print("W E L C O M E");
print("Author: Vitaz145");
print("URL: https://vk.com/vitaz145");
print("Version: 2.1b");
t.sleep(1)
#Precise Cycle
while True:
    operation = input('''
    Control List:
    '/' for division
    '*' for multiplication
    '+' for addition
    '-' for subtraction

    'V' for coffee cooking
    'C' for mode change[Not working]
    'W' for wave
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
    elif operation.upper() == 'W':
        t.sleep(3)
        print("Really?")
        t.sleep(2)
        print("Wave?")
        t.sleep(3)
        print("Do you know, that this is unlimited console spam?")
        t.sleep(1.5)
        print("Huh...")
        t.sleep(3)
        print("Are you sure?")
        t.sleep(4)
        print("Ah, you cannot answer now, too late.")
        t.sleep(3)
        print("Okay, here is your waves...")
        t.sleep(2)
        print("*tap*")
        t.sleep(2)
        while True:
            print(":")
            t.sleep(0.01)
            print("::")
            t.sleep(0.01)
            print(":::")
            t.sleep(0.01)
            print("::::")
            t.sleep(0.01)
            print(":::::")
            t.sleep(0.01)
            print("::::::")
            t.sleep(0.01)
            print(":::::::")
            t.sleep(0.01)
            print(":::::::")
            t.sleep(0.01)
            print("::::::")
            t.sleep(0.01)
            print(":::::")
            t.sleep(0.01)
            print("::::")
            t.sleep(0.01)
            print(":::::")
            t.sleep(0.01)
            print("::::::")
            t.sleep(0.01)
            print(":::::::")
            t.sleep(0.01)
            print("::::::")
            t.sleep(0.01)
            print(":::::")
            t.sleep(0.01)
            print("::::")
            t.sleep(0.01)
            print(":::")
            t.sleep(0.01)
            print("::::")
            t.sleep(0.01)
            print(":::")
            t.sleep(0.01)
            print("::")
    elif operation.upper() == 'V':
        print("Coocking coffee...")
        t.sleep(0.75)
        print("...")
        t.sleep(0.75)
        print("....")
        t.sleep(0.75)
        print(".....")
        t.sleep(0.75)
        print("......")
        t.sleep(0.75)
        print(".......")
        t.sleep(1)
        print("Coffee Done!")
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
