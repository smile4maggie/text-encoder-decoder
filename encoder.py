class Encoder:

	def encode(self, file):
		"""
		For each line in a given file, encode it and add it to the resulting string. 
		"""
		encoding = ""
		for line in file:
			encoding += self.encode_line(line)
		return encoding

	def encode_line(self, line):
		"""
		For each character in a given line (string):
			- If a character is consecutively repeated more than four times, follow it 
			with a '♥' ('\u2665'), the number of times it is repeated, and the Unicode 
			'×' (multiplication sign) character '\u00d7'. Then add that concatenated 
			string to the encoding.
			- If not, simply add the character to the encoding.
		"""
		result = ""
		curr = ""
		count = 0
		for char in line: 
			if char != curr:
				result += self.encode_char(curr, count)
				curr = char
				count = 1
			else:
				count += 1
		result += self.encode_char(curr, count)
		return result

	def encode_char(self, char, count):
		"""
		Given a character and the number of times it is repeated consecutively,
		return its most space-efficient encoding.
		"""
		if count > 4:
			return char + '\u2665' + str(count) + '\u00d7'
		else:
			return char * count
