from rsa import rsa_edu
import time

for x in range(300, 2000):
	start = time.time()
	r = rsa_edu("hello world@!!!!!!!!", x)
	r.decrypt()
	print  
	print r.dec, '\t' + str(x), '\t' + str(- (start - time.time()))