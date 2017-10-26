import requests
password=input(" password: ")
path=input(" path: ")
while True:
	command=input(" command: ")
	r=requests.post(path, data={ "password" : password, "command" : command})
	print(r.text)
