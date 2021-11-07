#lab4_zad2.
class Library:
    def __init__(self, city: str, street: str, zip_code: str, open_hours: str, phone: str):
        self.city= city
        self.street = street
        self.zip_code = zip_code
        self.open_hours = open_hours
        self.phone = phone
    def __str__(self):
        return f"Biblioteka znajduje się w {self.city} na ulicy {self.street}, kod pocztowy {self.zip_code}, godziny otwarcia {self.open_hours},numer {self.phone}"
class Order:
    def __init__(self, employee, student, books, order_date):
        self.employee=employee
        self.student= student
        self.books=books
        self.order_date=order_date
    def __str__(self):
        return f"Pracownik {self.employee}, student {self.student}, ksiązka {self.books},data {self.order_date}"
class Employee:
    def __init__(self, first_name, last_name, hire_date, birth_date, city, street, zip_code, phone):
        self.first_name = first_name
        self.last_name = last_name
        self.hire_date = hire_date
        self.birth_date = birth_date
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.phone = phone
    def __str__(self):
        return f"Imie {self.first_name}, nazwisko: {self.last_name}, data zatrudnienia:{self.hire_date}, data ur.: {self.birth_date}, miasto:{self.city}, ul.{self.street}, kod {self.zip_code}, numer {self.phone}"
class Book:
    def __init__(self, library, publication_date, author_name, author_surname, number_of_page):
        self.library =library
        self.publication_date = publication_date
        self.author_name = author_name
        self.author_surname = author_surname
        self.number_of_page = number_of_page
    def __str__(self):
        return f"Biblioteka {self.library}, data publikacji {self.publication_date}, imie autora{self.author_name}, nazwisko {self.author_surname}, liczba stron {self.number_of_page}"
class Student:
    def __init__(self, student: str, marks: int):
        self.student = student
        self.marks = marks
if __name__=='__main__':
    bibliotka_1 = Library("Katowice", "Zadole 3", "40-719","10-22", "312312312")
    biblioteka_2 = Library("Kraśnik", "Wyszyńskiego 13", "23-204","10-20", "781222131")

    ksiazka_1 = Book(bibliotka_1, "2004-04-16", "Stephen", "King", "204")
    ksiazka_2 = Book(bibliotka_1, "2008-09-09", "Marry", "Sheley", "230")
    ksiazka_3 = Book(biblioteka_2, "2005-08-11", "Joseph", "Murphy", "199")
    ksiazka_4 = Book(biblioteka_2, "2012-02-22", "Charles", "Duhigg", "334")
    ksiazka_5 = Book(biblioteka_2, "2018-08-16", "Stephen", "King", "224")

    pracownik_1 = Employee("Janusz", "Tracz", "2020-04-04", "1990-10-10", "Katowice", "Wyżynna", "40-719", "313124124")
    pracownik_2 = Employee("Mariusz", "Nowak", "2020-08-04", "1992-08-12", "Chorzów", "Długa", "40-739", "453534412")
    pracownik_3 = Employee("Kamil", "Jurek", "2019-08-09", "1993-03-11", "Katowice", "Krótka", "40-719", "222333444")

    student_1 = Student("Jan Nowak", "33")
    student_2 = Student("Kamil Kowalski", "55")
    student_3 = Student("Barry White", "40")

    order_1 = Order(pracownik_2, student_3, ksiazka_5, "2021-06-11")
    order_2 = Order(pracownik_1, student_1, ksiazka_1, "2021-07-22")

    print(order_1)
    print(order_2)