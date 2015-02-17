from sys import argv
from os.path import exists

script, from_file, to_file = argv

print "Copying from %s to %s" % (from_file, to_file)

#we could do these two on one line, how?
#indata = open.read(from_file)
indata = open(from_file).read()

out_file = open(to_file, 'w')
out_file.write(indata)

print "Alright, done."

out_file.close()