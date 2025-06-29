"""
LESSON 6: Inheritance - Code Reusability
========================================

🎯 What you'll learn:
- What is inheritance and why use it
- Single inheritance
- Method overriding
- super() function
- Multiple inheritance
- Method Resolution Order (MRO)

💡 Key Concepts:
- Parent/Base/Super class: The class being inherited from
- Child/Derived/Sub class: The class that inherits
- IS-A relationship: Child IS-A type of Parent
- Code reuse through inheritance
"""

# 🦴 PART 1: Basic Inheritance
# =============================

class Animal:
    """Base class for all animals"""
    
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.is_alive = True
    
    def eat(self):
        print(f"{self.name} is eating.")
    
    def sleep(self):
        print(f"{self.name} is sleeping.")
    
    def make_sound(self):
        print(f"{self.name} makes a sound.")


class Dog(Animal):  # Dog inherits from Animal
    """Dog class inherits from Animal"""
    
    def __init__(self, name, breed):
        # Call parent class constructor
        super().__init__(name, "Canine")
        self.breed = breed
    
    # Override parent method
    def make_sound(self):
        print(f"{self.name} says: Woof! Woof!")
    
    # Add new method specific to Dog
    def fetch(self):
        print(f"{self.name} is fetching the ball!")


class Cat(Animal):  # Cat inherits from Animal
    """Cat class inherits from Animal"""
    
    def __init__(self, name, color):
        super().__init__(name, "Feline")
        self.color = color
    
    # Override parent method
    def make_sound(self):
        print(f"{self.name} says: Meow!")
    
    # Cat-specific method
    def scratch(self):
        print(f"{self.name} is scratching!")


# Using inheritance
print("--- Basic Inheritance ---")
dog = Dog("Buddy", "Golden Retriever")
cat = Cat("Whiskers", "Orange")

# Methods from parent class
dog.eat()      # Inherited from Animal
cat.sleep()    # Inherited from Animal

# Overridden methods
dog.make_sound()  # Dog's version
cat.make_sound()  # Cat's version

# Class-specific methods
dog.fetch()
cat.scratch()


# 🚗 PART 2: Inheritance with super()
# ====================================

class Vehicle:
    """Base class for vehicles"""
    
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.is_running = False
        self.mileage = 0
    
    def start(self):
        self.is_running = True
        print(f"The {self.year} {self.make} {self.model} is starting.")
    
    def stop(self):
        self.is_running = False
        print("Vehicle stopped.")
    
    def drive(self, distance):
        if self.is_running:
            self.mileage += distance
            print(f"Drove {distance} miles. Total mileage: {self.mileage}")
        else:
            print("Start the vehicle first!")


class Car(Vehicle):
    """Car inherits from Vehicle"""
    
    def __init__(self, make, model, year, num_doors):
        # Call parent constructor
        super().__init__(make, model, year)
        self.num_doors = num_doors
        self.trunk_open = False
    
    def open_trunk(self):
        self.trunk_open = True
        print("Trunk opened.")
    
    def close_trunk(self):
        self.trunk_open = False
        print("Trunk closed.")


class Motorcycle(Vehicle):
    """Motorcycle inherits from Vehicle"""
    
    def __init__(self, make, model, year, type):
        super().__init__(make, model, year)
        self.type = type  # sport, cruiser, touring
    
    # Override parent method with extension
    def start(self):
        print("Putting on helmet...")
        super().start()  # Call parent's start method
        print("Ready to ride!")
    
    def do_wheelie(self):
        if self.is_running:
            print("Doing a wheelie! 🏍️")
        else:
            print("Start the motorcycle first!")


# Using vehicle inheritance
print("\n--- Vehicle Inheritance ---")
car = Car("Toyota", "Camry", 2023, 4)
motorcycle = Motorcycle("Harley", "Sportster", 2022, "cruiser")

# Inherited methods
car.start()
car.drive(50)
car.open_trunk()

# Overridden method
motorcycle.start()  # Custom start with parent call
motorcycle.drive(30)
motorcycle.do_wheelie()


# 🏢 PART 3: Multi-level Inheritance
# ==================================

class Employee:
    """Base employee class"""
    
    def __init__(self, name, employee_id):
        self.name = name
        self.employee_id = employee_id
        self.base_salary = 50000
    
    def work(self):
        print(f"{self.name} is working.")
    
    def get_salary(self):
        return self.base_salary


class Developer(Employee):
    """Developer inherits from Employee"""
    
    def __init__(self, name, employee_id, programming_languages):
        super().__init__(name, employee_id)
        self.programming_languages = programming_languages
        self.base_salary = 70000  # Developers have higher base
    
    def code(self):
        print(f"{self.name} is coding in {', '.join(self.programming_languages)}")
    
    # Override work method
    def work(self):
        print(f"{self.name} is writing code.")


