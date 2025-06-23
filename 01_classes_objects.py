"""
LESSON 1: Classes and Objects
=============================

🎯 What you'll learn:
- What are classes and objects?
- How to create a class
- How to create objects from a class
- Basic class syntax

💡 Key Concepts:
- Class: A blueprint or template for creating objects
- Object: An instance of a class
- self: Reference to the current instance
"""

# 🏗️ PART 1: Creating Your First Class
# =====================================

# A class is like a blueprint for creating objects

class Dog:
    """This is a simple Dog class"""
    
    # This is a method (function inside a class)
    def bark(self):
        print("Woof! Woof!")
    
    def wag_tail(self):
        print("The dog is wagging its tail happily!")


# 🎨 PART 2: Creating Objects (Instances)
# =======================================

# Creating objects from our Dog class
my_dog = Dog()      # This creates a new Dog object
neighbor_dog = Dog() # Another Dog object

print("--- Using our Dog objects ---")
my_dog.bark()        # Calling the bark method
my_dog.wag_tail()    # Calling the wag_tail method

neighbor_dog.bark()  # Same class, different object


# 🚗 PART 3: A More Complex Example
# =================================

class Car:
    """A class to represent a car"""
    
    # Methods can take parameters
    def start_engine(self):
        print("🚗 Vroom! The engine is starting...")
        
    def drive(self, destination):
        print(f"🚗 Driving to {destination}")
        
    def stop(self):
        print("🚗 The car has stopped.")
        
    def honk(self, times=1):
        for i in range(times):
            print("🚗 Beep!")


# Creating and using Car objects
print("\n--- Car Example ---")
my_car = Car()
my_car.start_engine()
my_car.drive("the grocery store")
my_car.honk(2)
my_car.stop()


# 📱 PART 4: Real-world Example - Smartphone
# ==========================================

class Smartphone:
    """A more practical example"""
    
    def turn_on(self):
        print("📱 Phone is turning on...")
        print("📱 Welcome!")
        
    def make_call(self, contact):
        print(f"📱 Calling {contact}...")
        print("📱 Ring... Ring...")
        
    def send_message(self, contact, message):
        print(f"📱 Sending message to {contact}: '{message}'")
        print("📱 Message sent! ✓")
        
    def take_photo(self):
        print("📱 Say cheese! 📸")
        print("📱 Photo saved to gallery")


# Using the Smartphone class
print("\n--- Smartphone Example ---")
my_phone = Smartphone()
my_phone.turn_on()
my_phone.make_call("Mom")
my_phone.send_message("Friend", "Hey, want to grab coffee?")
my_phone.take_photo()


# 🎮 PRACTICE EXERCISES
# =====================

print("\n" + "="*50)
print("🎯 YOUR TURN - EXERCISES")
print("="*50)

# Exercise 1: Create a Book class
# TODO: Create a class called 'Book' with the following methods:
# - open_book(): prints "Opening the book..."
# - read_page(page_number): prints "Reading page {page_number}"
# - close_book(): prints "Closing the book."

# Your code here:
class Book:
    def open_book(self):
        print("Opening the book...")
    
    def read_page(self, page_number):
        print(f"Reading page {page_number}")
    
    def close_book(self):
        print("Closing the book.")

# Test your Book class
print("\n--- Testing Book Class ---")
my_book = Book()
my_book.open_book()
my_book.read_page(42)
my_book.read_page(43)
my_book.close_book()


# Exercise 2: Create a BankAccount class
# TODO: Create a class with these methods:
# - check_balance(): prints "Checking balance..."
# - deposit(amount): prints "Depositing ${amount}"
# - withdraw(amount): prints "Withdrawing ${amount}"

# Your code here:
class BankAccount:
    def check_balance(self):
        print("Checking balance...")
    def deposit(self,amount):
        print(f"Depositing ${amount}")
    def withdraw(self,amount):
        print(f"Withdrawing ${amount}")


# Exercise 3: Create a MusicPlayer class
# TODO: Create a class with methods:
# - play_song(song_name): prints "♪ Playing: {song_name}"
# - pause(): prints "⏸ Music paused"
# - next_song(): prints "⏭ Skipping to next song"
# - set_volume(level): prints "🔊 Volume set to {level}%"

# Your code here:

class MusicPlayer:
    def play_song(self,song_name):
        print(f"♪ Playing: {song_name}")
    
    def pause(self):
        print("⏸ Music paused")
    
    def next_song(self):
        print("⏭ Skipping to next song")
    
    def set_volume(self,level):
        print(f"🔊 Volume set to {level}%")


# 🎯 CHALLENGE EXERCISE
# ====================
# Create a Restaurant class with methods for:
# - opening the restaurant
# - taking orders (with customer name and dish)
# - serving food
# - closing the restaurant
# Make it interactive and fun!

# Your code here:

class Restaurant:
    def open_restaurant(self):
        print("🍽️ Restaurant is opening...")
    
    def take_order(self,customer_name,dish):
        print(f"🍽️ {customer_name} is ordering {dish}")
    
    def serve_food(self):
        print("🍽️ Food is being served...")
    
    def close_restaurant(self):
        print("🍽️ Restaurant is closing...")


# 💡 TIPS:
# - Class names should use CamelCase (e.g., MyClass, BankAccount)
# - Method names should use snake_case (e.g., my_method, calculate_total)
# - Always include 'self' as the first parameter in methods
# - Think of classes as nouns and methods as verbs

print("\n✅ Great job! When you're ready, move on to 02_constructor.py") 