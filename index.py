import time

name = raw_input("What is your name? ")

print "Hello,", name + "! Time to play hangman!"

time.sleep(1)

print "Start guessing..."
time.sleep(0.5)

word = "secret"

guesses = ""

turns = 10

while turns > 0:
    failed = 0

    for letter in word:
        if letter in guesses:
            print letter,
        else:
            print "_",
            failed += 1

    if failed == 0:
        print "You won"
        break
    
    guess = raw_input("guess a character: ")
    guesses += guess
    if guess not in word:
        turns -= 1
        print "No dice!"
        print "You have", str(turns), "more guesses..."

    if turns == 0:
        print "Game over!"