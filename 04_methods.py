"""
LESSON 4: Instance, Class, and Static Methods
=============================================

🎯 What you'll learn:
- Instance methods (most common)
- Class methods (@classmethod)
- Static methods (@staticmethod)
- When to use each type

💡 Key Concepts:
- Instance methods: Work with instance data (self)
- Class methods: Work with class data (cls)
- Static methods: Don't need instance or class data
- Method decorators: @classmethod, @staticmethod
"""

# 🎨 PART 1: Instance Methods (Review)
# ====================================

class Dog:
    """Instance methods are the most common type"""
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.energy = 100
    
    # Instance method - uses 'self' to access instance data
    def bark(self):
        print(f"{self.name} says: Woof!")
        self.energy -= 5
    
    def play(self, minutes):
        print(f"{self.name} is playing for {minutes} minutes")
        self.energy -= minutes * 2
        if self.energy < 0:
            self.energy = 0
        print(f"Energy level: {self.energy}%")
    
    def sleep(self):
        print(f"{self.name} is sleeping... Zzz")
        self.energy = min(100, self.energy + 30)
        print(f"Energy restored to: {self.energy}%")


# Using instance methods
print("--- Instance Methods ---")
buddy = Dog("Buddy", 3)
buddy.bark()
buddy.play(10)
buddy.sleep()


# 🏭 PART 2: Class Methods
# ========================

class Pizza:
    """Demonstrating class methods"""
    
    # Class attributes
    restaurant_name = "Python Pizza"
    available_sizes = ["small", "medium", "large"]
    pizza_count = 0
    
    def __init__(self, size, toppings):
        if size not in Pizza.available_sizes:
            raise ValueError(f"Size must be one of: {Pizza.available_sizes}")
        
        self.size = size
        self.toppings = toppings
        self.price = self._calculate_price()
        Pizza.pizza_count += 1
        self.order_number = Pizza.pizza_count
    
    def _calculate_price(self):
        """Private instance method"""
        base_prices = {"small": 10, "medium": 15, "large": 20}
        topping_price = len(self.toppings) * 2
        return base_prices[self.size] + topping_price
    
    # Instance method
    def describe(self):
        print(f"Order #{self.order_number}: {self.size} pizza")
        print(f"Toppings: {', '.join(self.toppings)}")
        print(f"Price: ${self.price}")
    
    # Class method - uses 'cls' instead of 'self'
    @classmethod
    def from_string(cls, pizza_string):
        """Alternative constructor - creates Pizza from string"""
        # Format: "size:topping1,topping2,topping3"
        parts = pizza_string.split(":")
        size = parts[0]
        toppings = parts[1].split(",") if len(parts) > 1 else []
        return cls(size, toppings)  # Creates new instance
    
    @classmethod
    def create_margherita(cls, size="medium"):
        """Factory method - creates a specific type of pizza"""
        return cls(size, ["tomato", "mozzarella", "basil"])
    
    @classmethod
    def show_menu(cls):
        """Display restaurant information"""
        print(f"\n--- Welcome to {cls.restaurant_name} ---")
        print(f"Available sizes: {', '.join(cls.available_sizes)}")
        print(f"Pizzas made today: {cls.pizza_count}")


# Using class methods
print("\n--- Class Methods ---")
Pizza.show_menu()

# Regular constructor
pizza1 = Pizza("large", ["pepperoni", "mushrooms"])
pizza1.describe()

# Using alternative constructor (class method)
pizza2 = Pizza.from_string("medium:ham,pineapple,cheese")
pizza2.describe()

# Using factory method
pizza3 = Pizza.create_margherita("small")
pizza3.describe()

Pizza.show_menu()


# 🔧 PART 3: Static Methods
# =========================

class MathHelper:
    """Demonstrating static methods"""
    
    # Static methods don't use self or cls
    @staticmethod
    def add(x, y):
        """Simple addition"""
        return x + y
    
    @staticmethod
    def multiply(x, y):
        """Simple multiplication"""
        return x * y
    
    @staticmethod
    def is_even(number):
        """Check if number is even"""
        return number % 2 == 0
    
    @staticmethod
    def calculate_circle_area(radius):
        """Calculate area of circle"""
        import math
        return math.pi * radius ** 2


