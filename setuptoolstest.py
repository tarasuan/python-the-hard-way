import sys

try:
  import setuptools
except ImportError:
  sys.exit(1)
  print "exit 1"
else: 
  sys.exit(0)
  print "exit 2"
