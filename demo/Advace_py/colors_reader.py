import struct

def main():
    with open('colors.bin', 'rb') as f:
        buffer = f.read()

    items = struct.unpack_from('@fffHHH', buffer)

    print(repr(items))

if __name__ == '__main__':
    main()