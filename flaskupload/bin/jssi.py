import re
import json

# Read from file or use the dummy data
with open("../data/input/ssi.cfg", "r") as f:
    s = f.read()

field_labels = [
                'SLAVE',
                'SSI_SENDER', 
                'SSI_RECEIVER', 
                'COMMENT',
                'SENDER_EXT',
                'SENDER_COMMENT',
                'RECEIVER_EXT',
                'RECEIVER_COMMENT',
                'SSI_DATA',
                'SSI_DATA_COMMENT',
                'MESSAGEID'
                ]

# Define regex pattern and compile for speed
pat = '="(.*)"\n\s*'.join(field_labels) + '="(.*)"'
#print(pat)
pat = re.compile(pat)
#print(pat)
data=pat.findall(s)

# Prepare a list of dicts: each dict for a single block of data
d = [dict((k,v) for k,v in zip(field_labels, field_values)) for field_values in data]
text = json.dumps({'data': d}, indent=2)
#print(text)
# Write to a json file
with open('../data/output/ssi_output_demo.json', 'w') as f:
    f.write(text)

print("JSON Created at data/output")