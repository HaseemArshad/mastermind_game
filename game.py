import random

COLORS = ["R", "G", "B", "Y", "W", "O"]
TRIES = 10
CODE_LENGTH = 4

def generate_code():
    return [random.choice(COLORS) for _ in range(CODE_LENGTH)]

def guess_code():
    while True:
        guess = input("Guess (or type 'GIVE UP' to quit, 'HINT' for help): ").upper()
        
        if guess == "GIVE UP":
            return "GIVE UP"
        
        if guess == "HINT":
            return "HINT"

        guess = guess.split(" ")
        if len(guess) != CODE_LENGTH:
            print(f"You must guess {CODE_LENGTH} colors!")
            continue

        for color in guess:
            if color not in COLORS:
                print(f"Invalid color: {color}. Please try again!")
                break
        else:
            return guess

def check_code(guess, real_code):
    color_counts = {}
    correct_position = 0
    incorrect_position = 0

    for color in real_code:
        if color not in color_counts:
            color_counts[color] = 0
        color_counts[color] += 1

    # Check for correct positions
    for i, (guess_color, real_color) in enumerate(zip(guess, real_code)):
        if guess_color == real_color:
            correct_position += 1
            color_counts[guess_color] -= 1

    # Check for incorrect positions
    for i, guess_color in enumerate(guess):
        if guess[i] != real_code[i] and guess_color in color_counts and color_counts[guess_color] > 0:
            incorrect_position += 1
            color_counts[guess_color] -= 1

    return correct_position, incorrect_position

def game():
    print(f"Welcome to Mastermind! You have {TRIES} tries to guess the code.")
    print("The valid colors are:", *COLORS)
    code = generate_code()

    for attempts in range(1, TRIES + 1):
        guess = guess_code()

        if guess == "GIVE UP":
            print(f"You gave up! The code was:", *code)
            break
        
        if guess == "HINT":
            hint_color = random.choice(code)
            print(f"Hint: One of the colors in the code is {hint_color}.")
            continue

        correct_position, incorrect_position = check_code(guess, code)

        if correct_position == CODE_LENGTH:
            print(f"You guessed the code correctly in {attempts} tries!")
            break

        print(f"Correct Positions: {correct_position} | Incorrect Positions: {incorrect_position}")

    else:
        print("You ran out of tries. The code was:", *code)

if __name__ == "__main__":
    game()
