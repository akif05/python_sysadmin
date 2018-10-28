# whith 0b in front we can declare byt data tipe
0b11110000

# or use bin(240) function to convert int to binary
bin(240)

# bin xor   = ^
bin(0b11100100 ^ 0b00100111)

v = 0b11110000
~v
-241

bin(~0b11110000 & 0b11111111)

bin(~0b11110000 & 0b111111111)

# ask python how many bits requird to represent integer
int(32).bit_length()
int(240).bit_length()
int(-240).bit_length()


int (0xcafebabe).to_bytes(length=4, byteorder='big')

int (0xcafebabe).to_bytes(length=4, byteorder='little')

import sys
sys.byteorder

little_cafebabe=int(0xcafebabe).to_bytes(length=4, byteorder=sys.byteorder)

int.from_bytes(little_cafebabe, byteorder=sys.byteorder)
# hex(_)

bytes()
bytes(5)
print(bytes(range(65, 65+26)))
print (bytes('Norwegian characters A and 0', 'utf16'))

bytes.fromhex('54686520717569636b2062726f776e20666f78')


# Convert each byt to its text representation striping x00 from each leading
''.join(hex(c)[2:] for c in b'The quick brown fox')

bytearray()
bytearray(b'')
bytearray(5)
print (bytearray(b'\x00\x00\x00\x00\x00'))
print (bytearray(b'Construct from sequence of bytes'))

pangram = bytearray(b'The quick brow fox')
pangram.extend(b' jumps over the lazy dog')
print (pangram)
# replace from 40 to 43 with god
pangram[40:43] = b'god'
print(pangram)

words = pangram.split()
print(words)
# Join back
print (bytearray(b' ').join(words))