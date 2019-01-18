### Instructions

To manually encode/decode a particular .txt file:
	1. Make sure the `.txt` file is in the project directory, or add it
	2. Run the command `python3 manual_test.py` in the project directory
	3. The prompt will ask you for the name of the text file (without quotes) 
	   to encode (e.g. `data.txt`), and the name of the file to decode into 
	   (e.g. `output.txt`) which will then appear in the specfied location. 

### Testing

To run the unit tests, run the command `python3 test.py` in the root directory.
This will produce `filename-out.txt` files in the root directory that correspond
to the output of encoding/decoding `filename.txt`.

### Justification/Explanation

Since ASCII art tends to have many consecutively repeating characters in order to create 
uniform, aesthetically-pleasing images, I decided on an encoding method that would account
for this characteristic. By condensing repetition of characters into this encoding, we 
save a lot more space used for transport while preserving the file content information.

For example, we see in `data.txt` that the first line contains 41 space ` ` characters and 
then two commas `,`. My encoding compresses this line into a shorter string that can be 
interpreted as: `[character]♥[number of times repeated]×` for each character that has more than 
4 consecutive repetitions. This gives us an encoding: ` ♥41×,,`, which contains 7 characters as 
opposed to 43 characters. If a character (say `@`) repeats less than 5 consecutive times, we can 
simply add that character to the encoding that many number of times rather than including `@♥1×`, 
`@♥2×`, `@♥3×`, or `@♥4×` because this would take up greater than or equal to as much space as 
just writing it as `@`, `@@`, `@@@`, or `@@@@` respectively.

I chose '♥' as a separator because it's a cute non-ASCII character that should never appear 
in our 100x100 .txt files, and ended with a `×` character to signify the end of the integer 
that represents the number of times a character is repeated, which is always in the range 
[5, 100]. With these, I am able to compress the ASCII bitmaps into a shorter string on average
and linear in the worst case where there are no greater-than-four consecutive repetitions at all.