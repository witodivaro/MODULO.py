import gmpy2
from time import time

from lib import table, mitm

# Hey Murphy!
# Thanks for visiting the repo, means a lot :)

p = gmpy2.mpz(
    13407807929942597099574024998205846127479365820592393377723561443721764030073546976801874298166903427690031858186486050853753882811946569946433649006084171)
g = gmpy2.mpz(11717829880366207009516117596335367088558084999998952205599979459063929499736583746670572176471460312928594829675428279466566527115212748467589894601965568)
h = gmpy2.mpz(3239475104050450443565264378728065788649097520952449527834792452971981976143292558073856937958553180532878928001494706097394108577585732452307673444020333)
b = gmpy2.mpz(pow(2, 20))

build_start_time = time()
hash = table.build_hash_table(h, g, b, p)
print(f'Hash table building took: {time() - build_start_time} seconds')

search_start_time = time()
[x0, x1] = mitm.find_mitm(hash, g, b, p)
print(f'Searching table took: {time() - search_start_time} seconds')

x = x0 * b + x1

print(x)
