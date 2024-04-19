def analyze_input(input_str):
    if input_str.lower() in ["вихід", "exit", "quit", "e", "q"]:
        return "exit"
    elif input_str.replace('.', '', 1).replace('-', '', 1).isdigit():
        try:
            number = float(input_str)
            if number < 0:
                if '.' in input_str:
                    return f"негативне дробове число: {number}"
                else:
                    return f"негативне ціле число: {number}"
            else:
                if '.' in input_str:
                    return f"позитивне дробове число: {number}"
                else:
                    return f" позитивне ціле число: {number}"
        except ValueError:
            return "не коректне число"
    else:
        return "Не коректне число"


while True:
    user_input = input("Введіть число або 'вихід', щоб завершити програму: ")
    result = analyze_input(user_input)
    if result == "exit":
        print("Завершення програми.")
        break
    else:
        print(result)
