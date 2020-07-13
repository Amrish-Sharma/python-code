import re

with open("../data/input/j_select_demo.cfg", "r") as f:
    s = f.read().replace('"','')

field_labels = [
                'SENDER', 
                'RECEIVER',
                'OBJ_CLASS',
                'JOBN_PAR',
                'CONVTAB'
                ]

pat = '=([^\s]*)\s.*'.join(field_labels) + '=([^\s]*)\s'
pat = re.compile(pat)

print(pat)

data = pat.findall(s)

print(data)

