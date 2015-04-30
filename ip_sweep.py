import os

#thirdoctet = raw_input('Subnet octet: ')
first_octets = raw_input('First three octets to scan: ')

fourthoctet_begin = input('Start sweep: ')
fourthoctet_end = input('End sweep: ')

for x in range(fourthoctet_begin,fourthoctet_end+1):
	test = os.system("ping -c 1 " + first_octets + str(x) + '> /dev/null 2>&1')
	if test == 0:
		print '%s%d is up.' % (first_octets,x)
	else:
		print '%s%d is down.' % (first_octets,x)

#for i in range(0,2):
#	for j in range(1,11):
#		print 'ping -c 1 192.168.%d.%d' % (i,j)
