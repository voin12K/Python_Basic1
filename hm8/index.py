import random


def generate_random_number():
    return random.randint(1, 10)


def guess_number(num_attempts):
    secret_number = generate_random_number()
    print("Вгадайте число від 1 до 10.")

    for attempt in range(num_attempts):
        guess = int(input("Спроба {}: ".format(attempt + 1)))
        if guess == secret_number:
            print("Вітаємо! Ви вгадали число!")
            return True
        elif guess < secret_number:
            print("Загадане число більше.")
        else:
            print("Загадане число менше.")

    print("Ви не вгадали. Загадане число було {}.".format(secret_number))
    return False


def play_game():
    num_attempts = 3
    while True:
        if guess_number(num_attempts):
            play_again = input("Хочете зіграти ще раз? (так/ні): ")
            if play_again.lower() != 'так':
                print("Дякуємо за гру!")
                break
        else:
            play_again = input("Хочете спробувати ще раз? (так/ні): ")
            if play_again.lower() != 'так':
                print("Дякуємо за гру!")
                break


play_game()
