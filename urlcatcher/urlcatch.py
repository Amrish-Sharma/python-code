from bs4 import BeautifulSoup
import urllib.request, urllib.parse, urllib.error
import ssl
import re

#to ignore certificate issues
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#taking user inputs, cnt is the count and posistion taken as integer
url = input('Enter URL: ')
cnt =int(input('Enter count: '))
position=int(input('Enter position: '))

#to repeat cnt times
for i in range(cnt):
    #opening the url while ignoring the cert issues
    html = urllib.request.urlopen(url, context=ctx).read()
    #parsing the url with html.parser
    soup = BeautifulSoup(html, 'html.parser')
    #taking the anchor links
    tags = soup('a')
    #setting the count=0, this is counter variable not the cnt
    count = 0
    #looping through the anchor tags
    for tag in tags:
        count = count +1
        #until the position,we'll do nothing
        if count>position:
            break
        url = tag.get('href', None)
        #to get the name content from the tag href
        name=tag.contents[0]
#print the result along with the name
print(url)
print("Result is : ",name)