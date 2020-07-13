import re
import json

# Read from file or use the dummy data
with open("../data/input/j_select.cfg", "r") as f:
    s = f.read().replace('"','')

field_labels = [
                'SENDER', 
                'RECEIVER',
                'OBJ_CLASS',
                'JOBN_PAR',
                'CONVTAB'
                ]
# Define regex pattern and compile for speed
pat = '=([^\s]*)\s.*'.join(field_labels) + '=([^\s]*)\s'
pat = re.compile(pat)

# Extract target fields
data = pat.findall(s)
#print(data)

# Prepare a list of dicts: each dict for a single block of data
d = [dict((k,v) for k,v in zip(field_labels, field_values)) for field_values in data]
text = json.dumps({'data': d}, indent=2)
#print(text)
# Write to a json file
with open('../data/output/rules_output.json', 'w') as f:
    f.write(text)

print("JSON Created at data/output")
