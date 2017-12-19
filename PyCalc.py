# Def imports
import time
# Welcome screen
time.sleep(0.15)
print("W E L C O M E\start");
print("Author: Vitaz145");
print("URL: https://vk.com/vitaz145");
print("Version: 1.1b");
print("W E L C O M E\end");
print("");
time.sleep(1)
# Start of cycle
while True:
    operation = input('''
    Control List:
    '/' for division
    '*' for multiplication
    '+' for addition
    '-' for subtraction

    'V' for coffee cooking
    'E' for exit
    ''')
    # Exit Check
    if operation.upper() == 'E':
        exit()
    elif operation.upper() == 'V':
        print("Coocking coffee...")
        time.sleep(0.75)
        print("...")
        time.sleep(0.75)
        print("....")
        time.sleep(0.75)
        print(".....")
        time.sleep(0.75)
        print("......")
        time.sleep(0.75)
        print(".......")
        time.sleep(1)
        print("Coffee Done!")
    else:
        number_1 = int(input('Number one: '));
        number_2 = int(input('Number two: '));
        time.sleep(0.25)
        print("You typed:");
        time.sleep(0.25)
        print(number_1, number_2);
        time.sleep(0.25)
        print("")
        # Plus
        if operation == '+':
            print('{} + {} = '.format(number_1, number_2))
            time.sleep(0.25)
            print(number_1 + number_2)
        # Subtract
        elif operation == '-':
            print('{} - {} = '.format(number_1, number_2))
            time.sleep(0.25)
            print(number_1 - number_2)
        # Multiplic
        elif operation == '*':
            print('{} * {} = '.format(number_1, number_2))
            time.sleep(0.25)
            print(number_1 * number_2)
        # Division
        elif operation == '/':
            print('{} / {} = '.format(number_1, number_2))
            time.sleep(0.25)
            print(number_1 / number_2)
        # Error404
        else:
            print("Error. Seems like you typed wrong operator. Program will auto restart now.")
            time.sleep(0.05)
            print("...")
            time.sleep(0.25)
            print("...")
            time.sleep(0.35)
            print("...")
            time.sleep(0.5)
            print("...")
            time.sleep(0.8)
            print("...")
            time.sleep(0.01)
            print("Restart complete")
