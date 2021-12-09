import gmpy2 as math

from lib.mod import multiplyMod


def buildHashTable(h, g, b, p):
    '''
    Build (h / g ^ x) mod p hash table
    '''
    hash = {}

    gToMaxX = pow(g, b - 1)
    gToMaxXModP = math.f_mod(gToMaxX, p)
    gToMaxXModPInverted = math.invert(gToMaxXModP, p)
    hDividedByG = multiplyMod(h, gToMaxXModPInverted, p)
    hDividedByGModP = math.f_mod(hDividedByG, p)

    for x in range(b - 1, 1, -1):
        hash[str(hDividedByGModP)] = x

        # (ab) mod N == (a mod N)(b mod N) mod N
        # https://math.stackexchange.com/questions/2416119/rules-for-modulus-and-multiplication
        hDividedByGModP = multiplyMod(hDividedByGModP, g, p)

    return hash
