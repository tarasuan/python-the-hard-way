with open('test.txt', 'w') as f:
  f.write('This is a test, it is only a test')

with open('test.txt', 'r') as f:
  print f.read()