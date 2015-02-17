numbers = []

def make_list():

  for i in range(0, 12):
    print "At the top, i is %d" % i
    numbers.append(i)
    print "Numbers now: ", numbers
    print "At the bottom, the i is %d" % i

make_list()

print "The number: "
for num in numbers:
  print num