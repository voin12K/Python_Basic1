x = input("введіть ціле число: ")

if x.isdigit():
    x = int(x)
    if x % 2 == 0:
        res = "парне"
    else:
        res = "не парне"
else:
    res = "не валідне"

print("Ваше число " + str(x) + " " + res)
