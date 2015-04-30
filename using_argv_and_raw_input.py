from sys import argv

script, first, second, third = argv

input = raw_input("Type something here: ")
print """the script is called %s, the first variable is %s,
	the second and third are %s and %s, respectively,
	AND you typed %s.""" % (script, first, second, third, input)
