# this one is like your scripts with argv
def print_two(*args):
  arg1, arg2 = args
  print "arg1: %r, arg2: %r" % (arg1, arg2)

#ok the *args are actually pointless
def print_two_again(arg1, arg2):
  print "arg1: %r, arg2: %r" % (arg1, arg2)

# this takes just one argument
def print_one(arg1):
  print "arg1 %r" % arg1

# this one takes none
def print_none():
  print "Nuthin."

print_two("tara","zack")
print_two_again("tara","zack")
print_one("First!")
print_none()