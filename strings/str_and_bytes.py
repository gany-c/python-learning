"""
In general,

a byte is just 8 bits of information. You can put whatever you want in it.
If you want to fit characters in it, then ASCII is the solution - 26 English chars,
their Upper case and numbers

Unicode involves representing foreign characters as well. So a Unicode character
will have more than one byte. There are different forms of UTF encoding like UTF-8, 16, 32 etc

In Python3,

The 'bytes' data type is composed of raw bytes
The str data type is composed of unicode characters

But,

While creating an str variable you don't have to specify the encoding type.
You have to specify the encoding type while converting the str to bytes
"""

some_str = "The yiddish policeman's union"

for c in some_str:
    print(f"char = {c}")

byte_array = some_str.encode()

for b in byte_array:
    print(f"byte = {b}")

unicode_string = 'Hello, \u03A0\u03C1\u03BF\u03B3\u03C1\u03AC\u03BC\u03BC\u03B1!'  # Greek letters for "Pi" and "rho"

print(f"Unicode string = {unicode_string}")

for c in unicode_string:
    print(f"char = {c}")

# UTF-8 encoding for the Unicode characters
utf8_encoded_bytes = unicode_string.encode('utf-8')

# Print the UTF-8 encoded bytes
print(utf8_encoded_bytes)

for b in utf8_encoded_bytes:
    print(f"byte = {b}")


utf32_encoded_bytes = unicode_string.encode('utf-32')
# Print the UTF-32 encoded bytes
print(utf32_encoded_bytes)
print(utf8_encoded_bytes)
