import sys
import bz2
import binascii
import os

# Converting into .bz2 file

def Compresstobz2(path):
	bz2file = bz2.BZ2File(path+'.bz','wb')
	f = open(path,'rb')
	for i in f:
	    bz2file.write(i)

	bz2file.close()
	f.close()
	return path+'.bz'

# Remove me

def VanishMe(path):
	try:
		os.remove(path)
		return True
	except:
		return False

