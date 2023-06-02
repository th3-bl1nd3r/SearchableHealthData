def int_to_bytes(n):
    return n.to_bytes((n.bit_length() + 7) // 8, 'big')


def bytes_to_int(byte_array):
    return int.from_bytes(byte_array, byteorder='big')
