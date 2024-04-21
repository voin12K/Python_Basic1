encoded_utf8 = b'r\xc3\xa9sum\xc3\xa9'

decoded_str = encoded_utf8.decode('utf-8')
print("Декодований рядок (utf-8):", decoded_str)

encoded_latin1 = decoded_str.encode('latin1', errors='ignore')
print("Рядок у байтовому вигляді (Latin1):", encoded_latin1)

decoded_str_again = encoded_latin1.decode('latin1')
print("Декодований рядок знову (Latin1):", decoded_str_again)
