from sys import argv

script, filename, fileagain = argv
prompt = '>'

txt = open(filename)

print "Here's your file %r:" % filename
print txt.read()

print "Type the %r :" fileagain
fileagain = raw_input(prompt)

print "Here's your fil %r" % fileagain
print fileagain.read()