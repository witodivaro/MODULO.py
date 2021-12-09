import gmpy2 as math


def multiplyMod(a, b, modulus):
    # (A * B) mod C = ((A mod C) * (B mod C)) mod C
    intermediateMultiplication = (
        math.f_mod(a, modulus)
        * math.f_mod(b, modulus)
    )

    return math.f_mod(intermediateMultiplication, modulus)


def addMod(a, b, modulus):
    aMod = a if a < modulus else a % modulus
    bMod = b if b < modulus else b % modulus

    # (A + B) mod C = (A mod C + B mod C) mod C
    intermediateAddition = (aMod * bMod)

    return math.f_mod(intermediateAddition, modulus)
