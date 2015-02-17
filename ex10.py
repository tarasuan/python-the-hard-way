tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \ a \\ cat."
singlequote_cat = 'I\'m single quote cat.'
carriagereturn_cat = "I'm \r ASCII a \r ASCII cat."
verticaltab_cat = "I'm \v vertical tab \v cat."
complicated_cat = '''
I'm a \v vertical tab \v cat
with a \"love\" for 
\t sounds like this \a
\t on their own lines
or like \r ASCII this.
'''
cat_leisure = "rest"
cat_leisure2 = "relaxation"
combo_cat = "I need \nsome \n\"%s and %s\"." % (cat_leisure, cat_leisure2)

fat_cat = '''
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
'''

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat
print singlequote_cat
print carriagereturn_cat
print verticaltab_cat
print complicated_cat
print combo_cat