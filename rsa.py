import random
import time
from math import sqrt
from primegen import randprime

def crypt(message):
	i = 0
	dec = ''
	if len(message)%2 == 1:
		end = len(message)
	else:
		end = len(message)  

	while i < len(message) - 1:
		h = str(message[i]+ message[i+1])
		i = i + 2
		dec = dec + chr(int(h, 16))
	print dec


start = time.time()

randprime1 = randprime(420)
randprime2 = randprime(420)
tot = (randprime2 - 1) * (randprime1 - 1)
n = randprime1 * randprime2

phi = [1 for x in range(2**16)]
e = 3
while True:
	if phi[e] == 1 and tot%e != 0:
		break
	elif phi[e] == 1:
		z = e
		while z < len(phi)-1:
			phi[z] = 0
			z = z + e
	e = e + 2

k = 1
while True:
	if ((k*tot) + 1)%e == 0:
		break
	k = k + 1

d = ((k*tot) + 1)/e

s = "hello world how's it going?"
hi = ''.join(hex(ord(x))[2:] for x in s)
hi = int(hi, 16)
c = (hi**e)%n

bd = bin(d)
sigma = 1
for x in range(len(bd)-2):
	if bd[len(bd) - (x+1)] is '1':
		sigma = sigma * (c%n)
	c = (c*c)%n

end = time.time()
print end - start
u = sigma%n
print len(str(n))
d = hex(u)[2:len(hex(u))]

crypt(d)
