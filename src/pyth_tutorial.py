# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

__author__="dmarques"
__date__ ="$Mar 26, 2014 1:47:47 PM$"

#define function
def square (x):
 return x*x;

#user input
username=raw_input("Enter name: ");

#lists
family = ['mom', 'dad', 'bro', 'sis'];

#slicing
example=[0,1,2,3,4,5,6,7,8,9]

if __name__ == "__main__":
    print username;
    print family[2] #list indexing
    print example [4:8] #slicing
    print example [-5:];