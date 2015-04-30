x = "There are %d types of people." % 10 # just defining a variable with a %d formatter to show a number
binary = "binary" # defining a variable as a string
do_not = "don't" # same as above
y = "Those who know %s and those who %s." % (binary, do_not) # defining a string with two string formatters in

print x
print y

print "I said: %r." % x
print "I also said: '%s'." % y

hilarious = False # define a logical statement
joke_evaluation = "Isn't that a funny joke? %r" # define a varibale as a string with space for a formatter to be defined

print joke_evaluation % hilarious # print the above string with the formatter filled in 

w = "This is the left side of ..."
e = "a string with a right side."

print w + e
