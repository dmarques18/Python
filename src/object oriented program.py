__author__="dmarques"
__date__ ="$Mar 27, 2014 2:48:16 PM$"

#create class
class exampleClass:
    eyes="blue"
    age=21
    def thisMethod(self):
        return 'hey this worked'

#create object
exampleObject=exampleClass()

if __name__ == "__main__":
    print exampleObject.eyes
    print exampleObject.thisMethod()
    
    
