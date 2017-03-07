from rsa import rsa_edu
import time

for x in range(600, 2000):
	start = time.time()
	r = rsa_edu("hello world@!!!!!!!!", x)
	print r.dec, '\t' + str(len(bin(r.n))), '\t' + str(- (start - time.time()))