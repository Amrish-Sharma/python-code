import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:

    url = input("Enter the full url address: ")
    #hostname = urlparse(url).netloc
    hostname=url.split('/')[2]
    print(hostname)
except:
    print('URL entered is not in correct format')
    print('Please enter url in format http://hostame.com/path/to/the/url')
    print('or in format https://hostame.com/path/to/the/url')
#added try/except blocks
try:
    mysock.connect((hostname, 80))
    cmd = 'GET {0} HTTP/1.0\r\n\r\n'.format(url).encode()
    mysock.sendall(cmd)
    count=0
    while True:
        
        data = mysock.recv(512)
        if len(data) < 1:
            break
        
        if count < 3000:
            count = count + len(data)
            print(data.decode(),end='')
    print('\n Total Count of Characters: ',count)    
    mysock.close()
except:
    print('something is not right')
