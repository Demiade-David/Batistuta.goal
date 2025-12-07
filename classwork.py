from abc import ABC, abstractmethod

class CarModel(ABC):
    @abstractmethod
    def set_firstname(self):
        pass
    @abstractmethod
    def set_surname(self):
        pass
    @abstractmethod
    def set_age(self):
        pass
    @abstractmethod
    def set_class(self):
        pass
    @abstractmethod
    def get_info(self):
        pass


class Student1(CarModel):
    def __init__(self, firstname, surname, age, student_class):
        self.firstname = firstname
        self.surname = surname
        self.age = age
        self.student_class = student_class

    def set_firstname(self, firstname):
        self.firstname = firstname

    def set_surname(self, surname):
        self.surname = surname

    def set_age(self, age):
        self.age = age

    def set_class(self, student_class):
        self.student_class = student_class

    def get_info(self):
        return f"Student Name: {self.firstname} {self.surname}, Age: {self.age}, Class: {self.student_class}"
    
class Student2(Student1):
    def __init__(self, firstname, surname, age, student_class, grade):
        super().__init__(firstname, surname, age, student_class)
        self.grade = grade

    def set_grade(self, grade):
        self.grade = grade

    def get_info(self):
        base_info = super().get_info()
        return f"{base_info}, Grade: {self.grade}"
student1 = Student1("", "", "", "")
student1.set_firstname("Alice") 
student1.set_surname("Smith")
student1.set_age(17)
student1.set_class("10th Grade")
print(student1.get_info())
student = Student2("", "", 0, "", "")
student.set_firstname("John")
student.set_surname("Doe")
student.set_age(16)
student.set_class("11th Grade")
student.set_grade("A")
print(student.get_info())

# class Car(CarModel):
#     def __init__(self, name, make, year, ):
#         self.name = name
#         self.make = make
#         self.year = year

#     def get_max_speed(self):
#         if self.year < 2000:
#             return 120
#         elif self. year < 2010:
#             return 150
#         else:
#             return 180
  

#     def set_name(self, name):
#         self.name = name

#     def set_make(self, make):
#         self.make = make
#     def set_year(self, year):
#         self.year = year
#     def get_info(self):
#         return f"Car Name: {self.name}, Car Make: {self.make}, Year: {self.year}, Max Speed: {self.get_max_speed()} km/h "
# car= Car("", "", 2020,)

# car.set_name("Honda")
# car.set_make("Civic")
# print(car.get_info())

# class Truck(Car):
#     def __init__(self, name, make, year, capacity):
#         super().__init__(name, make, year)
#         self.capacity = capacity

#     def get_info(self):
#         base_info = super().get_info()
#         return f"{base_info}, Truck Capacity: {self.capacity} tons, Max Speed: {self.get_max_speed() - 20} km/h "

# Truck= Truck("Ford", "F-150", 2021, 30)
# print(Truck.get_info())




# class Account:
#     def __init__(self, num, balance):
#         self.num = num
#         self.balance = balance

#     def get_num(self):
#         print("Account number:", self.num)

#     def get_balance(self):
#         print("Account balance:", self.balance)

#     def set_num(self, new_num):
#         self.num = new_num
    
#     def set_balance(self, new_balance):
#         if new_balance < 0:
#             print("Balance cannot be negative.")
#         else:
#             self.balance += new_balance

# account1 = Account("123456789", 5000)

# account1.set_balance(1500)
# account1.get_balance()




