with open('rssfeeds.txt') as rssfile:
    lines = rssfile.read().splitlines()
for line in lines:
    if line.startswith('http'):
        print(line)
    else: 
        pass
