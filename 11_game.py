import random

options = ('rock', 'paper', 'scissors')

computer_wins = 0
user_wins = 0

rounds = 1

while True:

  print('*' * 10)
  print('ROUND', rounds)
  print('*' * 10)

  print('computer_wins', computer_wins)
  print('user_wins', user_wins)

  user_option = input('rock, paper or scissors => ')
  user_option = user_option.lower()

  rounds += 1

  if not user_option in options:
    print('That option is not valid')
    continue

  computer_option = random.choice(options)

  print('User option =>', user_option)
  print('Computer option =>', computer_option)

  if user_option == computer_option:
      print('Tie!')
  elif user_option == 'rock':
      if computer_option == 'scissors':
          print('rock wins scissors')
          print('user won!')
          user_wins += 1
      else:
          print('paper wins rock')
          print('computer won!')
          computer_wins += 1
  elif user_option == 'paper':
      if computer_option == 'rock':
          print('paper wins rock')
          print('user won')
          user_wins += 1
      else:
          print('scissors wins paper')
          print('computer won!')
          computer_wins += 1
  elif user_option == 'scissors':
      if computer_option == 'paper':
          print('scissors wins paper')
          print('user won!')
          user_wins += 1
      else:
          print('rock wins scissors')
          print('computer won!')
          computer_wins += 1

  if computer_wins == 2:
    print('The winner is the computer')
    break

  if user_wins == 2:
    print('The winner is the user')
    break
