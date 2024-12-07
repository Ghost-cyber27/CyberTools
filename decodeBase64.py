import base64

data = "Input encrypted data here"

while 'picoCTF' not in data:
    data = base64.b64decode(data).decode('utf8')

print(data)