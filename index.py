import time
import random

name = raw_input('What is your name? ')

print 'Hello,', name + '! Time to play hangman!'
time.sleep(1)
print 'Start guessing...'
time.sleep(0.5)

words = ['secret', 'forever', 'cruise', 'healthy', 'vegetarian']
word = random.choice(words)
guesses = ''
turns = 10

while turns > 0:
  word_count = len(word)

  for letter in word:
    if letter in guesses:
      word_count -= 1
      print letter,
    else:
      print '_',

  if word_count == 0:
    print 'You won'
    break

  guess = raw_input('guess a character: ')
  if guess in guesses:
    print 'You already guessed ' + guess + '!'
  elif guess not in word:
    turns -= 1
    print 'No dice!'
    print 'You have', str(turns), 'more guesses...'

  guesses += guess

  if turns == 0:
    print 'Game over!'