"""
LESSON 5: Encapsulation - Public, Protected, and Private
========================================================

🎯 What you'll learn:
- What is encapsulation and why it matters
- Public attributes and methods
- Protected members (convention with _)
- Private members (name mangling with __)
- Property decorators for controlled access

💡 Key Concepts:
- Encapsulation: Bundling data and methods, hiding internal details
- Access modifiers in Python (convention-based)
- Getters and setters using @property
- Name mangling for private attributes
"""

# 🔓 PART 1: Public Members (Default)
# ===================================

class Car:
    """Everything is public by default in Python"""
    
    def __init__(self, brand, model):
        # Public attributes - accessible from anywhere
        self.brand = brand
        self.model = model
        self.speed = 0
    
    # Public method
    def accelerate(self, amount):
        self.speed += amount
        print(f"Speed is now {self.speed} km/h")
    
    # Public method
    def get_info(self):
        return f"{self.brand} {self.model}"


# Using public members
print("--- Public Members ---")
car = Car("Toyota", "Camry")
print(car.brand)  # Direct access to public attribute
car.speed = 50    # Can modify directly
car.accelerate(30)


# 🔒 PART 2: Protected Members (Single Underscore)
# ================================================

class BankAccount:
    """Protected members use single underscore (convention)"""
    
    def __init__(self, owner, initial_balance):
        self.owner = owner
        # Protected attribute - should not be accessed outside class/subclasses
        self._balance = initial_balance
        self._transaction_count = 0
    
    # Public method
    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            self._increment_transaction_count()
            print(f"Deposited ${amount}")
    
    # Protected method - for internal use
    def _increment_transaction_count(self):
        self._transaction_count += 1
    
    # Protected method - can be used by subclasses
    def _validate_withdrawal(self, amount):
        return amount > 0 and amount <= self._balance
    
    # Public method using protected members
    def get_balance(self):
        return self._balance


# Protected members can still be accessed (but shouldn't be)
print("\n--- Protected Members ---")
account = BankAccount("Alice", 1000)
account.deposit(500)
print(f"Balance: ${account.get_balance()}")

# This works but violates convention:
print(f"Protected balance: ${account._balance}")  # Don't do this!
print(f"Transactions: {account._transaction_count}")  # Don't do this!


# 🔐 PART 3: Private Members (Double Underscore)
# ==============================================

class SecureVault:
    """Private members use double underscore (name mangling)"""
    
    def __init__(self, pin):
        # Private attributes - name gets mangled
        self.__pin = pin
        self.__is_locked = True
        self.__contents = []
    
    # Public method
    def unlock(self, pin):
        if self.__verify_pin(pin):
            self.__is_locked = False
            print("Vault unlocked!")
            return True
        else:
            print("Incorrect PIN!")
            return False
    
    # Private method - internal use only
    def __verify_pin(self, pin):
        return pin == self.__pin
    
    # Public method
    def add_item(self, item):
        if not self.__is_locked:
            self.__contents.append(item)
            print(f"Added {item} to vault")
        else:
            print("Vault is locked!")
    
    # Public method to safely access private data
    def show_contents(self):
        if not self.__is_locked:
            return self.__contents.copy()  # Return copy to prevent modification
        else:
            return "Vault is locked!"


# Using private members
print("\n--- Private Members ---")
vault = SecureVault(1234)

# This won't work - attribute doesn't exist with this name
try:
    print(vault.__pin)  # AttributeError
except AttributeError:
    print("Cannot access __pin directly (name mangled)")

# Must use public interface
vault.unlock(1234)
vault.add_item("Diamond")
vault.add_item("Gold")
print(f"Contents: {vault.show_contents()}")

# Name mangling creates _ClassName__attribute
# This works but defeats the purpose of private members:
print(f"Accessing private via name mangling: {vault._SecureVault__pin}")  # Don't do this!


# 📊 PART 4: Property Decorators (Pythonic Getters/Setters)
# =========================================================

class Person:
    """Using @property for controlled access"""
    
    def __init__(self, name, birth_year):
        self._name = name
        self._birth_year = birth_year
        self._email = None
    
    # Getter using @property
    @property
    def name(self):
        """Name property (read-only)"""
        return self._name
    
    # Age calculated dynamically
    @property
    def age(self):
        """Calculate age from birth year"""
        from datetime import datetime
        return datetime.now().year - self._birth_year
    
    # Email with getter and setter
    @property
    def email(self):
        """Email property with validation"""
        return self._email
    
    @email.setter
    def email(self, value):
        """Set email with validation"""
        if self._validate_email(value):
            self._email = value
        else:
            raise ValueError("Invalid email format")
    
    # Private validation method
    def _validate_email(self, email):
        return "@" in email and "." in email


