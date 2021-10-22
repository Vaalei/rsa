from numbers import Number
from random import choice
from math import sqrt
from time import time
from Crypto.Util import number
from functools import reduce
# pip install pycryptodome


primesUpToHundred = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

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


def getNumberFromFile(name):
    # Behövs inte
    file = open(name, "r")

    list = []

    for col in file:
        col = col.replace("\n", "")
        list.append(int(col))

    file.close()
    return list


def getCryptoPrimes(bit):
    num1 = number.getPrime(bit)
    num2 = number.getPrime(bit)
    return num1, num2


def getE(p,q):
    phi, mod = (p - 1) * (q - 1), p * q
    if mod < 65537:
        return (3, inv(3, phi), mod)
    else:
        return (65537, inv(65537, phi), mod)
    



def getLowestE(listOfEs, subtractedPrimes):
    for i in listOfEs:
        temp = 0
        while temp*i < subtractedPrimes:
            temp+=1
        if temp*i == subtractedPrimes:
            return i


def getD(e, f):
    d = 0 
    while True:
        d+=1
        if e * d % f == 1:
            return d 

        # If there are high primes involved, you may want to print how much it has computed
        if d % 10**8 == 0:
            print(str(d/10**8)+"*10^8")
        

def decrypt(hiddenMessage, sk, mod):
    decryptedMessage = pow(hiddenMessage, sk, mod)
    return decryptedMessage

def encrypt(message, pk, mod):
    return pow(message, pk, mod)


def getNumInput(shownText=""):
    string = input(shownText)
    if string == "": 
        return ""
    if string == "exit":
        return "exit"
    list = []
    for i in string:
        try:
            int(i)
            list.append(i)
        except:
            pass
    final = int("".join(list))
    return final

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


def getFastD(e, phi):
    d_old = 0; r_old = phi
    d_new = 1; r_new = e
    while r_new > 0:
        a = r_old // r_new
        (d_old, d_new) = (d_new, d_old - a * d_new)
        (r_old, r_new) = (r_new, r_old - a * r_new)
    return d_old % phi if r_old == 1 else None



def inv(p, q):
    """Multiplicative inverse"""
    def xgcd(x, y):
        """Extended Euclidean Algorithm"""
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


