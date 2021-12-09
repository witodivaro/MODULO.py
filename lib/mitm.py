import gmpy2 as math

from lib.mod import addMod, multiplyMod


def findMITM(hash, g, b, p):
    '''
        Finds (g^b)^x relative to the h / (g ^ x) in hash
    '''

    gToB = pow(g, b)
    gToBModP = math.f_mod(gToB, p)
    gToPower = 1

    for x0 in range(1, b):
        gToPower = multiplyMod(gToPower, gToBModP, p)

        try:
            x1 = hash[str(gToPower)]
            return [x0, x1]
        except KeyError:
            pass

    return [None, None]
