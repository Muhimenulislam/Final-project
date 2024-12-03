import random

# Generate a random number between 1 and 10
secret_number = random.randint(1, 10)

print("Guess a number between 1 and 10!")

while True:
    guess = int(input("Your guess: "))
    if guess == secret_number:
        print("You guessed it right!")
        break
    else:
        print("Wrong guess. Try again!")
