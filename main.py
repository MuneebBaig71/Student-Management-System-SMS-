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