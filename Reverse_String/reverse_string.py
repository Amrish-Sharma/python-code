#!/usr/bin/env python3

class ReverseString:
    def __init__(self,string):
        self.string= string

    def reverse_string(self):
        input_string = self.string
        input_list= input_string.split(" ")
        reverse_string= " ".join(str(x) for x in input_list[::-1])
        return reverse_string

use_string=input("Enter The String That You Want to Reverse: ")
rs=ReverseString(use_string)
print(rs.reverse_string())




