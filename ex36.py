from sys import exit

def losangeles():
  print "You touch down at LAX."
  print "As you leave the airport, a shifty man hands you another letter."

  choice = raw_input("> ")

  if "open" in choice or "read" in choice:
    print """
    Inside the envelope is a letter. It reads,
    'You have 30 minutes to find the stars and sun.'
    What do you do?
    """

    choice = raw_input("> ")
    
    if "taxi" in choice or "uber" in choice or "lyft" in choice:
      print "Great, on we go!\n"
    elif "metro" in choice:
      dead("Yeah right! Ha ha ha. You died!")
    else: 
      dead("Boop. You died.")
  else:
      dead("Boop. You died.")

  print "The driver asks you were you're headed."

  location = raw_input("> ")

  if "griffith" in location:
    print "Griffith Observatory, coming right up!"
  elif "beach" in location or "sea" in location:
    dead("Too literal! Try again.")
  else:
    dead("Sorry dude, that's not correct.")

  budget = budget - 50

  print "You arrived at your destination. That'll be $50."
  print "Your budget is now %s" % budget

  print "You go into the observatory and see the sun and stars."
  print "Congratulations! You solved the mystery of Los Angeles!"
  print "Let's go back to the airport. Anywhere else you'd like to go?"

  choice = raw_input("> ")

  if "san" in choice or "francisco" in choice:
    sanfrancisco()

def sanfrancisco():
  print "You touch down at SFO."
  print "As you leave the airport, another shifty man hands you *another* letter."

  choice = raw_input("> ")

  if "read" in choice or "open" in choice:
    print """
    Welcome to foggy San Francisco!
    Your mission is to find the lady in a wedding dress.
    Head downtown to begin your adventure.
    """
  else: 
    dead("Boop. You died. You need a lot of help!")

  print "How are you going to get to downtown?"

  while True:
    choice = raw_input("> ")

    if "bart" in choice:
      print "Now we're talking!"
    elif "cab" in choice or "uber" in choice or "taxi" in choice or "lyft" in choice:
      print "Ok, but that's going to cost you $80! Taxis are expensive and surge pricing applies."
      print ""
      budget = budget - 80
      print "Your budget is now %s" % budget
    else: 
      print "You can do it! Try again."

  print "Great! Let's get going downtown!"
  print "You get out of the cab at Market Street."
  print "Ahead of you is the Embarcadero. To the right is the Ferry Building."
  print "Which way?"

  while True:
    choice = raw_input("> ")

    if "ferry" in choice:
      ferry()
    else: 
      print "That's not quite right. Try again."

def ferry():
  print "you've made it to the ferry building."
  print "you look around and notice a man in a wedding dress"
  print "what do you do?"

  while True:
    choice = raw_input("> ")

    if "talk" in choice or "ask" in choice:
      print "The wedding dress man says,"
      print "/'You've found me! Congratulations!/'"
    else: 
      print "You can do it! Try again."

  brooklyn()


def dead(why):
  print why
  exit(0)

def start():
  name = raw_input("Hello what's your name?\n")
  print "Hi %s, you are at the beginning of a grand adventure!" % name  
  print "You will be given a mission to complete on each trip."
  print "Your budget is %s." % oldbudget
  print "Good luck!"

  raw_input("Press enter to continue.\n")

  chooser()

def chooser():
  print "You are at the airport! A shifty-looking fellow"
  print "hands you an envelope, and walks away."
  print "What do you do now?\n"

  choice = raw_input("> ")

  if "open" in choice or "read" in choice:
    print """
    Inside the envelope is a letter. It reads,
    'San Francisco or Los Angeles?'
    """

    while True:
      choice = raw_input("> ")

      if "san" in choice or "francisco" in choice:
        print "let's do this!"
        sanfrancisco()
      elif "los" in choice or "angeles" in choice or "LA" in choice:
        print "well ok, lets get going!"
        losangeles()
      else:
        print "Hm, this seems hard for you. Try again."

  else:
      dead("Boop. You died. Load the game and try again!")

  global budget = 200
start()