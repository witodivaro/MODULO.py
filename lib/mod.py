import gmpy2 as math
from lib import helpers


def mul_mod(a, b, modulus):
    """Modular Multiplication

    (ab) mod N == (a mod N)(b mod N) mod N
    https://math.stackexchange.com/questions/2416119/rules-for-modulus-and-multiplication

    Args:
        a (int): multiplied
        b (int): multiplier
        modulus (int): mod

    Returns:
        int: multiplication result
    """

    intermediate_mult = (
        math.f_mod(a, modulus)
        * math.f_mod(b, modulus)
    )

    return math.f_mod(intermediate_mult, modulus)


def add_mod(a, b, modulus):
    aMod = a if a < modulus else a % modulus
    bMod = b if b < modulus else b % modulus

    # (A + B) mod C = (A mod C + B mod C) mod C
    intermediateAddition = (aMod * bMod)

    return math.f_mod(intermediateAddition, modulus)


def exp_mod(base, power, modulus):
    """Modular Exponentiation

    Fast algorithm using binary power
    https://ru.wikipedia.org/wiki/%D0%92%D0%BE%D0%B7%D0%B2%D0%B5%D0%B4%D0%B5%D0%BD%D0%B8%D0%B5_%D0%B2_%D1%81%D1%82%D0%B5%D0%BF%D0%B5%D0%BD%D1%8C_%D0%BF%D0%BE_%D0%BC%D0%BE%D0%B4%D1%83%D0%BB%D1%8E#CITEREF%D0%A2%D0%B5%D0%BE%D1%80%D0%B5%D1%82%D0%B8%D1%87%D0%B5%D1%81%D0%BA%D0%B8%D0%B9_%D0%BC%D0%B8%D0%BD%D0%B8%D0%BC%D1%83%D0%BC_%D0%B8_%D0%B0%D0%BB%D0%B3%D0%BE%D1%80%D0%B8%D1%82%D0%BC%D1%8B_%D1%86%D0%B8%D1%84%D1%80%D0%BE%D0%B2%D0%BE%D0%B9_%D0%BF%D0%BE%D0%B4%D0%BF%D0%B8%D1%81%D0%B82010


    Args:
        base (int): base
        power (int): power
        modulus (int): mod

    Returns:
        int: result
    """

    power_binary = helpers.convert_to_binary(power)

    result = 1

    for i in range(0, len(power_binary)):
        bit = power_binary[i]

        if (bit == '1'):
            result = mul_mod(result, base, modulus)

        if (i != len(power_binary) - 1):
            result = mul_mod(result, result, modulus)

    return result
