input_string = input("Введіть довільну строку: ")

even_chars = input_string[::2]

reverse_upper = input_string[::-1].upper()

print("Введена строка:", input_string)
print("Строка з парних символів:", even_chars)
print("Строка, написана у зворотній послідовності та у верхньому регістрі:", reverse_upper)
