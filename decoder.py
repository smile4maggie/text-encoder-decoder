class Decoder:

	def decode(self, encoding, output):
		"""
		For each non-null ASCII character an encoding string, write it the desired output file 
		based on how many times that character is consecutively repeated.
		Decoding:
			- If a character is a '♥' ('\u2665'), then iterate through the next 1-3 characters
			depending on if they are still digits to find the numTimes the previous character
			is repeated. Write that previous character into the output file numTimes.
			- Otherwise, if a character is not '×' ('\u00d7'), write the character to the output 
			file and set prev to that character.
		"""
		file = open(output, "w")
		index = 0
		prev = ""
		while index < len(encoding):
			char = encoding[index]
			if char == '\u2665':
				index += 1
				numTimes = ""
				digit = encoding[index]
				while digit.isdigit():
					numTimes += digit
					index += 1
					digit = encoding[index]
				for i in range(int(numTimes) - 1):
					file.write(prev)
			else:
				index += 1
				if char != '\u00d7':
					prev = char
					file.write(char)
		file.close()