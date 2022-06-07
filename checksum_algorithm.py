# this table holds pre-generated bit-shifted/XOR-ed CRC values,
# so algorithm can cycle through bytes using this table
crc_table = []


def create_crc_lookup_table():
    a = []
    for i in range(256):  # cycle through all possible byte-values
        k = i  # assign current byte-value to a variable
        for j in range(8):  # work through all the bits
            if k & 1:  # if first bit is 1...
                k ^= 0x1db710640  # do XOR division with generator polynomial
            # bit-shift first bit in order to either get of the first
            # one generated by division on line 12, or simply discard
            # first bit since it was previously zero
            k = k >> 1
        a.append(k)  # append the result value to the
    return a


def mycrc32(data):
    global crc_table
    if not crc_table:
        crc_table = create_crc_lookup_table()
    crc = 0xffffffff  # initial state of crc
    for byte in data:  # cycle through all the bytes of given data
        # access the pre-generated value from the crc table
        # using current crc state and current byte value and XOR
        # afterwards
        crc = crc_table[(crc & 0xff) ^ byte] ^ (crc >> 8)
    return crc ^ 0xffffffff