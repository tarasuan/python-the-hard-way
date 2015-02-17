from sys import exit
import random
from random import randint

class Scene(object):

  def enter(self):
    print "This scene is not yet configured. Subclass it and implement enter()."
    exit(1)

class FlipCoin(Scene):

  def enter(self):
    wins = 0
    print "\n\n\n\nYou and Chevy go to your first game. The dealer says,"
    print "'Call this coin when I flip it in the air. Ready?'"

    coin = ("heads", "tails")
    flip = random.choice(coin)
    print flip

    guess = raw_input("Call it! ")

    if flip == guess:
      wins += 1
      print "you win"

    else:
      print "you lose"

    raw_input("press enter to continue")
    
    return 'pick_a_number'


class PickNumber(Scene):
  def enter(self):
    print "You and Chevy make your way to the next game."
    print "Pick a number between 1 and 10."
    print "You have 5 tries."

    number = randint(0,9) 
    print number
    tries = 1

    guess = raw_input("Pick a number between 1 and 10. ")
    #need to do a check here to make sure guess isn't blank?
    guess = int(guess)

    while guess != number  and tries < 5:
      tries += 1
      print "Wrong! Go again."
      guess = raw_input("Pick a number between 1 and 10. ")

    if int(guess) == number:
      print "You win!\n\n\n"

    else:
      print "you lose\n\n\n"

    return 'war'


class War(Scene):
  def enter(self):
    print "Fresh and undaunted, the dynamic duo heads for the next game."
    print "The dealer says, 'Ready for War?'"
    print "First to three wins the game."

    raw_input("Press Enter to deal")

    # need to account for A being high and low.
    deck = {'1':'A', '2':'2', '3':'3', '4':'4', '5':'5', '6':'6', '7':'7', 
    '8':'8', '9':'9', '10':'10', '11':'J', '12':'Q', '13':'K'}

    your_count = 0
    my_count = 0

    while your_count < 3 and my_count < 3:
      my_deal = random.choice(deck.keys())
      your_deal = random.choice(deck.keys())
      print "Your card is %s" % deck.get(your_deal)
      print "My card is %s" % deck.get(my_deal)

      if int(your_deal) > int(my_deal):
        your_count += 1
        print "You won this hand"
        print "The score is %s to %s" % (your_count, my_count)

      elif int(your_deal) == int(my_deal):
        print "Tie, go again"

      else:
        my_count += 1
        print "You lost this hand"
        print "The score is %s to %s" % (your_count, my_count)

      raw_input("Press Enter to continue...")

    if your_count == 3:
      print 'You have won. Congratulations!'

    else:
      print "You have lost this game. So sad."

    raw_input("Press Enter to continue")
    return 'rock_paper_scissors'

class RockPaperScissors(Scene):
  def enter(self):
    print "On to the next game. Rock Paper Scissors? Best of 3 wins."
    print "Type rock, paper, or scissors to play."

    your_count = 0
    my_count = 0

    dealer = ['rock', 'paper', 'scissors']

    while your_count < 3 and my_count < 3:
      _choice = raw_input("Ready? Rock, Paper, Scissors!")
      dealer_choice = random.choice(dealer)
      print "You chose %r and dealer chose %s" % (_choice, dealer_choice)

      if _choice == "rock" and dealer_choice == "scissors":
        your_count += 1
        print "You won this hand"
        print "The score is %s to %s" % (your_count, my_count)

      elif _choice == "paper" and dealer_choice == "rock":
        your_count += 1
        print "You won this hand"
        print "The score is %s to %s" % (your_count, my_count)  

      elif _choice == "scissors" and dealer_choice == "paper":
        your_count += 1
        print "You won this hand"
        print "The score is %s to %s" % (your_count, my_count)

      elif _choice == dealer_choice:
        print "Tie, go again"

      else:
        my_count += 1
        print "You lost this hand"
        print "The score is %s to %s" % (your_count, my_count)

    raw_input("Press Enter to continue...")

    if your_count == 3:
      print 'You have won. Congratulations!'

    else:
      print "You have lost this game. So sad."

    raw_input("Press Enter to continue")

    return 'cash_out'

class Death(Scene):
  def enter(self):
    print "You died."

class CashOut(Scene):
  def enter(self):
    print "Cashing out?"
    print "Good job, you helped Chevy Chase save his family!"