# -*- coding:utf-8 -*-
#5.5问题求解:猜数字游戏

import math
import random

def welcome_message():
  print 'Guess My Secret Number! '
  print 'This game allows you to guess a secret number by using'
  print 'information provided for you each time you guess. '
  print 'You only get a limited number of guesses,'
  print 'so think carefully about each guess. '

def setup():
  high_range = 100
  low_range = 1
  num_guess = 20
  response = " "
  given = 0
  print 'A secret number will be generated between 1 and 100. '
  print 'You can change these calues to any values'
  print 'that you want (whole number only)'
  print 'Do you want to select your own range?'
  print 'Type \'y\' for yes or \'n\' for no:'
  response = raw_input()
  if response == 'y':
    print 'Enter the low value of your desired range: '
    low_range = input()
    while int(low_range) != low_range:
      print 'You must enter a whole number. Try again: '
      low_range = input()
    print 'Enter the high value your desired range: '
    high_range = input()
    while int(high_range)!=high_range or high_range<=low_range:
      if int(high_range)!=high_range:
        print 'You must enter a whole number. Try again: '
        high_range = input()
      if high_range<=low_range:
        print 'The upper value must be greater than '
        print 'the lower value. Try again: '
        high_range = input()
    print 'The game normally allows a player 20 guess. '
    print 'Do you want to change the number of guesses allowed?'
    print 'Type \'y\' for yes or \'n\' for no. '
    response = raw_input()
    if response == 'y':
      print 'Enter the number of guesses you want to allow: '
      num_guess = input()
      while int(num_guess) != num_guess or num_guess<1:
        print 'You must enter a whole number greater than 0.'
        print 'Try again: '
        num_guess = input()
  given = math.floor(random.uniform(0,high_range-low_range+1))+low_range
  return low_range,high_range,num_guess,given

def game():
  while True:
    low_range,high_range,num_guess,given= setup()
    count = 1
    print 'I\'m thinking of a whole number '
    print 'between ',low_range,' and ',high_range
    print 'Can you guess the number? '
    print 'You have ',num_guess,' Chances to guess.'
    guess = input()
    if guess == given:
      print 'Wow! You won on the first try! '
    else:
      while count<=num_guess or guess!=given:
        while int(guess) != guess:
          print 'You must guess a whole number. '
          print 'Guess again.'
          guess = input()
        if guess<given:
          print 'Your guess is too low.Guess again:'
          guess = input()
        else:
          if guess>given:
            print 'Your guess is too high. Guess again:'
            guess = input()
          else:
            print 'Congratulation! You win!'
            break
    if count>num_guess and guess!=given:
      print 'Sorry. You have used up all your guesses. '
    print 'Do you want to play again? '
    print 'Type \'y\' for yes,\'n\' for no:'
    response = raw_input()
    if response != 'y':
      print 'Goodbye'
      break

welcome_message()
game()