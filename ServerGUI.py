import socket
import os
import sys
import bz2
import binascii
import ComPress
videoformat=set(['mp4','avi','flv','mkv'])
imageformat=set(['png','jpg','jpeg','bmp','gif'])
sock 	=	socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s=sys.argv[1]
print s
server_addr	=	(s,8000)
print >> sys.stderr,'starting up on %s port %s'%server_addr
sock.bind(server_addr)
sock.listen(1)
print >> sys.stderr,'waiting for connection'
connection , client	=	sock.accept()
while True:
	try:
		print >>sys.stderr, 'connection from', client
		filename	=	connection.recv(1024)
		ext=filename.split('.')[-1]
		if ext in videoformat:
			filepath='/home/shoyab/compressions/videos/'+filename
			bz2file=open(filepath+'.bz','wb')
		elif ext in imageformat:
			filepath='/home/shoyab/compressions/images/'+filename
			bz2file=open(filepath+'.bz','wb')
		else:
			filepath='/home/shoyab/compressions/text/'+filename
			bz2file=open(filepath+'.bz','wb')
		while True:
			data 	=	connection.recv(1024)
			if data=='EOFEOF':
				break
			if not data:
				bz2file.close()
				break
			bz2file.write(data)
			#print data
		connection.sendall('file received successfully\n')
		uncompress=open(filepath,'wb')
		bz2file=open(filepath+'.bz','rb')
		for i in bz2file:
			uncompress.write(i)
		bz2file.close()
		uncompress.close()
		os.remove(filepath+'.bz')
		print 'finally'
	finally:
		pass
		#connection.close()