import requests
import json

phonenumber = input("Enter phone number: ")
message=input("Type the message that you would like to send: ")

url = "https://www.fast2sms.com/dev/bulk"

payload = "sender_id=FSTSMS&message={0}&language=english&route=p&numbers={1}".format(message,phonenumber)
headers = {
    'authorization': "Iw1GCUNjSz3td8Mo5vErHF40mYbeAXOcpynsf9T2VhaP7ZQR6qtlwx0PKEegzVpHvBmR1TuZcyaQOUqS",
    'Content-Type': "application/x-www-form-urlencoded",
    'Cache-Control': "no-cache",
    }

response = requests.request("POST", url, data=payload, headers=headers)

json_object = json.loads(response.text)

print("Status:",json_object["message"])

#print(response.text)