
#declared and defined variables str1 and str2
str1 = "ff"
str2 = "fffffffffff"
#declared and defined variables num1 and num2
num1 = 23.3333
num2 = 4.1111
#calculating the len if the str2 to make same space in print
width=len(str2)

#using the formatting with width for the string st:<{width} 
#to make sure the variables are correctly formatted we are using variables st and num1 
print("str is {str1:<{width}} and num is {num1:15}".format(str1=str1, width=width, num1=num1))
print("str is {} and num is {:15}".format(str2, num2))