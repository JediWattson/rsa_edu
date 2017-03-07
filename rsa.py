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
                self.encrypt_key = 3
                while True:
                        if phi[self.encrypt_key] == 1 and tot%self.encrypt_key != 0:
                                break
                        elif phi[self.encrypt_key] == 1:
                                z = self.encrypt_key
                                while z < len(phi)-1:
                                        phi[z] = 0
                                        z = z + self.encrypt_key
                        self.encrypt_key = self.encrypt_key + 2
                self.k = 1
                while True:
                        if ((self.k*tot) + 1)%self.encrypt_key == 0:
                                break
                        self.k = self.k + 1
                self.decrypt_key = ((self.k*tot) + 1)/self.encrypt_key
                self.encrypt()
                self.decrypt()
				
        def hextostring(self, message):
                i = 0
                self.dec = ''
                while i < len(message) - 1:
                        h = str(message[i]+ message[i+1])
                        i = i + 2
                        self.dec = self.dec + chr(int(h, 16))
					
        def encrypt(self):
				be = bin(self.encrypt_key)
				sigma = 1
				for x in range(len(be) - 2):
						if be[-(x+1)] is '1':
								sigma = sigma*(self.hi%self.n)
						self.hi = (self.hi*self.hi)%self.n
				self.crypt = sigma%self.n
                
        def decrypt(self):
                bd = bin(self.decrypt_key)
                sigma = 1
                for x in range(len(bd)-2):
                        if bd[-(x+1)] is '1':
                                sigma = sigma * (self.crypt%self.n)
                        self.crypt = (self.crypt*self.crypt)%self.n
                u = sigma%self.n
                d = hex(u)[2:len(hex(u))]
                self.hextostring(d)

