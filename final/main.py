import sys
import datetime
from data_manager import DataManager
from person import Person


def print_menu():
    print("1. Додати нову людину")
    print("2. Пошук людини")
    print("3. Завантажити дані з файлу")
    print("4. Зберегти дані у файл")
    print("5. Вийти")


def get_input_date(prompt):
    while True:
        date_str = input(prompt)
        try:
            date = datetime.datetime.strptime(date_str, '%d.%m.%Y')
            return date
        except ValueError:
            try:
                date = datetime.datetime.strptime(date_str, '%d %m %Y')
                return date
            except ValueError:
                try:
                    date = datetime.datetime.strptime(date_str, '%d/%m/%Y')
                    return date
                except ValueError:
                    try:
                        date = datetime.datetime.strptime(date_str, '%d-%m-%Y')
                        return date
                    except ValueError:
                        print("Неправильний формат дати. Спробуйте ще раз.")


def main():
    data_manager = DataManager()

    while True:
        print_menu()
        choice = input("Оберіть пункт меню: ")

        if choice == "1":
            name = input("Ім'я: ")
            surname = input("Прізвище: ")
            patronymic = input("По-батькові: ")
            birth_date = get_input_date("Дата народження (дд.мм.рррр або дд мм рррр або дд/мм/рррр або дд-мм-рррр): ")
            death_date = input(
                "Дата смерті (дд.мм.рррр або дд мм рррр або дд/мм/рррр або дд-мм-рррр, залишити порожнім якщо живий): ")
            if death_date:
                death_date = get_input_date(death_date)
            else:
                death_date = None
            gender = input("Стать (m/f): ")

            person = Person(name, surname, patronymic, birth_date, death_date, gender)
            data_manager.add_person(person)
            print("Людина додана.\n")

        elif choice == "2":
            search_term = input("Введіть строку для пошуку: ")
            results = data_manager.search_person(search_term)
            if results:
                for person in results:
                    print(person)
            else:
                print("Нічого не знайдено.\n")

        elif choice == "3":
            filename = input("Введіть назву файлу: ")
            data_manager.load_from_file(filename)
            print("Дані завантажені.\n")

        elif choice == "4":
            filename = input("Введіть назву файлу: ")
            data_manager.save_to_file(filename)
            print("Дані збережені.\n")

        elif choice == "5":
            print("До побачення!")
            sys.exit()

        else:
            print("Неправильний вибір, спробуйте ще раз.\n")


if __name__ == "__main__":
    main()
