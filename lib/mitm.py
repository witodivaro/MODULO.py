import gmpy2 as math

from lib import mod


def find_mitm(hash, g, b, p):
    '''
        Finds (g^b)^x relative to the h / (g ^ x) in hash
    '''

    g_to_b_mod_p = mod.exp_mod(g, b, p)
    g_to_power = 1

    for x0 in range(1, b):
        g_to_power = mod.mul_mod(g_to_power, g_to_b_mod_p, p)

        try:
            x1 = hash[str(g_to_power)]
            return [x0, x1]
        except KeyError:
            pass

    return [None, None]
