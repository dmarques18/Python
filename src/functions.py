__author__="dmarques"
__date__ ="$Mar 27, 2014 2:32:22 PM$"

def whatsup (x):
    return 'whats up ' + x

def plusten (y):
    return y + 10

def name (first='danny', last='marques'):
    print '%s %s' % (first, last)

if __name__ == "__main__":
    
    print whatsup('joe')

print plusten(6)
print name('joe')