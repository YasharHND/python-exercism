def encode_one(number):
    binary = bin(number)[2:]
    separated = []
    for i in range(len(binary) // 7):
        seven_bits = binary[(i * -7) - 7:i * -7 or None]
        separated.insert(0, seven_bits)
    remaining = len(binary) % 7
    if remaining > 0:
        separated.insert(0, "".join(["0" for _ in range(7 - remaining)]) + binary[:remaining])
    out = [int("0b1" + byte_, 2) for byte_ in separated[:-1]] + [int("0b0" + separated[-1], 2)]
    return out


def encode(numbers):
    out = []
    for number in numbers:
        out += encode_one(number)
    return out


def decode_one(bytes_):
    if len(bytes_) == 1:
        return bytes_[0]
    binary_str = "0b"
    for byte in bytes_:
        byte_str = bin(byte)
        if len(byte_str) == 10:
            binary_str += byte_str[3:]
        else:
            byte_str = byte_str[2:]
            binary_str += "".join(["0" for _ in range(7 - len(byte_str))]) + byte_str
    return int(binary_str, 2)


def decode(bytes_):
    if bytes_[-1] != 0x0 and bytes_[-1] != 0x7F:
        raise ValueError("incomplete sequence")
    out = []
    parts = []
    sequence = []
    for byte in bytes_:
        sequence.append(byte)
        if byte == 0x0 or byte == 0x7F or byte == 0x56:
            parts.append(sequence)
            sequence = []
    for part in parts:
        out.append(decode_one(part))
    return out
