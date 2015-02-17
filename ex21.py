def add(a, b):
  print "ADDING %d + %d" % (a, b)
  return a + b

def subtract(a, b):
  print "SUBTRACTING %d - %d" % (a, b)
  return a - b

def multiply(a, b):
  print "MULTIPLYING %d * %d" % (a, b)
  return a * b

def divide(a, b):
  print "DIVIDING %d / %d" % (a, b)
  return a / b

print "Let's do some math with just functions!"

age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

print "Age: %d, Height: %d, Weight: %d, IQ: %d" % (age, height, weight, iq)

# A puzzle for the extra credit, type it in anyway.
print "Here is a puzzle."

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

print "That becomes: ", what, "Can you do it by hand?"

what3 = age + (height - (weight * (iq / 2)))

print "what3 becomes:", what3, "SEE???"

what_inverse = subtract(iq, divide(height, multiply(age, add(weight, 2.))))

print "Inverse becomes: ", what_inverse, "OMG!"

  