class SeniorDeveloper(Developer):
    """SeniorDeveloper inherits from Developer (multi-level)"""
    
    def __init__(self, name, employee_id, programming_languages, team_size):
        super().__init__(name, employee_id, programming_languages)
        self.team_size = team_size
        self.base_salary = 100000  # Senior devs earn more
    
    def mentor(self):
        print(f"{self.name} is mentoring {self.team_size} developers.")
    
    # Override work method again
    def work(self):
        super().work()  # Call Developer's work
        print(f"{self.name} is also reviewing code and mentoring.")
    
    # Override salary with bonus
    def get_salary(self):
        base = super().get_salary()
        bonus = self.team_size * 1000  # $1000 per team member
        return base + bonus


# Multi-level inheritance
print("\n--- Multi-level Inheritance ---")
employee = Employee("John", "EMP001")
developer = Developer("Alice", "DEV001", ["Python", "JavaScript"])
senior_dev = SeniorDeveloper("Bob", "SR001", ["Python", "Java", "Go"], 5)

# Different levels of methods
employee.work()
developer.work()
developer.code()

senior_dev.work()  # Calls multiple levels
senior_dev.mentor()
print(f"{senior_dev.name}'s salary: ${senior_dev.get_salary():,}")


# 💎 PART 4: Multiple Inheritance
# ===============================

class Flyer:
    """Mixin class for flying ability"""
    
    def __init__(self):
        self.altitude = 0
    
    def fly(self, height):
        self.altitude = height
        print(f"Flying at {height} feet!")
    
    def land(self):
        self.altitude = 0
        print("Landed safely.")


class Swimmer:
    """Mixin class for swimming ability"""
    
    def __init__(self):
        self.depth = 0
    
    def swim(self, depth):
        self.depth = depth
        print(f"Swimming at {depth} feet deep!")
    
    def surface(self):
        self.depth = 0
        print("Back at the surface.")


class Duck(Animal, Flyer, Swimmer):
    """Duck has multiple inheritance"""
    
    def __init__(self, name):
        # Initialize all parent classes
        Animal.__init__(self, name, "Bird")
        Flyer.__init__(self)
        Swimmer.__init__(self)
    
    def make_sound(self):
        print(f"{self.name} says: Quack! Quack!")


# Multiple inheritance
print("\n--- Multiple Inheritance ---")
duck = Duck("Donald")

# Methods from Animal
duck.eat()
duck.make_sound()

# Methods from Flyer
duck.fly(100)
duck.land()

# Methods from Swimmer
duck.swim(10)
duck.surface()


# 🎭 PART 5: Method Resolution Order (MRO)
# ========================================

class A:
    def method(self):
        print("Method from class A")

class B(A):
    def method(self):
        print("Method from class B")

class C(A):
    def method(self):
        print("Method from class C")

class D(B, C):
    pass  # D doesn't override method


# MRO determines which method is called
print("\n--- Method Resolution Order ---")
d = D()
d.method()  # Which method is called?

# Check MRO
print(f"MRO for class D: {[cls.__name__ for cls in D.__mro__]}")


# 🏦 PART 6: Real-world Example - Banking System
# ==============================================

class Account:
    """Base account class"""
    
    def __init__(self, account_number, owner, balance=0):
        self.account_number = account_number
        self.owner = owner
        self._balance = balance
        self.transactions = []
    
    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            self._log_transaction("Deposit", amount)
            return True
        return False
    
    def withdraw(self, amount):
        if 0 < amount <= self._balance:
            self._balance -= amount
            self._log_transaction("Withdrawal", amount)
            return True
        return False
    
    def get_balance(self):
        return self._balance
    
    def _log_transaction(self, type, amount):
        from datetime import datetime
        self.transactions.append({
            'date': datetime.now(),
            'type': type,
            'amount': amount,
            'balance': self._balance
        })


class SavingsAccount(Account):
    """Savings account with interest"""
    
    def __init__(self, account_number, owner, balance=0):
        super().__init__(account_number, owner, balance)
        self.interest_rate = 0.02  # 2% annual
        self.withdrawal_limit = 6  # per month
        self.withdrawals_this_month = 0
    
    def withdraw(self, amount):
        if self.withdrawals_this_month >= self.withdrawal_limit:
            print("Monthly withdrawal limit reached!")
            return False
        
        if super().withdraw(amount):
            self.withdrawals_this_month += 1
            return True
        return False
    
    def add_interest(self):
        interest = self._balance * self.interest_rate
        self.deposit(interest)
        print(f"Interest added: ${interest:.2f}")