# Using static methods - no need to create instance
print("\n--- Static Methods ---")
print(f"5 + 3 = {MathHelper.add(5, 3)}")
print(f"4 × 7 = {MathHelper.multiply(4, 7)}")
print(f"Is 42 even? {MathHelper.is_even(42)}")
print(f"Circle area (r=5): {MathHelper.calculate_circle_area(5):.2f}")

# Can also call from instance (but not recommended)
math_obj = MathHelper()
print(f"Via instance: 2 + 2 = {math_obj.add(2, 2)}")


# 🏦 PART 4: Real-World Example - Bank System
# ===========================================

class BankAccount:
    """Complete example using all three method types"""
    
    # Class attributes
    bank_name = "Python National Bank"
    interest_rate = 0.02  # 2% annual
    total_accounts = 0
    minimum_balance = 100
    
    def __init__(self, owner, initial_deposit):
        if initial_deposit < BankAccount.minimum_balance:
            raise ValueError(f"Minimum deposit is ${BankAccount.minimum_balance}")
        
        self.owner = owner
        self.balance = initial_deposit
        BankAccount.total_accounts += 1
        self.account_number = f"ACC{BankAccount.total_accounts:06d}"
        self.transactions = []
        self._log_transaction(f"Account opened with ${initial_deposit}")
    
    # Instance methods
    def deposit(self, amount):
        """Instance method - modifies instance state"""
        if amount > 0:
            self.balance += amount
            self._log_transaction(f"Deposited ${amount}")
            return True
        return False
    
    def withdraw(self, amount):
        """Instance method - uses instance data"""
        if 0 < amount <= self.balance - BankAccount.minimum_balance:
            self.balance -= amount
            self._log_transaction(f"Withdrew ${amount}")
            return True
        print("Insufficient funds or invalid amount")
        return False
    
    def get_balance(self):
        """Instance method - accesses instance data"""
        return self.balance
    
    def _log_transaction(self, description):
        """Private instance method"""
        from datetime import datetime
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.transactions.append(f"{timestamp}: {description}")
    
    # Class methods
    @classmethod
    def from_employee_account(cls, employee_name):
        """Factory method for employee accounts with bonus"""
        initial_bonus = 500
        return cls(f"Employee: {employee_name}", initial_bonus)
    
    @classmethod
    def update_interest_rate(cls, new_rate):
        """Update interest rate for all accounts"""
        old_rate = cls.interest_rate
        cls.interest_rate = new_rate
        print(f"Interest rate updated from {old_rate*100}% to {new_rate*100}%")
    
    @classmethod
    def get_bank_statistics(cls):
        """Show bank-wide statistics"""
        print(f"\n--- {cls.bank_name} Statistics ---")
        print(f"Total accounts: {cls.total_accounts}")
        print(f"Current interest rate: {cls.interest_rate*100}%")
        print(f"Minimum balance required: ${cls.minimum_balance}")
    
    # Static methods
    @staticmethod
    def calculate_interest(principal, rate, years):
        """Calculate simple interest - doesn't need instance/class data"""
        return principal * rate * years
    
    @staticmethod
    def validate_amount(amount):
        """Validate monetary amount"""
        try:
            amount = float(amount)
            return amount > 0 and round(amount, 2) == amount
        except:
            return False
    
    @staticmethod
    def format_currency(amount):
        """Format amount as currency"""
        return f"${amount:,.2f}"


# Using all method types
print("\n--- Bank System Example ---")

# Regular account creation
account1 = BankAccount("Alice Johnson", 1000)
print(f"Account created: {account1.account_number}")

# Using class method (factory)
employee_account = BankAccount.from_employee_account("Bob Smith")
print(f"Employee account created: {employee_account.account_number}")

# Instance methods
account1.deposit(500)
account1.withdraw(200)
print(f"Alice's balance: {BankAccount.format_currency(account1.get_balance())}")

# Class method
BankAccount.update_interest_rate(0.025)
BankAccount.get_bank_statistics()

# Static methods
interest = BankAccount.calculate_interest(1000, 0.025, 3)
print(f"\nInterest on $1000 for 3 years: {BankAccount.format_currency(interest)}")

# Validation using static method
amounts = [100, -50, 45.678, "abc", 99.99]
for amt in amounts:
    valid = BankAccount.validate_amount(amt)
    print(f"Is {amt} a valid amount? {valid}")


# 🎯 PART 5: When to Use Each Type
# =================================

