import socket
import sys
import bz2
import binascii
import ComPress
import time
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = (sys.argv[1], 8000)
print >>sys.stderr, 'connecting to %s port %s' % server_address
sock.connect(server_address)
flag=1
while flag:
    try:
        path=raw_input("Enter full file path you want to compress and send over server")
        bzfilepath=ComPress.Compresstobz2(path)
        filename=path.split('/')[-1]
        sock.sendall(filename)
        bz2file = bz2.BZ2File(bzfilepath,'rb')
        while True:
            message=bz2file.readline()
            if message:
                sock.sendall(message)
            else:
                bz2file.close()
                break
        time.sleep(1)
        sock.sendall('EOFEOF')
        ComPress.VanishMe(bzfilepath)
        status=sock.recv(1024)
        print status
    except:
        flag=0
sock.close()
