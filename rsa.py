from math import sqrt
from primegen import randprime

class rsa_edu:
        def __init__(self, message, size):
                self.hi = ''.join(hex(ord(x))[2:] for x in message)
                self.hi = int(self.hi, 16)
                randprime1 = randprime(size)
                randprime2 = randprime(size)
                tot = (randprime2 - 1) * (randprime1 - 1)
                self.n = randprime1 * randprime2

                phi = [1 for x in range(2**16)]
                self.e = 3
                while True:
                        if phi[self.e] == 1 and tot%self.e != 0:
                                break
                        elif phi[self.e] == 1:
                                z = self.e
                                while z < len(phi)-1:
                                        phi[z] = 0
                                        z = z + self.e
                        self.e = self.e + 2
                self.k = 1
                while True:
                        if ((self.k*tot) + 1)%self.e == 0:
                                break
                        self.k = self.k + 1
                self.decrypt_key = ((self.k*tot) + 1)/self.e
                self.encrypt()

        def hextostring(self, message):
                i = 0
                self.dec = ''
                while i < len(message) - 1:
                        h = str(message[i]+ message[i+1])
                        i = i + 2
                        self.dec = self.dec + chr(int(h, 16))
				
						
        def encrypt(self):
                self.crypt = (self.hi**self.e)%self.n
                
        def decrypt(self):
                bd = bin(self.decrypt_key)
                sigma = 1
                for x in range(len(bd)-2):
                        if bd[len(bd) - (x+1)] is '1':
                                sigma = sigma * (self.crypt%self.n)
                        self.crypt = (self.crypt*self.crypt)%self.n
                u = sigma%self.n
                d = hex(u)[2:len(hex(u))]
                self.hextostring(d)

