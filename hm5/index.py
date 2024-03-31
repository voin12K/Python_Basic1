number = input("Введіть число: ")

is_integer = number.isdigit()

result = "парне" if is_integer and int(number) % 2 == 0 else "непарне" if is_integer else "не валідне"
print(f"Ваше число {number} {result}.")
