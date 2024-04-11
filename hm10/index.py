f = int(input("Введите целое число: "))

result = lambda x: 'парне' if x % 2 == 0 else 'не парне'

print(result(f))
