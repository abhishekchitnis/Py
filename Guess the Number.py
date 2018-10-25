import random

guesses_made = 0

name = input('Hello! \nWelcome to Guess the Number in My Mind \nMy Name is Abhishek!!! \nWhat is your Name? : ')

number = random.randint(1, 20)
print ('Well, {0}, I am Thinking of a Number Between 1 and 20.'.format(name))
print('Can you Guess the Number!')

while guesses_made < 6:

    guess = int(input('Enter your Guess Here : '))

    guesses_made += 1

    if guess < number:
        print ('Your Guess is Too Low. Try to Go Higher and Guess the Number Again.')

    if guess > number:
        print ('Your guess is Too High. Try to Go Lower and Guess the Number Again.')

    if guess == number:
        break

if guess == number:
    print ('Congratulations, {0}! You Guessed my Number in {1} Guesses!'.format(name, guesses_made))
else:
    print ('Sorry you Exceded your Choices. The Number I was Thinking of is {0}'.format(number))