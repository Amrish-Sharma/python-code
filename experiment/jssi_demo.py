import re
import json

#to read the file and store the content in variabnle s
with open("ssi_demo.cfg", "r") as f:
    s = f.read()
    if "SLAVE" in s:
        print(s)
        



