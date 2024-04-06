n = int(input("Введіть ціле додатне число n: "))

sum_of_cubes = 0

for i in range(1, n + 1):
    if i % 3 != 0:
        sum_of_cubes += i ** 3

print("Сума кубів всіх натуральних чисел від 1 до", n, " : ", sum_of_cubes)
