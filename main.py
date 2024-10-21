# # print('hello world')
# # name = 'muneeb'

# # _private_variable = 42



# # text = "123"
# # is_decimal = text.isdecimal()
# # print(is_decimal)  # Output: True

# # name: int = 123
# # name = 'muneeb'
# # # print(type(name))
# # print(name)
# # name = "muneeb"
# # age = 23


# # name: list[str] = ["muneeb", "ahmed", "ali"]
# # print(name.index("muneeb"))
# # print(id(list))
# # popped_value = name.pop()
# # print(id(popped_value))
# # print(name, popped_value)

# # name:str = "ada lovelace"
# # print(name.title())
# C: int = 299792458  # The speed of light in m/s

# def main():
#     mass_in_kg: float = float(input("Enter kilos of mass: "))

#     # Calculate energy
#     # equivalently energy = mass * (C ** 2)
#     # using the ** operator to raise C to the power of 2
#     energy_in_joules: float = mass_in_kg * (C ** 2)

#     # Display work to the user
#     print("e = m * C^2...")
#     print("m = " + str(mass_in_kg) + " kg")
#     print("C = " + str(C) + " m/s")
    
#     print(str(energy_in_joules) + " joules of energy!")


# # There is no need to edit code beyond this point

# if __name__ == '__main__':
#     main()

# name = "   muneeb   "
# print(name.title())
# print(f"'{name.rstrip()}'")
# names = ["muneeb","john","ali"]
# print("unfortunately muneeb will not be arriving")
# names.insert(0,"baig")
# names.insert(2,"bakar")
# names.append("kishor")
# while len(names)>2:
#     names.pop()

# print(len(names))

# def num(*x):
#     total = 0
#     for num in x:
#         total += num
#     return total

# print(num(1, 2, 3))  # Output: 6
# print(num(4, 5, 6, 7))  # Output: 22


# def main(students):
#     for student in student:
#         print(f"my name is {students{'name'}} and my age is {students{'age'}}")

# students =[
#     {"name" : "muneeb", "age" : 23}
# ]

# main(students)

# def students(*subjects, **names):
#     print("Student details: ")
#     print(f"Subjects: {','.join(subjects)}")
#     for key, value in names.items():
#         print(f" {key} : {value}")
        


# students("english", "maths", "science",name="muneeb",age=23 , Roll_no=123)

# import csv

# def save_expense(expense, filename="expenses.csv"):
#     """Append a single expense to the CSV file."""
#     with open(filename, mode="a", newline='') as f:
#         writer = csv.writer(f)
#         writer.writerow([expense['date'], expense['category'], expense['amount'], expense.get('description', '')])

# def add_expense():
#     """Get user input and save it as an expense."""
#     date = input("Enter the date (YYYY-MM-DD): ")
#     category = input("Enter the category (e.g., food, transport): ")
#     amount = float(input("Enter the amount: "))
#     description = input("Enter a description (optional): ")

#     # Create an expense dictionary
#     expense = {
#         "date": date,
#         "category": category,
#         "amount": amount,
#         "description": description
#     }

#     # Save the expense to a CSV file
#     save_expense(expense)

# # Sample usage
# add_expense()

# class Student:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     def info(self):
#         print(f"my name is {self.name} and my age is {self.age}")

# # new_person = Student("Muneeb", 21)
# # new_person.info()
# # print(new_person.name, new_person.age)

# class Detail(Student):
#     def __init__(self, name, age, roll_number):
#         super().__init__(name, age)
#         self.roll_number = roll_number

#     def status(self):
#         print(f"your name is {self.name} and roll number is {self.roll_number}")
        
# # new = Admin("ali",23,123)
# # new.status()

# class Notification:
#     def send_notification(self, message):
#         print(f"Sending notification: {message}")

# class Admin(Detail, Notification):
#     def __init__(self, name, age , roll_number, username, email, access_level):
#         super().__init__(name, age, roll_number)
#         self.access_level = access_level
#         self.username = username
#         self.email = email

