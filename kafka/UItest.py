import sys
from time import sleep

j = 3
k = 1
l = 100

for i in range(10):
    sleep(0.1)
    j+=1
    sleep(0.1)
    k+=3
    l+=43
    sleep(0.1)
    print('\rFiles read:',i,end="\n")
    print('\rFiles read:',i,end="\r")
    '''
    \rFiles skipped: %i 
    \rGUID log file size: %i
    \rTotal downloaded: %i '% (i,j,k,l), end="")
    '''
    """
    print('\rFiles read: %i' % i, end="")
    sys.stdout.flush()
    """
print('')
