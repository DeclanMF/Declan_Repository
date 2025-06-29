def quadratic_equation(a, b, c):
    """
    Solves quadratic equations, input 'exit' or 'quit' to exit
    """
    while True:
        try:
            a1 =      float(a)
            b1 =            float(b)
            c1 =           float(c)
            quadratic_alpha_root = 0
            quadratic_beta_root = 0
            discriminant = (b1 ** 2 - (4 * a1 * c1))
            if discriminant >= 0:
                quadratic_alpha_root = (-b1 + (discriminant ** (1 / 2))) / (2 * a1)
                quadratic_beta_root = (-b1 - (discriminant ** (1 / 2))) / (2 * a1)
                break
            elif discriminant < 0:
                print(f'No real roots exist, although roots = {(-b1 + (discriminant ** (1 / 2))) / (2 * a1)} and '
                      f'{(-b1 - (discriminant ** (1 / 2))) / (2 * a1)}')
                print('Re-enter valid values')
                continue
        except Exception as e:
            print(f'Fatal error experienced: {e}')
    return quadratic_alpha_root, quadratic_beta_root


def square_limit_finder():
    """
    Using iteration gap, limit and the steps, this program finds all the numbers having their squares between 0 and the 
    limit alongside their squares, delay time is added for fancy work
    """
    from time import sleep
    print('-' * 73)
    print(f'Input the limit for which the square of consecutive numbers are contained')
    print('-' * 73)
    iteration = 0
    number = input('Limit: ')
    step = input('Input the steps to iterate through: ')
    time = input('Input the time for each new line to appear: ')
    result = 0
    print(f'Iteration for numbers with their square between {number}')
    try:
        number1 = float(number)
        step1 = float(step)
        time1 = float(time)
        while iteration ** 2 <= number1:
            iteration += step1
            result = f'{iteration}² = {iteration ** 2}'
            sleep(time1)
    except Exception as e:
        print(f'Fatal error experienced: {e}')
    return result


def rectangle_circle_area_perimeter_finder():
    """
    Evaluates the perimeter and area of either a rectangle or a circle based on the received information
    """
    from math import pi
    title = 'Rectangle/Circle area and perimeter solver'
    print('_' * len(title))
    print(title)
    print('_' * len(title))
    print('-' * 50)
    print('Rectangle and circle perimeter and area calculator')
    print('-' * 50)
    print(f'Are we working on a [r]ectangle or a [c]ircle? ')
    result = str()
    while True:
        shape = input()
        try:
            if shape == 'r':
                length = float(input('What\'s the length? '))
                breadth = float(input('And the breadth? '))
                perimeter = (length + breadth) * 2
                area = length * breadth
                result = f'Area is {area} and perimeter is {perimeter}'
                break
            elif shape == 'c':
                radius = float(input('For a circle, the radius is all we need: '))
                perimeter = 2 * pi * radius
                area = pi * radius ** 2
                result = f'Area is {area} and perimeter is {perimeter}'
                break
        except Exception as e:
            print(f'Unexpected error occurred: {e}')
            continue
    return result


def test_questions():
    """
    Adhoc geography test to measure my knowledge of use of nested loops and inline operators
    """
    title = 'Geography test'
    print('_' * len(title))
    print(title)
    print('_' * len(title))
    questions = ['What continent is Guadalupe found? ',
                 'What country borders USA to the north? ',
                 'What country uses more than one denomination for 1 currency value? ',
                 'What\'s the capital of Russia? ']
    answers = ['south america', 'canada', 'nigeria', 'moscow']
    output = 0
    while True:
        try:
            for question in questions:
                answer = input(question)
                for q_answer in answers:
                    if answer == q_answer:
                        output += 1
            break
        except Exception as e:
            print(f'Fatal error encountered: {e}')
            continue
    return f'You got {output}/{len(questions)}'




def calculator():
    """
    Two digit calculator for +, -, *, / and even power operations
    """
    title = 'Two digit calculator'
    print('_' * len(title))
    print(title.upper())
    print('_' * len(title))
    number = float(input('What is the number? '))
    operation = input('Operator: ')
    second = float(input('Working on? '))
    result = 0
    while True:
        try:
            if operation == '+':
                result = f'{number + second}'
                break
            elif operation == '-':
                result = f'{number - second}'
                break
            elif operation == '*':
                result = f'{number * second}'
                break
            elif operation == '/':
                result = f'{number / second}'
                break
            elif operation == ('^' or '**'):
                result = f'{number ** second}'
                break
        except Exception as e:
            print(f'Fatal error occurred: {e}')
            continue
    return result


def whatsapp_simulation():
    import time

    def whatsapp_init_login():
        import time
        name = 'Whatsapp'
        index = 1
        print(f'Welcome to {name}')
        time.sleep(2)
        print('Input your phone number: ')
        phone_number = input()
        print('Looks like you\'re new, how would you love to signup:')
        signup_decision = int(input(f'{index}. E-mail verification\n'
                                    f'{index + 1}. Missed call\n'
                                    f'{index + 2}. Verify through SMS\n'
                                    f'{index + 3}. Voice call\n'
                                    f'Input the index: '))
        if signup_decision == 1:
            time.sleep(1)
            six_digit_random()
        elif signup_decision == 2:
            print('Calling...')
            time.sleep(2)
            print(f'Missed call from {phone_number}')
            time.sleep(1)
            print('Verified')
        elif signup_decision == 3:
            time.sleep(3)
            print('You have an SMS')
            time.sleep(1)
            print('You have been verified')
        elif signup_decision == 4:
            time.sleep(1)
            print(f'{name} calling...')
            print('1. Answer')
            print('2. Decline')
            iv = input()
            if iv == 1:
                print('You have been verified')
            elif iv == 2:
                print('Answer to verify')
        else:
            print('Please input validly')

    print(whatsapp_init_login())
    print('Configuring, Please wait...')
    time.sleep(5)
    print('Done!')
    time.sleep(1)
    print('Start chatting...')
    time.sleep(2)
    print('Fatal error')


def six_digit_random():
    """
    Generates six pseudo-random numbers
    """
    import random
    import time
    number_1 = random.randint(0, 9)
    number_2 = random.randint(0, 9)
    number_3 = random.randint(0, 9)
    number_4 = random.randint(0, 9)
    number_5 = random.randint(0, 9)
    number_6 = random.randint(0, 9)
    number = f'{number_1}{number_2}{number_3}{number_4}{number_5}{number_6}'
    print('Type in the number that was sent to your e-mail')
    print(number)
    tries = 4
    while tries > 0:
        user_input = input('Input the 6 digits: ')
        if user_input == number:
            print('Input valid, you may continue')
            break
        else:
            tries -= 1
            print(f'Input invalid, you have {tries} more tries')
            continue
    if tries <= 0:
        print('You have been locked out!\n')
        time.sleep(1)
        print('Verify your account or create a new one')
    return number


print(quadratic_equation(1, 2, 3))