class CheckingAccount(Account):
    """Checking account with overdraft protection"""
    
    def __init__(self, account_number, owner, balance=0):
        super().__init__(account_number, owner, balance)
        self.overdraft_limit = 500
    
    def withdraw(self, amount):
        available = self._balance + self.overdraft_limit
        if 0 < amount <= available:
            self._balance -= amount
            self._log_transaction("Withdrawal", amount)
            if self._balance < 0:
                print(f"Using overdraft. Balance: ${self._balance}")
            return True
        else:
            print("Exceeds overdraft limit!")
            return False
    
    def write_check(self, payee, amount):
        print(f"Writing check to {payee} for ${amount}")
        return self.withdraw(amount)


class PremiumAccount(SavingsAccount, CheckingAccount):
    """Premium account with features from both"""
    
    def __init__(self, account_number, owner, balance=0):
        # Initialize the base Account class
        Account.__init__(self, account_number, owner, balance)
        # Set attributes from both parent classes
        self.interest_rate = 0.03  # Higher interest
        self.withdrawal_limit = 10  # Higher limit
        self.withdrawals_this_month = 0
        self.overdraft_limit = 1000  # Higher overdraft
        self.is_premium = True
    
    def get_perks(self):
        print("Premium Perks:")
        print(f"- Interest Rate: {self.interest_rate*100}%")
        print(f"- Withdrawal Limit: {self.withdrawal_limit}/month")
        print(f"- Overdraft Limit: ${self.overdraft_limit}")
        print("- Free checks")
        print("- No ATM fees")


# Using the banking system
print("\n--- Banking System Example ---")

# Savings Account
savings = SavingsAccount("SAV001", "Alice", 1000)
savings.deposit(500)
savings.withdraw(200)
savings.add_interest()
print(f"Savings balance: ${savings.get_balance():.2f}")

# Checking Account
checking = CheckingAccount("CHK001", "Bob", 500)
checking.write_check("Landlord", 600)  # Uses overdraft
print(f"Checking balance: ${checking.get_balance():.2f}")

# Premium Account
premium = PremiumAccount("PRM001", "Charlie", 5000)
premium.get_perks()
premium.add_interest()
premium.write_check("Car Dealer", 2000)
print(f"Premium balance: ${premium.get_balance():.2f}")


# 🎮 PRACTICE EXERCISES
# =====================

print("\n" + "="*50)
print("YOUR TURN - EXERCISES")
print("="*50)

# Exercise 1: Create a Shape hierarchy
# TODO: Create these classes:
# - Shape (base): attributes: name, color; methods: area(), perimeter()
# - Rectangle(Shape): attributes: width, height; override area() and perimeter()
# - Circle(Shape): attributes: radius; override area() and perimeter()
# - Square(Rectangle): only needs side length; adjust constructor

# Your code here:


# Exercise 2: Create a Person hierarchy
# TODO: Create these classes:
# - Person: attributes: name, age; method: introduce()
# - Student(Person): add: student_id, grades[]; methods: add_grade(), get_gpa()
# - Teacher(Person): add: subject, classes[]; method: teach()
# - TeachingAssistant(Student, Teacher): combines both roles

# Your code here:


# Exercise 3: Create a Device hierarchy
# TODO: Create these classes:
# - Device: attributes: brand, model, is_on; methods: turn_on(), turn_off()
# - Phone(Device): add: phone_number; methods: call(), send_sms()
# - Computer(Device): add: ram, storage; methods: run_program()
# - Smartphone(Phone, Computer): combines features; add: apps[]

# Your code here:


# 🎯 CHALLENGE EXERCISE
# ====================
# Create a game character system:
# - Character: health, name, level; methods: attack(), defend(), level_up()
# - Warrior(Character): strength stat, heavy armor; special: rage()
# - Mage(Character): mana, spells[]; special: cast_spell()
# - Rogue(Character): stealth, agility; special: sneak_attack()
# - Paladin(Warrior, Mage): holy powers; combine warrior and magic
# Add proper constructors and method overrides!

# Your code here:


# 💡 INHERITANCE TIPS:
# - Use inheritance for "IS-A" relationships
# - Prefer composition over inheritance when unsure
# - Always call super().__init__() in child constructors
# - Override methods to specialize behavior
# - Use multiple inheritance carefully (prefer mixins)
# - Check MRO when debugging multiple inheritance

print("\n✅ Excellent! You understand inheritance! Next: 07_polymorphism.py") 