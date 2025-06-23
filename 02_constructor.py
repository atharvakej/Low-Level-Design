"""
LESSON 2: Constructor and __init__ Method
=========================================

🎯 What you'll learn:
- What is a constructor?
- The __init__ method
- Instance attributes
- Creating objects with initial values

💡 Key Concepts:
- Constructor: Special method called when creating an object
- __init__: Python's constructor method
- Instance attributes: Variables that belong to each object
- self: Reference to the current instance
"""

# 🏗️ PART 1: Understanding __init__
# ==================================

import datetime


class Dog:
    """A Dog class with a constructor"""
    
    def __init__(self, name, age):
        # These are instance attributes
        # They belong to each individual dog object
        self.name = name
        self.age = age
        print(f"A new dog named {self.name} is born!")
    
    def bark(self):
        print(f"{self.name} says: Woof! Woof!")
    
    def describe(self):
        print(f"{self.name} is {self.age} years old.")


# Creating Dog objects with initial values
print("--- Creating Dogs ---")
buddy = Dog("Buddy", 3)
max_dog = Dog("Max", 5)

print("\n--- Using our Dogs ---")
buddy.bark()
buddy.describe()

max_dog.bark()
max_dog.describe()


# 🚗 PART 2: More Complex Constructor
# ===================================

class Car:
    """Car class with multiple attributes"""
    
    def __init__(self, brand, model, year, color="Silver"):
        # Setting instance attributes
        self.brand = brand
        self.model = model
        self.year = year
        self.color = color  # Default parameter
        self.is_running = False  # Default value
        self.speed = 0
        
        print(f"New {color} {year} {brand} {model} created!")
    
    def start(self):
        if not self.is_running:
            self.is_running = True
            print(f"The {self.brand} {self.model} is now running.")
        else:
            print("The car is already running!")
    
    def accelerate(self, increase):
        if self.is_running:
            self.speed += increase
            print(f"Speed increased to {self.speed} km/h")
        else:
            print("Start the car first!")
    
    def info(self):
        print(f"\n--- Car Information ---")
        print(f"Brand: {self.brand}")
        print(f"Model: {self.model}")
        print(f"Year: {self.year}")
        print(f"Color: {self.color}")
        print(f"Running: {self.is_running}")
        print(f"Speed: {self.speed} km/h")


# Using the Car class
print("\n--- Car Example ---")
my_car = Car("Toyota", "Camry", 2023)
sports_car = Car("Ferrari", "F8", 2024, "Red")

my_car.info()
my_car.start()
my_car.accelerate(50)
my_car.accelerate(30)
my_car.info()


# 📚 PART 3: Student Class Example
# ================================

class Student:
    """Example showing data validation in constructor"""
    
    def __init__(self, name, age, grade):
        # Data validation in constructor
        if age < 5 or age > 100:
            print("Warning: Unusual age for a student!")
        
        if grade < 1 or grade > 12:
            print("Warning: Grade should be between 1 and 12!")
        
        self.name = name
        self.age = age
        self.grade = grade
        self.subjects = []  # Empty list for subjects
        self.grades = {}    # Empty dictionary for grades
    
    def enroll_subject(self, subject):
        self.subjects.append(subject)
        print(f"{self.name} enrolled in {subject}")
    
    def add_grade(self, subject, grade):
        self.grades[subject] = grade
        print(f"Grade recorded: {subject} = {grade}")
    
    def show_report_card(self):
        print(f"\n--- Report Card for {self.name} ---")
        print(f"Age: {self.age}, Grade: {self.grade}")
        print("Subjects:", ", ".join(self.subjects))
        if self.grades:
            print("Grades:")
            for subject, grade in self.grades.items():
                print(f"  {subject}: {grade}")
            average = sum(self.grades.values()) / len(self.grades)
            print(f"Average: {average:.2f}")


# Using Student class
print("\n--- Student Example ---")
alice = Student("Alice", 15, 10)
alice.enroll_subject("Math")
alice.enroll_subject("Science")
alice.enroll_subject("English")

alice.add_grade("Math", 95)
alice.add_grade("Science", 88)
alice.add_grade("English", 92)

alice.show_report_card()


# 🏦 PART 4: Bank Account with Constructor
# ========================================

class BankAccount:
    """Bank account with initial balance"""
    
    def __init__(self, account_holder, initial_balance=0):
        self.account_holder = account_holder
        self.balance = initial_balance
        self.transaction_history = []
        
        # Record account creation
        self.transaction_history.append(f"Account opened with ${initial_balance}")
        print(f"Account created for {account_holder}")
        print(f"Initial balance: ${initial_balance}")
    
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.transaction_history.append(f"Deposited ${amount}")
            print(f"Deposited ${amount}. New balance: ${self.balance}")
        else:
            print("Deposit amount must be positive!")
    
    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds!")
        elif amount <= 0:
            print("Withdrawal amount must be positive!")
        else:
            self.balance -= amount
            self.transaction_history.append(f"Withdrew ${amount}")
            print(f"Withdrew ${amount}. New balance: ${self.balance}")
    
    def show_history(self):
        print(f"\n--- Transaction History for {self.account_holder} ---")
        for transaction in self.transaction_history:
            print(f"- {transaction}")
        print(f"Current balance: ${self.balance}")