#     def send_admin_notification(self):
#         self.send_notification(f"Admin {self.username} has logged in.")

# new = Admin("muneeb",21,123, "muneeb123", "n9HJW@example.com", "admin")
# new.send_admin_notification()

# class User:
#     def __init__(self, username, email):
#         self.username = username
#         self.email = email

#     def display_user_info(self):
#         print(f"User: {self.username}, Email: {self.email}")
# class Customer(User):
#     def display_user_info(self):
#         print(f"Customer: {self.username}, Email: {self.email}")

# new = Customer("muneeb", "n9HJW@example.com")
# new.display_user_info()

# class TopLevel:
#     top_class_var = 100
#     def __init__(self):
#         self.top_var = 101

#     def top_method(self):
#         return 102


# class MidLevel(TopLevel):
#     mid_class_var = 200
#     def __init__(self):
#         super().__init__()
#         self.mid_var = 201
    
#     def mid_method(self):
#         return 202


# class LowerLevel(MidLevel):
#     lower_class_var = 300
#     def __init__(self):
#         super().__init__()
#         self.lower_var = 301

#     def lower_method(self):
#         return 302


# obj = LowerLevel()

# print(isinstance(obj, TopLevel))
# print(issubclass(TopLevel, LowerLevel))

# class Human:
#     def eat(self):
#         print("Human eats")

# class Animal:
#     def eat(self):
#         print("Animal eats")

# human_obj = Human()
# animal_obj = Animal()



# def eat_func (obj):
#     obj.eat()

# eat_func(human_obj)

# eat_func(animal_obj)

# def eat_all(obj):
#     for i in obj:
#         i.eat()
# new = eat_all([human_obj, animal_obj])

# class BankAccount:
#     def __init__(self, owner, balance):
#         # Public attribute
#         self.owner = owner
        
#         # Protected attribute
#         self._balance = balance
        
#         # Private attribute
#         self.__account_number = "1234567890"
    
#     # Public method to view the balance
#     def get_balance(self):
#         return self._balance
    
#     # Protected method (can be accessed within class or subclass)
#     def _deposit(self, amount):
#         if amount > 0:
#             self._balance += amount
#             print(f"Deposited {amount}. New balance is {self._balance}")
    
#     # Private method (not intended to be accessed directly)
#     def __generate_account_report(self):
#         return f"Account Report: Owner: {self.owner}, Balance: {self._balance}"
    
#     # Public method to get account report (calls the private method)
#     def get_account_report(self):
#         return self.__generate_account_report()


# # Instantiating a BankAccount object
# account = BankAccount("Alice", 1000)

# # Accessing public attribute
# print(f"Account Owner: {account.owner}")

# # Accessing protected attribute (though it's discouraged)
# print(f"Balance (Protected): {account._balance}")

# # Trying to access private attribute (This will fail)
# # print(account.__account_number)  # Uncommenting this will raise an AttributeError

# # Accessing private attribute through name mangling (not recommended)
# print(f"Account Number (Private): {account._BankAccount__account_number}")

# # Accessing public method
# print(f"Current Balance: {account.get_balance()}")

# # Accessing protected method (though it's discouraged)
# account._deposit(500)

# # Accessing private method via public method
# print(account.get_account_report())

# from abc import ABC, abstractmethod
# class User():
#     def __init__(self, username, email):
#         self._username = username
#         self._email = email

#     # @abstractmethod
#     # def display_user_info(self):
#     #     print(f"User: {self._username}, Email: {self._email}")

#     @staticmethod
#     def display_user_info():
#         print("hello")

# new = User("muneeb", "n9HJW@example.com")
# # new.display_user_info()
# print(new._username)
# print(new._email)
# # new.display_user_info()

