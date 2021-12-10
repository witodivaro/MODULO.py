import gmpy2 as math

from lib import mod


def build_hash_table(h, g, b, p):
    """Builds hash table for h / (g^x)"""

    hash = {}

    g_to_max_x_mod_p = mod.exp_mod(g, b - 1, p)
    g_to_max_x_mod_p_inverted = math.invert(g_to_max_x_mod_p, p)

    h_divided_by_g_mod_p = mod.mul_mod(h, g_to_max_x_mod_p_inverted, p)

    for x in range(b - 1, 1, -1):
        hash[str(h_divided_by_g_mod_p)] = x

        h_divided_by_g_mod_p = mod.mul_mod(h_divided_by_g_mod_p, g, p)

    return hash
