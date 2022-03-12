import random
print("Checking test work with GIT")
def hangman():
    print("\n гр. RI1-02 X. Asad \n")
    print("Привет! Добро пожаловать в игру ВИСЕЛИЦА")

    wordlist = ['банан', 'арбуз', 'виноград', 'манго', 'яблоко']
    secret = random.choice(wordlist)
    guesses = 'бнзвдмгяко'
    turns = 5

    while turns > 0:
        missed = 0
        for letter in secret:
            if letter in guesses:
                print(letter,end='')
            else:
                print('_', end='')
                missed += 1

        if missed == 0:
            print('\n Ты выиграл!')
            break
        guess = input('\n Назови букву: ')
        guesses += guess

        if guess not in secret:
            turns -=1
            print('\n не угадал...')
            print('\n', 'Осталось попыток: ', turns)
            if turns < 5: print('\n  | ')
            if turns < 4: print('  o  ')
            if turns < 3: print(' /|\ ')
            if turns < 2: print('  |  ')
            if turns < 1: print(' /|\ ')
            if turns == 0: print('\n Это слова: ', secret)

ans = 'да'
while ans == 'да':
    hangman()
    print('Хочешь сыграть снова? (да или нет)')
    ans = input()