# Using properties
print("\n--- Property Decorators ---")
person = Person("Alice", 1990)

# Accessing like attributes, but actually calling methods
print(f"Name: {person.name}")
print(f"Age: {person.age}")

# Setting email through setter
person.email = "alice@example.com"
print(f"Email: {person.email}")

# This will raise an error
try:
    person.email = "invalid-email"
except ValueError as e:
    print(f"Error: {e}")


# 🏢 PART 5: Complete Example - Employee Management
# =================================================

class Employee:
    """Comprehensive encapsulation example"""
    
    # Class-level private attribute
    __company_name = "Tech Corp"
    
    def __init__(self, name, employee_id, salary):
        # Public attribute
        self.name = name
        
        # Protected attributes
        self._employee_id = employee_id
        self._department = None
        
        # Private attributes
        self.__salary = salary
        self.__performance_rating = 0
        self.__bonus = 0
    
    # Public method
    def get_public_info(self):
        """Return publicly available information"""
        return f"{self.name} (ID: {self._employee_id})"
    
    # Property for salary (read-only from outside)
    @property
    def salary(self):
        """Get current salary"""
        return self.__salary
    
    # Property for total compensation
    @property
    def total_compensation(self):
        """Calculate total compensation including bonus"""
        return self.__salary + self.__bonus
    
    # Protected method - for use in subclasses
    def _calculate_bonus(self):
        """Calculate bonus based on performance"""
        if self.__performance_rating >= 4:
            self.__bonus = self.__salary * 0.15
        elif self.__performance_rating >= 3:
            self.__bonus = self.__salary * 0.10
        else:
            self.__bonus = self.__salary * 0.05
    
    # Public method with validation
    def set_performance_rating(self, rating, reviewer_id):
        """Set performance rating with validation"""
        if self.__validate_reviewer(reviewer_id):
            if 1 <= rating <= 5:
                self.__performance_rating = rating
                self._calculate_bonus()
                print(f"Performance rating set to {rating}")
            else:
                print("Rating must be between 1 and 5")
        else:
            print("Unauthorized reviewer")
    
    # Private method
    def __validate_reviewer(self, reviewer_id):
        """Check if reviewer is authorized"""
        # Simplified validation
        return reviewer_id.startswith("MGR")
    
    # Property with setter for department
    @property
    def department(self):
        return self._department
    
    @department.setter
    def department(self, dept):
        valid_departments = ["Engineering", "Sales", "HR", "Marketing"]
        if dept in valid_departments:
            self._department = dept
        else:
            raise ValueError(f"Department must be one of: {valid_departments}")


# Using the Employee class
print("\n--- Employee Management Example ---")
emp = Employee("Bob Smith", "EMP001", 75000)

# Public access
print(emp.get_public_info())

# Property access
print(f"Salary: ${emp.salary:,}")

# Setting department through property
emp.department = "Engineering"
print(f"Department: {emp.department}")

# Using public method with validation
emp.set_performance_rating(4, "MGR001")
print(f"Total compensation: ${emp.total_compensation:,}")

# Trying unauthorized access
emp.set_performance_rating(5, "EMP002")  # Won't work


# 🏛️ PART 6: Banking System with Full Encapsulation
# ==================================================

