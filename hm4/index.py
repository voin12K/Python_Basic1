name = input("привіт , як тебе звати? ")
age_str = input("добре, а скільки тобі років? ")

if age_str.isdigit():
    age = int(age_str)

    if age < 1:
        print("Помилка, введіть коректний вік")
    elif age < 11:
        print(f"Привіт, шкет {name}")
    elif age < 19:
        print(f"Як справи, {name}?")
    elif age < 100:
        print(f"Що бажаєте, {name}?")
    else:
        print(f"{name}, ви брешете - у наш час стільки не живуть...")
else:
    print("Помилка, введіть ціле число")
