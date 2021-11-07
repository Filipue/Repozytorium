#lab4_zad2.
class Library:
    def __init__(self, city, street, zip_code, open_hours, phone):
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
    library_1 = Library("Katowice", "Bogucicka 4", "40-000", "9:00-18:00", "700700700")
    library_2 = Library("Sosnowiec", "Prosta 7", "41-200", "8:300-19:00", "800800800")

    book_1 = Book(library_1, "2013-05-23", "Adam", "Słowacki", 1200)
    book_2 = Book(library_1, "2017-12-06", "Juliusz", "Mickiewicz", 1354)
    book_3 = Book(library_1, "2020-08-23", "Wojciech", "Dunia", 111)
    book_4 = Book(library_2, "2004-11-11", "Małgorzata", "Domagalik", 120)
    book_5 = Book(library_2, "2022-12-31", "Jan", "Nowak", 542)

    emp_1 = Employee("Adam", "Małysz", "2020-01-01", "1975-02-02", "Katowice", "Prosta 23", "40-000", "123456789")
    emp_2 = Employee("Mariusz", "Pudzianowski", "2019-01-01", "1970-02-02", "Kraków", "Krzywa 32", "50-00", "987654321")
    emp_3 = Employee("Thiago", "Cionek", "2018-01-01", "1977-02-02", "Warszawa", "Długa 123", "60-000", "567894321")

    student_1 = Student("Adam", 67)
    student_2 = Student("Kasia", 32)
    student_3 = Student("Jan", 99)

    order_1 = Order(emp_1, student_2, book_5, "2021-11-06")
    order_2 = Order(emp_3, student_3, book_3, "2020-12-27")

    print(order_1)
    print(order_2)