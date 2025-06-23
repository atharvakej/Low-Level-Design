"""
LESSON 3: Instance and Class Attributes
=======================================

🎯 What you'll learn:
- Instance attributes vs Class attributes
- When to use each type
- How they behave differently
- Common pitfalls to avoid

💡 Key Concepts:
- Instance attributes: Belong to each individual object
- Class attributes: Shared by all instances of the class
- Attribute access and modification
"""

# 🎨 PART 1: Instance Attributes
# ===============================

class Dog:
    """Demonstrating instance attributes"""
    
    def __init__(self, name, breed):
        # These are INSTANCE attributes
        # Each dog object has its own copy
        self.name = name
        self.breed = breed
        self.tricks = []  # Empty list for each dog
    
    def teach_trick(self, trick):
        self.tricks.append(trick)
        print(f"{self.name} learned: {trick}")
    
    def show_tricks(self):
        print(f"{self.name}'s tricks: {', '.join(self.tricks)}")


# Each dog has its own attributes
print("--- Instance Attributes ---")
dog1 = Dog("Buddy", "Golden Retriever")
dog2 = Dog("Max", "Poodle")

# Teaching different tricks
dog1.teach_trick("sit")
dog1.teach_trick("fetch")
dog2.teach_trick("roll over")

# Each dog has its own tricks list
dog1.show_tricks()
dog2.show_tricks()


# 🏫 PART 2: Class Attributes
# ===========================

class Student:
    """Demonstrating class attributes"""
    
    # CLASS attributes - shared by all instances
    school_name = "Python High School"
    total_students = 0
    all_students = []
    
    def __init__(self, name, grade):
        # Instance attributes
        self.name = name
        self.grade = grade
        
        # Modifying class attributes
        Student.total_students += 1
        Student.all_students.append(name)
        
        print(f"{name} enrolled at {Student.school_name}")
    
    def introduce(self):
        print(f"Hi, I'm {self.name} in grade {self.grade}")
        print(f"I study at {Student.school_name}")


# Creating students
print("\n--- Class Attributes ---")
student1 = Student("Alice", 10)
student2 = Student("Bob", 11)
student3 = Student("Charlie", 10)

print(f"\nTotal students: {Student.total_students}")
print(f"All students: {Student.all_students}")
print(f"School name: {Student.school_name}")

# Changing class attribute affects all instances
print("\n--- Changing Class Attribute ---")
Student.school_name = "Advanced Python Academy"
student1.introduce()  # Uses new school name
student2.introduce()  # Also uses new school name


# 🚗 PART 3: Mixing Instance and Class Attributes
# ===============================================

class Car:
    """A more complex example"""
    
    # Class attributes
    total_cars_made = 0
    manufacturer = "Python Motors"
    available_colors = ["Red", "Blue", "Black", "White", "Silver"]
    
    def __init__(self, model, color, year):
        # Validate color
        if color not in Car.available_colors:
            print(f"Warning: {color} not in standard colors!")
        
        # Instance attributes
        self.model = model
        self.color = color
        self.year = year
        self.mileage = 0
        self.is_running = False
        
        # Update class attribute
        Car.total_cars_made += 1
        self.car_id = Car.total_cars_made  # Unique ID for each car
        
        print(f"Car #{self.car_id} created: {year} {color} {model}")
    
    def drive(self, distance):
        if self.is_running:
            self.mileage += distance
            print(f"Drove {distance} km. Total mileage: {self.mileage} km")
        else:
            print("Start the car first!")
    
    def start(self):
        self.is_running = True
        print(f"{self.model} started!")
    
    @classmethod
    def show_factory_info(cls):
        """Class method to show factory information"""
        print(f"\n--- {cls.manufacturer} Factory Info ---")
        print(f"Total cars produced: {cls.total_cars_made}")
        print(f"Available colors: {', '.join(cls.available_colors)}")


# Using the Car class
print("\n--- Car Example ---")
car1 = Car("Sedan", "Blue", 2023)
car2 = Car("SUV", "Red", 2024)
car3 = Car("Coupe", "Green", 2024)  # Non-standard color

# Each car has its own mileage
car1.start()
car1.drive(100)
car2.start()
car2.drive(50)

# Class method shows shared information
Car.show_factory_info()


# ⚠️ PART 4: Common Pitfalls
# ==========================

