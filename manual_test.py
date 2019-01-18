from encoder import Encoder
from decoder import Decoder

# Encoding
filename = input("Enter the filename to encode: ")
file = open(filename, "r")
encoder = Encoder()
print("Attempting to encode file " + filename + "...")
encoding = encoder.encode(file)
print("Successfully encoded! The encoded file:")
print(encoding)

# Decoding
decoder = Decoder()
output = input("Specify the path/filename to decode into: ")
decoding = decoder.decode(encoding, output)
print("Successfully decoded!")