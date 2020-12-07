# get user input command line
fname = input('Enter a file: ')
if len(fname) < 1: fname = 'text.txt'

# non reccommended open syntax: must close
fh = open(fname)

for line in fh:
    print(line)
fh.close()

# recommended syntax
with open(fname) as fh:
    for line in fh:
        print('\n', line)