def count_numbers(numbers_list):
    counter = {}
    for number in numbers_list:
        if number in counter:
            counter[number] += 1
        else:
            counter[number] = 1
    return counter

numbers_list = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3]
result = count_numbers(numbers_list)
print(result)
