import sys


filename = sys.argv[1]
bad_chars = sys.argv[2]

bad_chars_arr = bad_chars.split("\\x")
bad_chars_arr = bad_chars_arr[1:]

bad_chars_set = set()

for bad_char in bad_chars_arr:
    bad_chars_set.add(int(bad_char, 16))

def has_bad_char(addr):
    for i in range(0,4):
        byte = (addr >> (i * 8)) & 0xFF
        if byte in bad_chars_set:
            return True

    return False


with open(filename) as file:
    for line in file:
        line = line.strip()

        if not line[:2] == "0x":
            continue

        parts = line.split(":")
        addr = parts[0]
        addr = int(addr, 16)

        if has_bad_char(addr):
            continue

        print(line)