# Using BankAccount
print("\n--- Bank Account Example ---")
john_account = BankAccount("John Doe", 1000)
john_account.deposit(500)
john_account.withdraw(200)
john_account.show_history()


# 🎮 PRACTICE EXERCISES
# =====================

print("\n" + "="*50)
print("YOUR TURN - EXERCISES")
print("="*50)

# Exercise 1: Create a Rectangle class
# TODO: Create a Rectangle class with:
# - __init__ method that takes width and height
# - calculate_area() method
# - calculate_perimeter() method
# - is_square() method that returns True if it's a square

# Your code here:

class Rectangle:

    def __init__(self, width, height):
        self.height = height
        self.width = width

    def calculate_area(self):
        return self.height * self.width

    def calculate_perimeter(self):
        return (self.height + self.width) * 2

    def is_square(self):
        return self.height == self.width

# Test the Rectangle class
print("\n--- Testing Rectangle Class ---")
rect1 = Rectangle(10, 5)
print(f"Rectangle dimensions: {rect1.width} x {rect1.height}")
print(f"Area: {rect1.calculate_area()}")
print(f"Perimeter: {rect1.calculate_perimeter()}")
print(f"Is it a square? {rect1.is_square()}")

square = Rectangle(7, 7)
print(f"\nSquare dimensions: {square.width} x {square.height}")
print(f"Is it a square? {square.is_square()}")


# Exercise 2: Create a Movie class
# TODO: Create a Movie class with:
# - __init__ that takes title, director, year, and rating (optional, default=0)
# - rate_movie(rating) method to update rating
# - get_age() method that returns how old the movie is
# - display_info() method to show all movie details

# Your code here:

class Movie:

    def __init__(self, title, director, year, rating=0):
        self.title = title
        self.director = director
        self.year = year
        self.rating = rating
    
    def rate_movie(self, rating):
        if 0 <= rating <= 10:
            self.rating = rating
            print(f"Rating updated to {rating}/10")
        else:
            print("Rating must be between 0 and 10")
    
    def get_age(self):
        current_year = datetime.datetime.now().year
        return current_year - self.year
    
    def display_info(self):
        print(f"\n--- Movie Information ---")
        print(f"Title: {self.title}")
        print(f"Director: {self.director}")
        print(f"Year: {self.year}")
        print(f"Age: {self.get_age()} years old")
        print(f"Rating: {self.rating}/10")

# Test the Movie class
print("\n--- Testing Movie Class ---")
movie1 = Movie("The Matrix", "Wachowski Sisters", 1999)
movie1.display_info()
movie1.rate_movie(9)
movie1.display_info()

movie2 = Movie("Inception", "Christopher Nolan", 2010, 8.5)
movie2.display_info()


# Exercise 3: Create a ShoppingCart class
# TODO: Create a ShoppingCart class with:
# - __init__ that takes owner_name
# - add_item(item_name, price) method
# - remove_item(item_name) method
# - get_total() method that returns total price
# - display_cart() method that shows all items and total

# Your code here:

class ShoppingCart:
    
    def __init__(self, owner_name):
        self.owner_name = owner_name
        self.items = {}  # Dictionary to store items and prices
        print(f"Shopping cart created for {owner_name}")
    
    def add_item(self, item_name, price):
        if price >= 0:
            self.items[item_name] = price
            print(f"Added {item_name} - ${price:.2f}")
        else:
            print("Price cannot be negative!")
    
    def remove_item(self, item_name):
        if item_name in self.items:
            removed_price = self.items.pop(item_name)
            print(f"Removed {item_name} - ${removed_price:.2f}")
        else:
            print(f"{item_name} not found in cart!")
    
    def get_total(self):
        return sum(self.items.values())
    
    def display_cart(self):
        print(f"\n--- {self.owner_name}'s Shopping Cart ---")
        if self.items:
            for item, price in self.items.items():
                print(f"  {item}: ${price:.2f}")
            print(f"Total: ${self.get_total():.2f}")
        else:
            print("Cart is empty!")

# Test the ShoppingCart class
print("\n--- Testing ShoppingCart Class ---")
cart = ShoppingCart("Alice")
cart.add_item("Apple", 2.99)
cart.add_item("Bread", 3.50)
cart.add_item("Milk", 4.25)
cart.display_cart()
cart.remove_item("Bread")
cart.display_cart()


# 🎯 CHALLENGE EXERCISE
# ====================
# Create a VideoGame class with:
# - Constructor that takes name, genre, and price
# - Attributes for: is_installed (False by default), hours_played (0 by default)
# - Methods for: install(), uninstall(), play(hours), show_stats()
# Make it interactive and add data validation!

# Your code here:


# 💡 CONSTRUCTOR TIPS:
# - __init__ is called automatically when you create an object
# - Always use self as the first parameter
# - You can have default parameters in __init__
# - Use the constructor to set initial state of your objects
# - Validate data in the constructor when needed

print("\n✅ Excellent! You now understand constructors! Next: 03_attributes.py") 