# class Balance:
#     amount = 0
#     def __init__(self,balance,acc):
#         self.balance = balance
#         self.acc = acc
#     def debit(self,amount):
#         self.balance -= amount
#         print(f"Debited {amount}. New balance is {self.balance}")

#     def credit(self,amount):
#         self.balance += amount
#         print(f"Credited {amount}. New balance is {self.balance}")

#     def display(self):
#         print(f"Your account balance is {self.balance}")

# user1 = Balance(1000,"1234")
# user1.credit(500)
# user1.debit(200)
# user1.display()

# class Engine:
#     def __init__(self, horsepower):
#         self.horsepower = horsepower
    
#     def start(self):
#         print(f"Engine with {self.horsepower} horsepower starts.")

# class Car:
#     def __init__(self, model, horsepower):
#         # Composition: Car "has-an" Engine
#         self.model = model
#         self.engine = Engine(horsepower)
    
#     def drive(self):
#         self.engine.start()  # Using the Engine to start the car
#         print(f"{self.model} is now driving.")


# my_car = Car("Toyota Camry", 268)
# my_car.drive()

# def add_numbers():
#     try:
#         a = int(input("Enter first number: "))
#         b = int(input("Enter second number: "))  # If not a number, this will raise ValueError
#         print(a + b)
#     except ValueError:
#         print("Please enter valid numbers")
#     except TypeError:
#         print("There was a type error")

# add_numbers()

# def add_numbers():
#     try:
#         a = int(input("Enter first number: "))
#         b = input("Enter second number: ")
#         print(a + b)  # This will cause a TypeError
#     except Exception as e:
#         print(f"An error occurred: {e}")

# add_numbers()

# def divide(a, b):
#     if b == 0:
#         return "Cannot divide by zero!"
#     else:
#         return a / b
    
# print(divide(10, 0))

# class Person:
#     def __init__(self):
#         self.name = None
#         self.age = None

#     def take_input(self):
#         self.name = input("Enter your name: ")
        
#         # Error handling for age input
#         while True:
#             try:
#                 self.age = int(input("Enter your age: "))
#                 break  # Exit loop if the input is valid
#             except ValueError:
#                 print("Invalid input. Please enter a valid integer for age.")

#     def display(self):
#         print(f"Name: {self.name}")
#         print(f"Age: {self.age}")


# # Creating an object
# person2 = Person()
# person2.take_input()  # Call the method to take input with error handling
# person2.display()  # Display the data

# class Engine:
#     def __init__(self, horsepower):
#         self.horsepower = horsepower
    
#     def start(self):
#         print(f"Engine with {self.horsepower} horsepower starts.")
# class Wheel:
#     def __init__(self, size):
#         self.size = size

# class Car:
#     def __init__(self, model, horsepower, wheel_size):
#         self.model = model
#         self.engine = Engine(horsepower)  # Car has-an Engine
#         self.wheels = Wheel(wheel_size)  # Car has four Wheels
    
#     def drive(self):
#         self.engine.start()
#         print(f"{self.model} with {self.wheels.size}-inch wheels is now driving.")

# my_car = Car("Ford Mustang", 450, 19)
# my_car.drive()

class Customer:
    def __init__(self, name, email, account_number,balance):
        self.name = name
        self.email = email
        self.__account_number = account_number
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount
        print(f"Deposited {amount}. New balance is {self.__balance}")

    def withdraw(self, amount):
        if amount > self.__balance:
            print("Insufficient funds")
        else:
            self.__balance -= amount
            print(f"Withdrew {amount}. New balance is {self.__balance}")
    def get_balance(self):
        return f" your balance is {self.__balance}" 

    def get_account_number(self):
        return f" your account number is {self.__account_number}"

user1 = Customer("muneeb","n9HJW@example.com","123456789",1000)
print(user1.get_balance())
print(user1.get_account_number())
user1.withdraw(500)
print(user1.get_balance())
user1.deposit(500)
print(user1.get_balance())
  


  