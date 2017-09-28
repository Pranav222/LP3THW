# assigning intiger value '10' in a variable.
types_of_people = 10
#assianinh string to varible x.
#This little f before the " (double-quote) and the {} characters tell Python
#this string needs to be formatted. Put these variables in there.
x = f"There are {types_of_people} types of people."
#assigning strings to variables.
binary = "binary"
do_not = "don't"
y = f"Those who know {binary} and those who {do_not}."
#prints the varibales x and y
print(x)
print(y)
#prints the variable in a formatted form
print(f"I said: {x}")
print(f"I also said: '{y}'")

hilarious = False
joke_evaluation = "Isn't that joke so funny?! {}"

print(joke_evaluation.format(hilarious))

w = "This is the left side of..."
e = "a string with a right side."
# Concatenation(w + e)
print(w + e)
