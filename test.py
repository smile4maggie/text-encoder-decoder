import unittest
import filecmp

from encoder import Encoder
from decoder import Decoder


class EncoderDecoderTest(unittest.TestCase):

	### HELPER METHODS ###

	def encode_file(self, filename):
		file = open(filename, "r")
		encoder = Encoder()
		encoded_file = encoder.encode(file)
		file.close()
		return encoded_file

	def check_equal_file_contents(self, filename):
		file = open(filename, "r")
		output = "out/" + filename.strip(".txt") + "-out.txt"
		encoder = Encoder()
		encoded = encoder.encode(file)
		file.close()
		decoder = Decoder()
		decoded = decoder.decode(encoded, output)
		self.assertTrue(filecmp.cmp(filename, output))

	### ENCODE TESTS ###

	def test_encode_simple_sentence(self):
		actual = self.encode_file("txt/simple_sentence.txt")
		expected = "@\u26655\u00d7a simple sentence@\u26655\u00d7"
		self.assertEqual(actual, expected)

	def test_encode_at_map(self):
		actual = self.encode_file("txt/at_map.txt")
		expected = "@\u2665100\u00d7"
		for line in actual.rsplit('\n'):
			self.assertEqual(line, expected)

	def test_encode_repeated_numbers(self):
		actual = self.encode_file("txt/repeated_numbers.txt")
		expected = '\n'.join(["1", "22", "333", "4444"]) + '\n'
		for i in range(5, 10):
			expected += str(i) + '\u2665' + str(i) + '\u00d7' + '\n'
		expected += "1010101010"
		actualLines = [line.rsplit('\n') for line in actual]
		expectedLines = [line.rsplit('\n') for line in expected]
		self.assertTrue(len(actualLines) == len(expectedLines))
		for i in range(len(actualLines)):
			self.assertEqual(actualLines[i], expectedLines[i])

	### DECODE TESTS ###

	def test_empty(self):
		self.check_equal_file_contents("txt/empty.txt")

	def test_simple_sentence(self):
		self.check_equal_file_contents("txt/simple_sentence.txt")

	def test_at_map(self):
		self.check_equal_file_contents("txt/at_map.txt")

	def test_repeated_numbers(self):
		self.check_equal_file_contents("txt/repeated_numbers.txt")

	def test_16ton(self):
		self.check_equal_file_contents("txt/16ton.txt")

	def test_teddybear(self):
		self.check_equal_file_contents("txt/teddybear.txt")

unittest.main(exit=False)
