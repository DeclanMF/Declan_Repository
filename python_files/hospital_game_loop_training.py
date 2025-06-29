import time
print('_' * 20)
print('Hospital game')
print('_' * 20)
name  = input('Input your first name and last name? ')
age = input('How old are you? ')
is_patient = input('Have you been here before? ')
while True:
    if is_patient.lower() == ('yes' or 'true'):
        print('You can visit your assigned doctor.')
        time.sleep(2)
        print('You\'re with your doctor')
        time.sleep(5)
        print('You have cancer')
        time.sleep(2)
        print('You can: ')
        print(f'1. Commit suicide\n2. Treat it\n3. Call your wife\n4. Ask questions')
        choice = int(input(f'What do you do {name.lower()}? '))
        if choice == 1:
            time.sleep(1)
            print('You are dead')
        elif choice == 2:
            print('You\'re doctor is trying to save your life?')
            time.sleep(1)
            print('Treating...')
            time.sleep(5)

        elif choice == 3:
            print('Calling wife...')
            time.sleep(2)
            print('She\'s not around, leave a typed note...')
            time.sleep(1)
            input('Say something to your wife...')
            time.sleep(1)
            print('Sending...')
            time.sleep(1)
            print('Sent')
            time.sleep(1)
            print('You can: ')
            print(f'1. Commit suicide\n2. Treat it\n3. Ask questions')
            choice = int(input(f'What do you do {name.lower()}? '))
            if choice == 1:
                time.sleep(1)
                print('You are dead')
            elif choice == 2:
                print('You\'re doctor is trying to save your life?')
                time.sleep(1)
                print('Treating...')
                time.sleep(5)
            else:
                input()
                input("We'll see what we can do about it?")
        else:
            input()
    elif is_patient.lower() == ('no' or 'false'):
        print('You have to register first')
        print(f'Name = {name}')
        print(f'Age = {age}')
        registered_account_no = input('Input your acc number = ')
        continue
    else:
        print('Input true or false')