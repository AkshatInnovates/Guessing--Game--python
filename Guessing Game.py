import random
random.randint(1,100)
jackpot = random.randint(1, 100)

guess = int(input("Guess the Number:"))
counter = 1
while guess != jackpot:
    if guess < jackpot:
        print("Guess Higher")
    else:
        print("Guess Lower")

    guess = int(input("Guess the Number:"))
    counter += 1

print("Sahi jawab")
print('You took', counter, 'attempt')