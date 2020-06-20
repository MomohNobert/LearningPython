from struct import *

# Store as bytes data.
packed_data = pack('iif', 6, 12, 4.56)
print(packed_data)

print(calcsize('i'))
print(calcsize('f'))
print(calcsize('iif'))

unpacked_data = unpack('iif', packed_data)
print(unpacked_data)