from sys import argv

script, user_name = argv
prompt = '>'

print "Hi %s, I'm the %s script." % (user_name, script)
print "I'd like to ask you a few questions."
print "Is your name %s?" % user_name
name = raw_input(prompt)

print "Where do you live, %s?" % user_name
live = raw_input(prompt)

print "What computer do you have?"
comp = raw_input(prompt)

print """
So you said %s to your name being %s,
you live in %s, and you have a %s computer.
""" % (name, user_name, live, comp)
