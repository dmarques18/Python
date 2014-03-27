__author__="dmarques"
__date__ ="$Mar 27, 2014 3:03:20 PM$"

fileWrite=open('/Users/dmarques/Documents/test.docx', 'w') #w = write
fileRead=open('/Users/dmarques/Documents/test.docx', 'r') #r=read

if __name__ == "__main__":
    
    fileWrite.write("hey now brown cow\nhello\ngoodbye\nwhat\nwhere")
    fileWrite.close()
    print fileRead.read()
    fileRead.close()