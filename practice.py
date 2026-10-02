# class Student:
#     def __init__(self, name, age, roll_no):
#         self.name = name
#         self.age = age
#         self.roll_no = roll_no

#     def show_details(self):
#         print(f"Name: {self.name}, Age: {self.age}, Roll No: {self.roll_no}")

# # Object banaya
# s1 = Student("Prince", 20, 101)
# s1.show_details()



# class bank:
#     def __init__(self, name, balance, branch):
#         self.name = name
#         self.balance = balance
#         self.branch = branch

#     def show(self):
#         print(f"name: {self.name}, balance: {self.balance}, branch: {self.branch}")

# bank1 = bank("Ram", 100000, "India")
# bank1.show()



# class Bank:
#     def __init__(self, name, balance, branch):
#         self.name = name
#         self.balance = balance
#         self.branch = branch

#     def show(self):
#         print(f"Name: {self.name}, Balance: {self.balance}, Branch: {self.branch}")

#     def deposit(self, amount):
#         self.balance = self.balance + amount
#         print(f"Deposited {amount}. New balance is {self.balance}")

#     def withdraw(self, amount):
#         # yaha balance se amount minus karo, lekin check karo balance kaafi hai ya nahi
#         if self.balance >= amount:
#             self.balance = self.balance - amount
#             print(f"Withdrew {amount}. New balance is {self.balance}")
#         else:
#             print("Insufficient balance.")


# bank1 = Bank("Ram", 100000, "MG Road")
# bank1.deposit(5000)
# bank1.withdraw(2000)
# bank1.show()



# accounts = []
# accounts.append(Bank("Ram", 100000, "MG Road"))
# accounts.append(Bank("Sita", 50000, "Connaught Place"))
# # ab loop se sabka show() call karo

# class Bank:
#     def __init__(self, name, balance, branch):
#         self.name = name
#         self.balance = balance
#         self.branch = branch

#     def show(self):
#         print(f"name: {self.name}, balance: {self.balance}, branch: {self.branch}")

# accounts = []
# accounts.append(Bank("Ram", 100000, "MG Road"))
# accounts.append(Bank("Sita", 50000, "Connaught Place"))
# for account in accounts:
#     account.show()