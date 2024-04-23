row1 = input("Введіть перший рядок: ")
row2 = input("Введіть другий рядок: ")
row3 = input("Введіть третій рядок: ")
row4 = input("Введіть четвертий рядок: ")

with open("file.txt", "w") as file:
    file.write(row1 + "\n")
    file.write(row2 + "\n")

with open("file.txt", "a") as file:
    file.write(row3 + "\n")
    file.write(row4 + "\n")

print("Записано в файл 'file.txt'")
