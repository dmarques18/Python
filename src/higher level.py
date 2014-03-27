__author__="dmarques"
__date__ ="$Mar 27, 2014 2:05:37 PM$"

if __name__ == "__main__":
    print "Hello World";
    
b=1
while b<=10:
    print b
    b+=1
    
list = ['soccer', 'football', 'hockey']
for food in list:
    print 'I play ' + food

ages = {'dad':40, 'mom':38, 'sister':20}
for item in ages:
    print item,' is ',ages[item],' years old.'

#infinite loop and break
while 1:
    name = raw_input('Enter name: ')
    if name == 'quit': break
