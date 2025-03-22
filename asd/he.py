# class BankAccount:
#     def __init__(self, account_holder, balance):
#         self.account_holder = account_holder
#         self.__balance = balance  # Private variable

#     def deposit(self, amount):
#         self.__balance += amount
#         print(f"{amount} deposit ho gaya. Naya balance: {self.__balance}")

#     def withdraw(self, amount):
#         if amount <= self.__balance:
#             self.__balance -= amount
#             print(f"{amount} withdraw ho gaya. Baqi balance: {self.__balance}")
#         else:
#             print("Balance kam hai!")

# # Object banayein
# account = BankAccount("Ali", 5000)
# account.deposit(2000) 
# account.withdraw(3000) 

# Ye line error de gi, kyunki __balance private hai
# print(account.__balance)


# class Animal:
#     def __init__(self, name):
#         self.name = name

#     def make_sound(self):
#         print("Yeh jaanwar awaz nikal raha hai")

# # Inheritance ka istemal
# class Dog(Animal):
#     def make_sound(self):
#         print(self.name, "bhonk raha hai!")

# # Object banayein
# dog1 = Dog("Tommy")
# dog1.make_sound()  



class Bird:
    def make_sound(self):
        print("Chirp Chirp")

class Cat:
    def make_sound(self):
        print("Meow Meow")

# Function jo dono objects ke liye kaam kare
def animal_sound(animal):
    animal.make_sound()

# Objects banayein
parrot = Bird()
kitty = Cat()

animal_sound(parrot)  
animal_sound(kitty) 
