from time import sleep

happiness = 0
sadness = 0
anxiety = 0
confidence = 0
emotion_limit = 10
while emotion_limit != 0:
    try:
        user_input = input('What emotion are you feeling in:\n'
                           '1. happiness\n2. sadness\n3. anxiety\n4. confidence\n').lower()
        if user_input == '1':
            happiness += 10
            emotion_limit -= 1
        elif user_input == '2':
            sadness += 10
            emotion_limit -= 1
        elif user_input == '3':
            anxiety += 3
            emotion_limit -= 1
        elif user_input == '4':
            confidence += 4
            emotion_limit -= 1
        else:
            print('We are not familiar with this input, type in the index of the value to move on')
            sleep(2.5)
            continue
    except Exception as e:
        print(f'Fatal error occurred: {e}')
