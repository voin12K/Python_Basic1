n = int(input("Введіть ціле додатне число n: "))

sum_of_cubes = 0
i = 1

while i <= n:
    if i % 3 != 0:
        sum_of_cubes += i ** 3
    i += 1

print("Сума кубів всіх натуральних чисел від 1 до", n, " : ", sum_of_cubes)
