import argparse
from isqrt import isqrt
from bitcash.format import coords_to_public_key, public_key_to_address

parser = argparse.ArgumentParser()
parser.add_argument('tag', help='the tag you want the bitcoin cash address to contain')
parser.add_argument('-t', '--testnet', help='if you want an address for testnet', action='store_true')
args = parser.parse_args()

TAG = bytearray(args.tag, encoding='ascii')
x = int(TAG.hex().ljust(64, '0'), 16)

p = 2**256 - 2**32 - 977
y = pow((x**3 + 7), (p+1)//4, p)

while ((y**2) % p) != (x**3 + 7) % p:
  x=x+1
  y = pow((x**3 + 7), (p+1)//4, p)

public_key = coords_to_public_key(x, y)
address = public_key_to_address(public_key, version=('test' if args.testnet else 'main'))
print('%s' % address)
