import sys
import socket

wordlist = open("wordlist.txt", "rw+")

for i in wordlist:
	address = i.strip('\r\n') +'.' + sys.argv[1]+ ".com"
	try:
		add=socket.gethostbyaddr(address)
		print address, add[2][0]
	except:
		pass
	
