print "Let's practice eveything."
print 'You\'d need to know \'bout escapes with \\ that do \n newlines and \t tabs, also \v tabs.'

poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and required an explanation
\n\t\vwhere there is none.
"""

print "---------------"
print poem
print "---------------"

five = (9+2) % 6
print "This should be five: %s" % five

def sec_form(start):
	jbeans = start * 500
	jars = jbeans / 1000
	crates = jars / 100
	return jbeans, jars, crates

start_pt = 1000
beans, jars, crates = sec_form(start_pt)

print "With a starting point of %d" % start_pt
print "We'd have %d beans, %d jars and %d crates." % (beans, jars, crates)

start_pt = start_pt / 10

print "We'd have %d beans, %d jars and %d crates." % sec_form(start_pt) 

