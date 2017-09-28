str1= "iam 6'2\" tall." # escape double-quote inside string
str2='iam 6\'2" tall.' # escape single-quote inside string
print(str1)
print(str2)

tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""
print(tabby_cat)
print(persian_cat)
print(backslash_cat)
print(fat_cat)

# New code with format strings and escape characters
escape = '\none! \ntwo \nthree \nfour \nfive \nsix \nseven \nten: {}'
print(escape.format('\n\t100\n\t1000'))
