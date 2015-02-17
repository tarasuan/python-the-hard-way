# defines a format as 4 replacements in a string
formatter = "%r %r %r %r"

#prints the formatter using the values provided
print formatter % (1, 2, 3, 4)
#same
print formatter % ("one", "two", "three", "four")
#same
print formatter % (True, False, False, True)
#prints itself
print formatter % (formatter, formatter, formatter, formatter)
#prints a more human complex set of strings
print formatter % (
  "I had this thing.",
  "That you could type up right.",
  "But it didn't sing.",
  "So I said goodnight."
)