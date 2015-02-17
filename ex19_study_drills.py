# trying to take user imput from terminal and use
#as an argument in a function :-(

def tea_party(tea_types):
  print "you have %d teas, yummy!"  % tea_types

tea_types = int(raw_input("how many teas do you want?"))

tea_party(tea_types)