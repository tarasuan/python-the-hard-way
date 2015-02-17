# get the argv module from sys
from sys import argv

#define the argv variables as "script" and "input_file"
script, input_file = argv

# create a function call print_all that takes an argument f
# and reads it.

def print_all(f):
  print f.read()

# create a function call rewind that takes an argument f
# and seeks it. Whatever that means.
def rewind(f):
  f.seek(0)

# create a function call print_a_line that takes two arguments, 
#line_count and f and prints the count and reads the lines?

def print_a_line(line_count, f):
  print line_count, f.readline()

#declare a variable called current_file which opens the 
# input_file argv

current_file = open(input_file)

print "First let's print the whole file:\n"

print_all(current_file)

print "Now let's rewind, kind of like a tape."

rewind(current_file)

print "Lets print three lines:"


#current_line is declared as 1. Current_file is the opened input_file
#current_line is passed in as the value for line_count in the function 
#print_a_line. So with those 2 parameters, print_a_line prints the nth
#line.
current_line = 1
print_a_line(current_line, current_file)

#current_line is declared as itself + 1. Current_file is the opened input_file
#current_line is passed in as the value for line_count in the function 
#print_a_line. So with those 2 parameters, print_a_line prints the nth
#line.

current_line += 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)