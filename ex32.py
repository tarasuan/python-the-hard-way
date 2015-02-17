the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

#this for-loop goes through a list
for number in the_count:
  print "this is the count: %d" % number

# same as above
for fruit in fruits:
  print "A %s fruit" % fruit

# also notice we can go through mixed lists too
# notice we use %r since we don't know what's in it

for i in change:
  print "I got %r" % i

# we can also build lists, first start with empty
elements = []

# then use the range function to do the 0 to 5 counts
#for i in range(0, 6):
  #print "Adding %d to the list." % i
  #append is a function that lists understand
elements.append(range(0, 6))

# now we can print them out too
#for i in elements:
  #print "Element was %d." % i

print elements
