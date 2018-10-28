
# Demo of reading the bynary file created from bynary.c file
# each line is as folowing
# 4bytes+20+4+4pading+8 = 40bytes in total

# 4 bytes for position
# 20 bytes for name
# 4 bytes for moons
# 4 bytes for padding
# 8 bytes fo mass
# Pading is added because
# mass is double and needs 8byte
# needs to bi inside of multiple of 8
# Thats why is jumping in next

import struct
record_size = 40 # No of bytes in a planet record

# Just read the fifth record
with open("planets.dat", "rb") as file:

    #Get the record in 5th line, which is record for Jupiter
    file.seek(4 * record_size)

    # Read it into content
    content = file.read(record_size)

    # Unpack the content to variables, and then strip \0's from C string
    # @i20sid means that data is stored using this machine native format
    pos, name, moons, mass = struct.unpack("@i20sid", content)
    name = name.decode().rstrip("\0")
    print ("%d: %8s: %2d moons, mass = %6.2f" % (pos, name, moons, mass))

with open("planets.dat", "rb") as file:
    content = file.read()
    for pos, name, moons, mass in struct.iter_unpack("@i20sid", content):
        name = name.decode().rstrip("\0")
        print("%d: %8s: %2d moons, mass = %6.2f" % (pos, name, moons, mass))