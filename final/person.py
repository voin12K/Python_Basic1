import datetime

class Person:
    def __init__(self, name, surname, patronymic, birth_date, death_date, gender):
        self.name = name
        self.surname = surname
        self.patronymic = patronymic
        self.birth_date = birth_date
        self.death_date = death_date
        self.gender = gender

    def calculate_age(self):
        end_date = self.death_date if self.death_date else datetime.datetime.now()
        age = end_date.year - self.birth_date.year
        if (end_date.month, end_date.day) < (self.birth_date.month, self.birth_date.day):
            age -= 1
        return age

    def __str__(self):
        age = self.calculate_age()
        gender = "чоловік" if self.gender == 'm' else "жінка"
        result = f"{self.name} {self.surname} {self.patronymic} {age} років, {gender}. Народився: {self.birth_date.strftime('%d.%m.%Y')}."
        if self.death_date:
            result += f" Помер: {self.death_date.strftime('%d.%m.%Y')}."
        return result
