import re
import json

# Read from file or use the dummy data
with open("../data/input/partner.cfg", "r") as f:
    s = f.read().replace

field_labels = [
                'PARTNER', 
                'ADDRESS1', 
                'DEPARTMENT', 
                'CONTACT_PERSON', 
                'TELEPHONE', 
                'FAX', 
                'EMAIL'
                ]
# Define regex pattern and compile for speed
pat = '="(.*)"\n\s*'.join(field_labels) + '="(.*)"'
pat = re.compile(pat)
print(pat)

# Extract target fields
data = pat.findall(s)

# Prepare a list of dicts: each dict for a single block of data
d = [dict((k,v) for k,v in zip(field_labels, field_values)) for field_values in data]
text = json.dumps({'data': d}, indent=2)
#print(text)
# Write to a json file
with open('../data/output/partner_output.json', 'w') as f:
    f.write(text)

print("JSON Created at data/output")