class BankAccount:
    """Demonstrating a common mistake with mutable class attributes"""
    
    # DANGER: Mutable class attribute (list)
    # This is usually a mistake!
    # transaction_history = []  # DON'T DO THIS!
    
    # Class attributes (immutable are safer)
    bank_name = "Python Bank"
    total_accounts = 0
    
    def __init__(self, owner, initial_balance=0):
        self.owner = owner
        self.balance = initial_balance
        # Each account should have its own transaction history
        self.transaction_history = []  # Instance attribute - CORRECT!
        
        BankAccount.total_accounts += 1
        self.account_number = f"ACC{BankAccount.total_accounts:04d}"
    
    def deposit(self, amount):
        self.balance += amount
        self.transaction_history.append(f"Deposited ${amount}")
        print(f"${amount} deposited to {self.account_number}")
    
    def show_history(self):
        print(f"\n--- {self.owner}'s Transaction History ---")
        for transaction in self.transaction_history:
            print(f"  - {transaction}")


# Each account has separate history
print("\n--- Bank Account Example ---")
acc1 = BankAccount("Alice", 1000)
acc2 = BankAccount("Bob", 500)

acc1.deposit(200)
acc2.deposit(100)

acc1.show_history()  # Only Alice's transactions
acc2.show_history()  # Only Bob's transactions

print(f"\nTotal accounts at {BankAccount.bank_name}: {BankAccount.total_accounts}")


# 📊 PART 5: Best Practices Example
# =================================

class Employee:
    """Demonstrating best practices"""
    
    # Class attributes - configuration and shared data
    company_name = "Tech Corp"
    next_employee_id = 1000
    departments = ["Engineering", "Sales", "HR", "Marketing"]
    
    def __init__(self, name, department, salary):
        # Validate department
        if department not in Employee.departments:
            raise ValueError(f"Department must be one of: {Employee.departments}")
        
        # Instance attributes - unique to each employee
        self.name = name
        self.department = department
        self.salary = salary
        self.employee_id = Employee.next_employee_id
        self.skills = []  # Each employee has their own skills list
        
        # Update class attribute
        Employee.next_employee_id += 1
    
    def add_skill(self, skill):
        """Add a skill to this employee"""
        if skill not in self.skills:
            self.skills.append(skill)
            print(f"{self.name} learned: {skill}")
    
    def get_info(self):
        """Display employee information"""
        print(f"\n--- Employee #{self.employee_id} ---")
        print(f"Name: {self.name}")
        print(f"Department: {self.department}")
        print(f"Company: {Employee.company_name}")
        print(f"Skills: {', '.join(self.skills) if self.skills else 'None yet'}")
    
    @classmethod
    def add_department(cls, dept_name):
        """Class method to add new department"""
        if dept_name not in cls.departments:
            cls.departments.append(dept_name)
            print(f"New department added: {dept_name}")


# Using Employee class
print("\n--- Employee Example ---")
emp1 = Employee("Alice", "Engineering", 75000)
emp2 = Employee("Bob", "Sales", 65000)

emp1.add_skill("Python")
emp1.add_skill("JavaScript")
emp2.add_skill("Communication")
emp2.add_skill("Negotiation")

emp1.get_info()
emp2.get_info()

# Adding new department using class method
Employee.add_department("Research")
print(f"\nAvailable departments: {Employee.departments}")


# 🎮 PRACTICE EXERCISES
# =====================

print("\n" + "="*50)
print("YOUR TURN - EXERCISES")
print("="*50)

# Exercise 1: Create a Book class
# TODO: Create a Book class with:
# - Class attribute: total_books (count of all books)
# - Class attribute: genres (list of available genres)
# - Instance attributes: title, author, genre, pages
# - Method to display book info
# - Class method to show library statistics

# Your code here:


# Exercise 2: Create a Player class for a game
# TODO: Create a Player class with:
# - Class attribute: max_level = 100
# - Class attribute: total_players = 0
# - Instance attributes: name, level (starts at 1), experience (starts at 0)
# - Method: gain_experience(points) - adds experience and levels up every 100 points
# - Method: display_stats()

# Your code here:


# Exercise 3: Create a Product class
# TODO: Create a Product class with:
# - Class attribute: store_name = "Python Store"
# - Class attribute: tax_rate = 0.08 (8%)
# - Instance attributes: name, base_price, category
# - Method: get_price_with_tax() - returns price including tax
# - Class method: update_tax_rate(new_rate)

# Your code here:


# 🎯 CHALLENGE EXERCISE
# ====================
# Create a SocialMediaPost class with:
# - Class attributes: platform_name, total_posts, trending_hashtags (list)
# - Instance attributes: author, content, likes (starts at 0), comments (list)
# - Methods: add_like(), add_comment(text), is_trending() (checks if post has trending hashtag)
# - Class method: add_trending_hashtag(tag)
# Make it interactive!

# Your code here:


# 💡 ATTRIBUTE TIPS:
# - Use instance attributes for data unique to each object
# - Use class attributes for shared data or configuration
# - Be careful with mutable class attributes (lists, dicts)
# - Access class attributes using ClassName.attribute
# - Instance attributes are created with self.attribute

print("\n✅ Great job! You now understand attributes! Next: 04_methods.py") 