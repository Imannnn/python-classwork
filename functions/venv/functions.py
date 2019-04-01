#def means define
def print_something(text):
    print(text) # print is a function that was already made

print_something("I want chicken.")
print_something("Now I want falafel")

def adding_two_numbers(n1=0,n2=0):
    alpha=n1+ n2
    return print(alpha)


#function names should be lower case
adding_two_numbers(4,7)

def print_any_numbers(*numbers): # the star is to have as many arguments as you want, limit could be 32
    for num in numbers:
        print(num)

#result= print(print_any_numbers(1,23,24,2,42,4,2432,3,24,2,4,24234) )

#lab
#create a calculator
def calculate():
    operation = input('''
Please type in the math operation you would like to complete:
+ for addition
- for subtraction
* for multiplication
/ for division
''')

    number_1 = int(input('Please enter the first number: '))
    number_2 = int(input('Please enter the second number: '))

    if operation == '+':
        print('{} + {} = '.format(number_1, number_2))
        print(number_1 + number_2)

    elif operation == '-':
        print('{} - {} = '.format(number_1, number_2))
        print(number_1 - number_2)

    elif operation == '*':
        print('{} * {} = '.format(number_1, number_2))
        print(number_1 * number_2)

    elif operation == '/':
        print('{} / {} = '.format(number_1, number_2))
        print(number_1 / number_2)

    else:
        print('You have not typed a valid operator, please run the program again.')

# Call calculate() outside of the function
calculate()