class EmailService:
    """Example showing when to use each method type"""
    
    # Class attributes
    smtp_server = "smtp.python.com"
    port = 587
    total_emails_sent = 0
    
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.sent_emails = []
        self.connected = False
    
    # Instance method - when you need instance data
    def send_email(self, to, subject, body):
        """Needs instance data (username, password)"""
        if not self.connected:
            print("Please connect first!")
            return
        
        print(f"Sending email from {self.username} to {to}")
        print(f"Subject: {subject}")
        self.sent_emails.append({"to": to, "subject": subject})
        EmailService.total_emails_sent += 1
    
    def connect(self):
        """Instance method - modifies instance state"""
        print(f"Connecting to {EmailService.smtp_server}...")
        self.connected = True
        print("Connected!")
    
    # Class method - when you need class data or alternative constructors
    @classmethod
    def from_gmail(cls, username, password):
        """Factory method for Gmail accounts"""
        # Could set Gmail-specific settings here
        instance = cls(username, password)
        instance.provider = "Gmail"
        return instance
    
    @classmethod
    def change_server(cls, new_server, new_port):
        """Updates configuration for all instances"""
        cls.smtp_server = new_server
        cls.port = new_port
        print(f"Email server changed to {new_server}:{new_port}")
    
    # Static method - when you don't need instance or class data
    @staticmethod
    def validate_email_address(email):
        """Doesn't need any instance or class data"""
        import re
        pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        return re.match(pattern, email) is not None
    
    @staticmethod
    def create_html_template(title, content):
        """Utility function - doesn't need class/instance data"""
        return f"<html><head><title>{title}</title></head><body>{content}</body></html>"


# Demonstrating usage
print("\n--- Email Service Example ---")

# Static method - can use without creating instance
print(f"Is 'user@example.com' valid? {EmailService.validate_email_address('user@example.com')}")
print(f"Is 'invalid.email' valid? {EmailService.validate_email_address('invalid.email')}")

# Create instance and use instance methods
email_service = EmailService("user@python.com", "password123")
email_service.connect()
email_service.send_email("friend@example.com", "Hello", "How are you?")

# Class method
EmailService.change_server("smtp.newserver.com", 465)


# 🎮 PRACTICE EXERCISES
# =====================

print("\n" + "="*50)
print("YOUR TURN - EXERCISES")
print("="*50)

# Exercise 1: Create a Temperature class
# TODO: Create a Temperature class with:
# - Instance method: __init__(self, celsius)
# - Instance method: to_fahrenheit() - converts to Fahrenheit
# - Class method: from_fahrenheit(cls, fahrenheit) - creates instance from Fahrenheit
# - Static method: celsius_to_kelvin(celsius) - converts any Celsius to Kelvin
# - Static method: is_freezing(celsius) - returns True if below 0°C

# Your code here:


# Exercise 2: Create a StringUtils class
# TODO: Create a StringUtils class with only static methods:
# - reverse_string(text) - reverses a string
# - count_vowels(text) - counts vowels in text
# - is_palindrome(text) - checks if text is palindrome
# - remove_spaces(text) - removes all spaces

# Your code here:


# Exercise 3: Create a User class
# TODO: Create a User class with:
# - Class attribute: total_users = 0
# - Instance attributes: username, email, is_active (True by default)
# - Instance method: deactivate() - sets is_active to False
# - Class method: from_email_only(cls, email) - creates user with email as username
# - Class method: get_active_users_count(cls) - returns count of active users
# - Static method: generate_username(first_name, last_name) - creates username

# Your code here:


# 🎯 CHALLENGE EXERCISE
# ====================
# Create a DateTime class with:
# - Instance attributes: day, month, year
# - Instance method: is_leap_year() - checks if the year is leap year
# - Instance method: add_days(days) - adds days to the date
# - Class method: today(cls) - creates instance with today's date
# - Class method: from_string(cls, date_string) - creates from "DD-MM-YYYY"
# - Static method: days_in_month(month, year) - returns days in given month
# - Static method: is_valid_date(day, month, year) - validates date

# Your code here:


# 💡 METHOD TIPS:
# - Use instance methods when you need to access/modify instance data (self)
# - Use class methods for alternative constructors or class-level operations (cls)
# - Use static methods for utility functions that don't need instance/class data
# - Instance methods are the most common - use them by default
# - Consider static methods for validation or conversion utilities

print("\n✅ Excellent! You understand method types! Next: 05_encapsulation.py") 