class BankingSystem:
    """Advanced encapsulation with multiple access levels"""
    
    def __init__(self):
        # Private: Internal data structures
        self.__accounts = {}
        self.__transaction_log = []
        self.__next_account_number = 1000
        
        # Protected: For subclass use
        self._interest_rate = 0.02
        self._minimum_balance = 100
    
    # Public: Create account
    def create_account(self, owner_name, initial_deposit):
        """Public method to create new account"""
        if initial_deposit >= self._minimum_balance:
            account_number = self.__generate_account_number()
            
            # Private inner dictionary for account data
            self.__accounts[account_number] = {
                'owner': owner_name,
                'balance': initial_deposit,
                'status': 'active',
                'pin': None
            }
            
            self.__log_transaction(account_number, "Account created", initial_deposit)
            print(f"Account {account_number} created for {owner_name}")
            return account_number
        else:
            print(f"Minimum deposit is ${self._minimum_balance}")
            return None
    
    # Private: Generate account number
    def __generate_account_number(self):
        """Private method for internal use"""
        account_number = f"ACC{self.__next_account_number}"
        self.__next_account_number += 1
        return account_number
    
    # Private: Log transactions
    def __log_transaction(self, account_number, transaction_type, amount):
        """Private method to log all transactions"""
        from datetime import datetime
        self.__transaction_log.append({
            'timestamp': datetime.now(),
            'account': account_number,
            'type': transaction_type,
            'amount': amount
        })
    
    # Public: Set PIN (with encapsulation)
    def set_pin(self, account_number, pin):
        """Set PIN for account"""
        if account_number in self.__accounts:
            if self.__validate_pin_format(pin):
                self.__accounts[account_number]['pin'] = self.__hash_pin(pin)
                print("PIN set successfully")
            else:
                print("PIN must be 4 digits")
        else:
            print("Account not found")
    
    # Private: Validate PIN format
    def __validate_pin_format(self, pin):
        """Private validation method"""
        return len(str(pin)) == 4 and str(pin).isdigit()
    
    # Private: Hash PIN for security
    def __hash_pin(self, pin):
        """Private method to hash PIN"""
        # Simplified hashing for demo
        return sum(int(d) * (i + 1) for i, d in enumerate(str(pin)))
    
    # Public: Get balance (requires PIN)
    def get_balance(self, account_number, pin):
        """Public method with security check"""
        if self.__verify_pin(account_number, pin):
            return self.__accounts[account_number]['balance']
        else:
            print("Invalid PIN")
            return None
    
    # Private: Verify PIN
    def __verify_pin(self, account_number, pin):
        """Private security method"""
        if account_number in self.__accounts:
            stored_pin = self.__accounts[account_number]['pin']
            return stored_pin == self.__hash_pin(pin)
        return False
    
    # Protected: For subclass extensions
    def _get_account_status(self, account_number):
        """Protected method for subclasses"""
        if account_number in self.__accounts:
            return self.__accounts[account_number]['status']
        return None


# Using the banking system
print("\n--- Banking System Example ---")
bank = BankingSystem()

# Create account
acc_num = bank.create_account("Alice Johnson", 500)

# Set PIN
bank.set_pin(acc_num, 1234)

# Check balance with PIN
balance = bank.get_balance(acc_num, 1234)
if balance:
    print(f"Balance: ${balance}")

# Try with wrong PIN
bank.get_balance(acc_num, 9999)

# Cannot access private attributes
try:
    print(bank.__accounts)  # Won't work
except AttributeError:
    print("Cannot access private __accounts directly")


# 🎮 PRACTICE EXERCISES
# =====================

print("\n" + "="*50)
print("YOUR TURN - EXERCISES")
print("="*50)

# Exercise 1: Create a PasswordManager class
# TODO: Create a PasswordManager class with:
# - Private attribute: __master_password
# - Private attribute: __passwords (dictionary)
# - Public method: set_master_password(password)
# - Public method: add_password(service, password) - requires master password
# - Public method: get_password(service, master_password) - returns password if master is correct
# - Private method: __verify_master_password(password)

# Your code here:


# Exercise 2: Create a Student class with grades
# TODO: Create a Student class with:
# - Public attribute: name
# - Protected attribute: _student_id
# - Private attribute: __grades (list)
# - Property: gpa (calculated from grades, read-only)
# - Public method: add_grade(grade) - validates grade is 0-100
# - Protected method: _calculate_gpa()

# Your code here:


# Exercise 3: Create a CreditCard class
# TODO: Create a CreditCard class with:
# - Private attributes: __card_number, __cvv, __balance
# - Public attribute: owner_name
# - Property: balance (read-only)
# - Property: masked_card_number (returns ****-****-****-1234)
# - Public method: charge(amount, cvv) - validates CVV before charging
# - Private method: __validate_cvv(cvv)

# Your code here:


# 🎯 CHALLENGE EXERCISE
# ====================
# Create a SmartHome class with:
# - Private dict: __devices (stores device states)
# - Private attribute: __security_code
# - Protected method: _log_activity(action)
# - Public method: add_device(device_name, initial_state="off")
# - Public method: control_device(device_name, state, security_code)
# - Property: device_count (read-only)
# - Property: activity_log (returns copy of log)
# Use proper encapsulation for security!

# Your code here:


# 💡 ENCAPSULATION TIPS:
# - Use public members for the interface you want to expose
# - Use protected (_) for internal use and subclass access
# - Use private (__) for sensitive data or true implementation details
# - Prefer properties over getters/setters in Python
# - Don't access protected/private members from outside the class
# - Remember: Python's encapsulation is about convention, not enforcement

print("\n✅ Great work! You understand encapsulation! Next: 06_inheritance.py") 