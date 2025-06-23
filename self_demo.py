"""
Demonstration: What happens without 'self' in class methods?
===========================================================
"""

# 🚫 CASE 1: Method without 'self' parameter
# ==========================================

class BrokenDog:
    """This class has methods without 'self' - IT WILL BREAK!"""
    
    def bark():  # ❌ Missing 'self' parameter
        print("Woof!")
    
    def wag_tail():  # ❌ Missing 'self' parameter
        print("Wagging tail...")


# Let's try to use it:
print("=== CASE 1: Methods without 'self' parameter ===")
try:
    broken_dog = BrokenDog()
    broken_dog.bark()  # This will cause an error!
except TypeError as e:
    print(f"❌ ERROR: {e}")
    print("→ Python automatically passes the instance as first argument")
    print("→ But our method has no parameters to receive it!\n")


# ✅ CASE 2: Correct way with 'self'
# ===================================

class GoodDog:
    """This class properly uses 'self'"""
    
    def bark(self):  # ✅ Has 'self' parameter
        print("Woof!")
    
    def wag_tail(self):  # ✅ Has 'self' parameter
        print("Wagging tail...")


print("=== CASE 2: Methods with 'self' parameter ===")
good_dog = GoodDog()
good_dog.bark()  # This works!
good_dog.wag_tail()  # This works too!
print("✅ Success: Methods work properly\n")


# 🤔 CASE 3: Having 'self' but not using it
# =========================================

class LazyDog:
    """This class has 'self' parameter but doesn't use it"""
    
    def bark(self):  # Has 'self' but doesn't use it
        print("Generic bark sound")  # Not using any instance data
    
    def do_math(self):  # Has 'self' but doesn't use it
        result = 2 + 2
        print(f"2 + 2 = {result}")


print("=== CASE 3: Having 'self' but not using it ===")
lazy_dog = LazyDog()
lazy_dog.bark()  # Works fine
lazy_dog.do_math()  # Works fine
print("✅ This works, but it's not utilizing object-oriented features\n")


# 💡 CASE 4: Why 'self' is important
# ==================================

class SmartDog:
    """This class shows why 'self' is useful"""
    
    def __init__(self, name):
        self.name = name  # Store data in the instance
        self.tricks = []
    
    def bark(self):
        print(f"{self.name} says: Woof!")  # Using instance data
    
    def learn_trick(self, trick):
        self.tricks.append(trick)  # Modifying instance data
        print(f"{self.name} learned: {trick}")
    
    def show_tricks(self):
        if self.tricks:  # Accessing instance data
            print(f"{self.name}'s tricks: {', '.join(self.tricks)}")
        else:
            print(f"{self.name} doesn't know any tricks yet")


print("=== CASE 4: Using 'self' to access instance data ===")
dog1 = SmartDog("Buddy")
dog2 = SmartDog("Max")

dog1.bark()  # "Buddy says: Woof!"
dog2.bark()  # "Max says: Woof!"

dog1.learn_trick("roll over")
dog1.learn_trick("fetch")
dog2.learn_trick("play dead")

dog1.show_tricks()  # Shows Buddy's tricks
dog2.show_tricks()  # Shows Max's tricks
print()


# 🎯 CASE 5: Static methods (legitimate case for no 'self')
# ========================================================

class DogUtils:
    """Utility class with static methods"""
    
    @staticmethod
    def dog_years_to_human(dog_years):  # No 'self' needed!
        return dog_years * 7
    
    @staticmethod
    def is_good_dog():  # No 'self' needed!
        return True  # All dogs are good dogs!


print("=== CASE 5: Static methods (no 'self' needed) ===")
human_years = DogUtils.dog_years_to_human(3)
print(f"3 dog years = {human_years} human years")
print(f"Is this a good dog? {DogUtils.is_good_dog()}")


# 📝 SUMMARY
# ==========
print("\n" + "="*50)
print("📝 SUMMARY: What happens without 'self'?")
print("="*50)
print("1. ❌ No 'self' parameter → TypeError when calling method")
print("2. ✅ Has 'self' but unused → Works but not OOP best practice")
print("3. ✅ Using 'self' properly → Access instance data & methods")
print("4. ✅ @staticmethod → Legitimate case for no 'self'")
print("\n💡 Rule: Always include 'self' in regular methods!") 