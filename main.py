print('Guess the number between 1 and 10. You have 3 attempts.') 
 
num = 8
guess = 0
guess_limit=5
guess_number = 0
guess = int(input(f'Guess a number 1-10: '))
guess_number +=1
while guess_number < guess_limit:
    
    if guess != num:
        guess_number +=1
        if guess > num:
            guess = int(input(f'{guess} Too high - Guess again 1-10: '))
        else:
            guess = int(input(f'{guess} too low - Guess again 1-10: '))
    if guess == num:
        print(f'You Win! You Guessed it: {guess}')
        break
    
if guess != num:
    print(f'Sorry you lose! It was {num}')