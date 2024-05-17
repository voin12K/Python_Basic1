import datetime
import csv
from person import Person

class DataManager:
    def __init__(self):
        self.people = []

    def add_person(self, person):
        self.people.append(person)

    def search_person(self, search_term):
        results = []
        search_term = search_term.lower()
        for person in self.people:
            if (search_term in person.name.lower() or
                search_term in person.surname.lower() or
                search_term in person.patronymic.lower()):
                results.append(person)
        return results

    def load_from_file(self, filename):
        self.people = []
        with open(filename, 'r', newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            for row in reader:
                if len(row) == 6:
                    name, surname, patronymic, birth_date, death_date, gender = row
                    birth_date = datetime.datetime.strptime(birth_date, '%d.%m.%Y')
                    death_date = datetime.datetime.strptime(death_date, '%d.%m.%Y') if death_date else None
                    person = Person(name, surname, patronymic, birth_date, death_date, gender)
                    self.people.append(person)

    def save_to_file(self, filename):
        with open(filename, 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            for person in self.people:
                birth_date = person.birth_date.strftime('%d.%m.%Y')
                death_date = person.death_date.strftime('%d.%m.%Y') if person.death_date else ''
                writer.writerow([person.name, person.surname, person.patronymic, birth_date, death_date, person.gender])
