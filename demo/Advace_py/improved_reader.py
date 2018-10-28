import struct
from pprint import pprint as pp
from binascii import hexlify

class Vector:

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __repr__(self):
        return 'Vector({}, {}, {})'.format(self.x, self.y, self.z)

class Color:

    def __init__(self, red, green, blue):
        self.red = red
        self.green = green
        self.blue = blue

    def __repr__(self):
        return 'Color({}, {}, {})'.format(self.red, self.green, self.blue)

class Vertex:

    def __init__(self, vector, color):
        self.vector = vector
        self.color = color

    def __repr__(self):
        return 'Vertex({!r}, {!r})'.format(self.vector, self.color)

def make_colored_vertex(x, y, z, red, green, blue):
    return Vertex(Vector(x, y, z),
                  Color(red, green, blue))


def main():
    with open('colors.bin', 'rb') as f:
        buffer = f.read()

    ## For debuging
    print("buffer: {} bytes".format(len(buffer)))

    indexes = ' '.join(str(n).zfill(2) for n in range(len(buffer)))
    print (indexes)

    hex_buffer = hexlify(buffer).decode('ascii')
    hex_pairs = ' '.join(hex_buffer[i:i+2] for i in range(0, len(hex_buffer)))

    print(hex_pairs)

    vertices = []
    #for x, y, z, red, green, blue in struct.iter_unpack('@3f3H', buffer):
    # in order to be corect we need to add x to our string which represents pading
    # for fields in struct.iter_unpack('@3f3H', buffer):
    for fields in struct.iter_unpack('@3f3Hxx', buffer):
        # vertex = make_colored_vertex(x, y, z, red, green, blue)
        vertex = make_colored_vertex(*fields)
        vertices.append(vertex)

    pp(vertices)

    # items = struct.unpack_from('@fffHHH', buffer)
    # print(repr(items))

if __name__ == '__main__':
    main()