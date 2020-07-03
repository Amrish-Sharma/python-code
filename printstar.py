#Printing Star Tree in Python

#Function created to print the star tree
def printstar():
    star = "*" #taking star as variable so that we can use "times" 
    space=" "  #taking space in a variable to make sure the space stays in tree
    for i in range(1,10): #You can increase the range from 1 to 6
        print(space*(10-i)+star*i+star*(i-1))

printstar()