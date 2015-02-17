print "why hello there!"
print "what's your name?"

name = raw_input("> ")

if name == "jean":
  print "hi %s! Happy almost-birthday!" % name
else:
  print "hi %s! I could swear you were Jean, but ok!" % name

input("Press any key to continue")

print "Now %s, what year were you born?" % name

birth_year = int(raw_input("> "))

if birth_year == 1942:
  years_old = 2014 - birth_year
  print "That makes you %s years old!" % years_old

else:
  print "Hm, that's not what I heard!"

print "Ok, well. If you could relive any year from your past, what year would that be?"

past_year = int(raw_input("> "))

if past_year > 1972:
  print "why, that's after tara was born!"
else:
  years_old_again =  past_year - birth_year
  print "That's when you were %s years old!" % years_old_again
  print "That's nice!"
  print "Have a very happy birthday tomorrow!"
