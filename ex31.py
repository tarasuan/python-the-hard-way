#first game

print "You enter a dark room with two doors. Do you go through door #1 or door #2?"

door = raw_input("> ")

if door == "1":
  print "There's a giant bear here eating a cheese cake. What do you do?"
  print "1. Take the cake."
  print "2. Scream at the bear."

  bear = raw_input("> ")

  if bear == "1":
    print "The bear eats your face off. Good job!"
  elif bear == "2":
    print "The bear eats your legs off. Good job!"
  else:
    print "Bear ran away. Well, doing %s was better." % bear

elif door == "2":
  print "You stare into the endless abyss at Cthulhu's retina."
  print "1. Blueberries."
  print "2. Yellow jacket clothespins."
  print "3. Understanding revolvers yelling melodies."

  insanity = raw_input("> ")

  if insanity == "1" or insanity == "2":
    print "Your body survives powered by a mind of jello. Good job!"
  else: 
    print "The insanity rots your eyes into a pool of muck. Good job!"

else:
  print "You stumble around and fall on a knife and die. Good job!"

#new game
print "You are raised from the dead and have one more chance. Do you drink, eat or sleep?"

do = raw_input("> ")

if do == "eat":
  print "that's delicious, now what? go back or forward?"

  go = raw_input("> ")

  if go == "back":
    print "ok you're back"
  elif go == "forward":
    print "onward we go!"
  else:
    print "well if you say so"

elif do == "drink":
  print "my that was thirst quenching, how about a snacK?"
  print "1. yes"
  print "2. no"

  snack = raw_input("> ")

  if snack == "1":
    print "that was delicious."
  else:
    print "fine then, party pooper."

elif do == "sleep":
  print "ok, but would you like to shower or poop first?"

  like = raw_input("> ")

  if like == "shower" or "poop":
    print "boy that felt good"
  else:
    print "well if you say so"

else:
  print "you died. I guess %s wasn't a great idea!" % do