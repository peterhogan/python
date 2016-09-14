import csv
import random
b = open('test.csv', 'w')
a = csv.writer(b)
x = range(1,100)
y = random.gammavariate(2,3)
data = [['Me', 'You'],
        [x, y]]

matrix = [[random.gauss(2,3) for x in range(1),random.gammavariate(1,2) for x in range(2)] for x in range(100)]

a.writerows(matrix)
b.close()

