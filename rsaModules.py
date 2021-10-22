from numbers import Number
from random import choice
from math import sqrt
from time import time
try:
    from Crypto.Util import number # pip install pycryptodome
except:
    print('module Crypto not found \nuse "pip install pycryptodome" to install it')
from functools import reduce



# https://www.geeksforgeeks.org/prime-factor/
def primeFactors(n):
    list = []
    while n % 2 == 0:
        list.append(2),
        n = n / 2
    for i in range(3, int(sqrt(n))+1, 2):
        while n % i == 0:
            list.append(int(i)),
            n = n / i   
    if n > 2:
        list.append(int(n))
    return list


def getCryptoPrimes(bit):
    num1 = number.getPrime(bit)
    num2 = number.getPrime(bit)
    return num1, num2


def getKeys(p,q):
    phi, mod = (p - 1) * (q - 1), p * q
    if mod < 65537:
        return (3, inv(3, phi), mod)
    else:
        return (65537, inv(65537, phi), mod)
    

def decrypt(hiddenMessage, sk, mod):
    decryptedMessage = pow(hiddenMessage, sk, mod)
    return decryptedMessage

def encrypt(message, pk, mod):
    return pow(message, pk, mod)


def removeLetters(string):
    list = []
    for i in string:
        try:
            int(i)
            list.append(i)
        except:
            pass
    final = int("".join(list))
    return final 


def inv(p, q):
    # Multiplicative inverse
    def xgcd(x, y):
        # Extended Euclidean Algorithm
        s1, s0 = 0, 1
        t1, t0 = 1, 0
        while y:
            q = x // y
            x, y = y, x % y
            s1, s0 = s0 - q * s1, s1
            t1, t0 = t0 - q * t1, t1
        return x, s0, t0      
 
    s, t = xgcd(p, q)[0:2]
    assert s == 1
    if t < 0:
        t += q
    return t


# credit : http://jhafranco.com/2012/01/29/rsa-implementation-in-python/ 
# for both text2Int & int2Text
def text2Int(text):
    """Convert a text string into an integer"""
    return reduce(lambda x, y : (x << 8) + y, map(ord, text))
 
def int2Text(number, size):
    """Convert an integer into a text string"""
    text = "".join([chr((number >> j) & 0xff)
                    for j in reversed(range(0, size << 3, 8))])
    return text.lstrip("\x00")

def modSize(mod):
    """Return length (in bytes) of modulus"""
    modSize = len("{:02x}".format(mod)) // 2
    return modSize

if __name__ == "__main__":
    print(getCryptoPrimes(128))


