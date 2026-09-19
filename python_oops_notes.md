# Python OOP (Object-Oriented Programming) — Complete Notes

---

## 1. What Is OOP and Why Use It?

OOP organizes code around **objects** — bundles of data (attributes) and behavior (methods) — instead of just functions operating on loose data. Benefits:

- **Modularity** — each class is a self-contained unit
- **Reusability** — inheritance lets you extend existing code instead of rewriting it
- **Scalability** — easier to model complex, real-world systems
- **Maintainability** — changes are localized to the relevant class

---

## 2. Classes and Objects

```python
class Dog:
    pass

d = Dog()               # d is an OBJECT (instance) of the CLASS Dog
print(type(d))           # <class '__main__.Dog'>
```

A **class** is a blueprint. An **object** is the actual thing built from that blueprint — you can create many objects from one class.

---

## 3. The `__init__` Constructor

```python
class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

d1 = Dog("Rex", "Labrador")
d2 = Dog("Bella", "Poodle")
print(d1.name, d1.breed)   # Rex Labrador
print(d2.name, d2.breed)   # Bella Poodle
```

`__init__` runs automatically the moment an object is created. `self` refers to *that specific object* — it's how each instance keeps its own data separate.

---

## 4. Instance Variables vs Class Variables

```python
class Dog:
    species = "Canis familiaris"   # CLASS variable — shared by every instance

    def __init__(self, name):
        self.name = name             # INSTANCE variable — unique per object

d1 = Dog("Rex")
d2 = Dog("Bella")

print(d1.species, d2.species)   # Canis familiaris   Canis familiaris
print(d1.name, d2.name)         # Rex   Bella

Dog.species = "Canis lupus familiaris"   # changing it on the CLASS affects ALL instances
print(d1.species)                          # Canis lupus familiaris
print(d2.species)                          # Canis lupus familiaris
```

---

## 5. Instance Methods vs Class Methods vs Static Methods

```python
class Dog:
    species = "Canis familiaris"

    def __init__(self, name):
        self.name = name

    def bark(self):                     # instance method — operates on THIS object
        return f"{self.name} says Woof!"

    @classmethod
    def from_string(cls, data_str):     # class method — operates on the CLASS
        name = data_str.split("-")[0]
        return cls(name)                # common use: alternative constructors

    @staticmethod
    def is_valid_name(name):            # static method — no self, no cls
        return len(name) > 0            # just a utility grouped inside the class

d = Dog.from_string("Rex-Labrador")
print(d.bark())                          # Rex says Woof!
print(Dog.is_valid_name("Rex"))          # True
```

| Type | First parameter | Access to | Called via |
|---|---|---|---|
| Instance method | `self` | The specific object's data | `obj.method()` |
| Class method | `cls` | The class itself (not one object) | `Class.method()` or `obj.method()` |
| Static method | none | Neither — just a plain function in the class's namespace | `Class.method()` or `obj.method()` |

---

## 6. The Four Pillars of OOP

### 6.1 Encapsulation
Bundling data with the methods that operate on it, and controlling access to that data.

```python
class BankAccount:
    def __init__(self, balance):
        self._balance = balance      # "protected" by convention (single underscore)
        self.__pin = "1234"           # "private" — name-mangled (double underscore)

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount

    def get_balance(self):
        return self._balance

acc = BankAccount(1000)
acc.deposit(500)
print(acc.get_balance())          # 1500
# print(acc.__pin)                 # AttributeError
print(acc._BankAccount__pin)      # '1234' — still reachable; Python has no TRUE private
```

### 6.2 Abstraction
Hiding internal implementation details and exposing only what's necessary — e.g. `acc.deposit(500)` hides how the balance is actually stored or validated. Enforced more strictly with abstract base classes (Section 14).

### 6.3 Inheritance
```python
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "Some generic sound"

class Dog(Animal):              # Dog inherits from Animal
    def speak(self):             # method OVERRIDING
        return f"{self.name} says Woof!"

d = Dog("Rex")
print(d.speak())                 # Rex says Woof!
print(isinstance(d, Animal))     # True — a Dog IS-A Animal
```

### 6.4 Polymorphism
The same method name behaves differently depending on which object calls it.

```python
class Cat(Animal):
    def speak(self):
        return f"{self.name} says Meow!"

animals = [Dog("Rex"), Cat("Whiskers")]
for a in animals:
    print(a.speak())
# Rex says Woof!
# Whiskers says Meow!
```

---

## 7. Access Modifiers — Public, Protected, Private

| Convention | Syntax | Meaning |
|---|---|---|
| Public | `self.name` | Accessible from anywhere (the default) |
| Protected | `self._name` | Convention only, meaning "internal use" — still fully accessible |
| Private | `self.__name` | Name-mangled to `_ClassName__name` — discourages, but doesn't prevent, outside access |

Python has **no true access enforcement** like Java's `private` keyword — it relies on convention (`_`) and name mangling (`__`) rather than hard restrictions.

---

## 8. `super()` and Method Overriding

```python
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "..."

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)          # calls the PARENT's __init__
        self.breed = breed

    def speak(self):
        parent_sound = super().speak()   # can still call the parent's version too
        return f"{self.name} the {self.breed} says Woof! (parent said: '{parent_sound}')"

d = Dog("Rex", "Labrador")
print(d.speak())
```

`super()` lets a subclass **extend** a parent's behavior instead of fully rewriting it — avoids duplicating `__init__`/method logic across every subclass.

**Why `super()` instead of calling the parent class by name directly?**

```python
class Dog(Animal):
    def __init__(self, name, breed):
        Animal.__init__(self, name)   # works, but hardcodes the parent's name
        self.breed = breed
```

This works for simple single inheritance, but breaks down with multiple inheritance — `super()` doesn't hardcode a specific parent; it defers to whatever the **MRO** says comes next, which makes the next example possible.

**`super()` with multiple inheritance — "cooperative" calls following the MRO:**

```python
class A:
    def __init__(self):
        print("A init")

class B(A):
    def __init__(self):
        super().__init__()
        print("B init")

class C(A):
    def __init__(self):
        super().__init__()
        print("C init")

class D(B, C):
    def __init__(self):
        super().__init__()
        print("D init")

D()
# A init
# C init
# B init
# D init
```

Each `super().__init__()` call doesn't jump straight to "its own parent" — it hands off to the **next class in the MRO** (`D → B → C → A → object`), which is why `C`'s `__init__` runs before control returns to `B`. This is the classic demonstration that `super()` follows the MRO, not a naive "my direct parent" lookup — a common interview trip-up.

> Note: `super()` with no arguments is Python 3 shorthand for `super(Dog, self)` — the explicit form is still valid and is required in Python 2.

---

## 9. Method Overloading — Why Python Doesn't Really Have It

```python
class Calculator:
    def add(self, a, b):
        return a + b

    def add(self, a, b, c):     # this OVERWRITES the previous add() entirely
        return a + b + c

calc = Calculator()
# calc.add(2, 3)             # TypeError — the 2-argument version no longer exists!
print(calc.add(2, 3, 4))      # 9
```

Unlike Java/C++, Python does **not** support true method overloading — redefining a method just replaces the earlier one. Achieve similar flexibility with:

```python
# Default arguments
class Calculator:
    def add(self, a, b, c=0):
        return a + b + c

calc = Calculator()
print(calc.add(2, 3))         # 5
print(calc.add(2, 3, 4))      # 9

# *args for a variable number of arguments
class Calculator:
    def add(self, *args):
        return sum(args)

calc = Calculator()
print(calc.add(1, 2, 3, 4))   # 10
```

---

## 10. Types of Inheritance & Method Resolution Order (MRO)

**1. Single Inheritance** — one child, one parent.

```python
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} makes a sound"

class Dog(Animal):
    def speak(self):
        return f"{self.name} says Woof!"

d = Dog("Rex")
print(d.speak())          # Rex says Woof!
```

**2. Multilevel Inheritance** — a chain: grandparent → parent → child.

```python
class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        return f"{self.name} is eating"

class Dog(Animal):
    def bark(self):
        return f"{self.name} is barking"

class Puppy(Dog):
    def play(self):
        return f"{self.name} is playing"

p = Puppy("Tiny")
print(p.eat())      # Tiny is eating    — inherited from Animal
print(p.bark())      # Tiny is barking   — inherited from Dog
print(p.play())      # Tiny is playing   — defined on Puppy itself
```

**3. Hierarchical Inheritance** — multiple children inherit from the same parent.

```python
class Animal:
    def __init__(self, name):
        self.name = name

class Dog(Animal):
    def speak(self):
        return f"{self.name} says Woof!"

class Cat(Animal):
    def speak(self):
        return f"{self.name} says Meow!"

d, c = Dog("Rex"), Cat("Whiskers")
print(d.speak())     # Rex says Woof!
print(c.speak())      # Whiskers says Meow!
```

**4. Multiple Inheritance** — one child inherits from more than one parent.

```python
class Swimmer:
    def swim(self):
        return "swims"

class Flyer:
    def fly(self):
        return "flies"

class Duck(Swimmer, Flyer):     # inherits from BOTH
    pass

d = Duck()
print(d.swim())      # swims
print(d.fly())         # flies
```

**5. Hybrid Inheritance** — a combination of the above in one hierarchy (here: hierarchical + multiple). This is also where the classic **"diamond problem"** shows up, resolved by Python's MRO:

```python
class Animal:
    def __init__(self, name):
        self.name = name

class Swimmer(Animal):          # hierarchical: both Swimmer and Flyer come from Animal
    def move(self):
        return f"{self.name} swims"

class Flyer(Animal):
    def move(self):
        return f"{self.name} flies"

class Duck(Swimmer, Flyer):      # multiple: Duck combines both branches -> HYBRID overall
    pass

d = Duck("Donald")
print(d.move())                   # Donald swims — MRO checks Swimmer before Flyer
print(Duck.__mro__)
# (<class 'Duck'>, <class 'Swimmer'>, <class 'Flyer'>, <class 'Animal'>, <class 'object'>)
```

Both `Swimmer` and `Flyer` define `move()`, so Python needs a rule to decide which one `Duck` should use — that's exactly the diamond problem. It resolves this via the **MRO** (Method Resolution Order, computed with the C3 linearization algorithm): classes are checked **left to right** as listed in `class Duck(Swimmer, Flyer)`, so `Swimmer.move()` wins. You can always inspect the exact resolution order with `ClassName.__mro__`.

---

## 11. Operator Overloading (Dunder Methods)

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __str__(self):
        return f"Point({self.x}, {self.y})"

p1 = Point(1, 2)
p2 = Point(3, 4)
p3 = p1 + p2          # Python calls p1.__add__(p2) behind the scenes
print(p3)              # Point(4, 6)
```

---

## 12. Common Magic (Dunder) Methods

| Method | Purpose | Triggered by |
|---|---|---|
| `__init__` | Constructor | `ClassName(...)` |
| `__str__` | Readable, user-facing string | `print(obj)`, `str(obj)` |
| `__repr__` | Unambiguous, developer-facing string | `repr(obj)`, console echo |
| `__len__` | Length | `len(obj)` |
| `__eq__` | Equality | `obj1 == obj2` |
| `__lt__` | Less-than | `obj1 < obj2` |
| `__add__` | Addition | `obj1 + obj2` |
| `__getitem__` | Indexing | `obj[key]` |
| `__iter__` | Iteration | `for x in obj:` |
| `__call__` | Makes the object callable | `obj()` |

```python
class Cart:
    def __init__(self):
        self.items = []

    def __len__(self):
        return len(self.items)

    def __getitem__(self, index):
        return self.items[index]

    def __repr__(self):
        return f"Cart({self.items})"

cart = Cart()
cart.items = ["apple", "banana"]
print(len(cart))     # 2
print(cart[0])         # apple
print(cart)             # Cart(['apple', 'banana'])
```

**`__str__` vs `__repr__`:** `__str__` is for end users (what `print()` shows); `__repr__` is for developers/debugging and should ideally be precise enough to recreate the object. If `__str__` is missing, Python falls back to `__repr__`.

---

## 13. Property Decorators — Pythonic Getters/Setters

```python
class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):               # getter — accessed like a plain attribute
        return self._radius

    @radius.setter
    def radius(self, value):         # setter — validation happens transparently
        if value < 0:
            raise ValueError("Radius cannot be negative")
        self._radius = value

    @property
    def area(self):                  # computed, read-only property
        return 3.14159 * self._radius ** 2

c = Circle(5)
print(c.radius)      # 5     (looks like an attribute, but actually runs a method)
c.radius = 10          # runs the setter, validates the new value
print(c.area)           # 314.159
c.radius = -5           # raises ValueError: Radius cannot be negative
```

`@property` lets you add validation or computed logic *later* without breaking existing code that does `obj.attribute` — unlike Java, you don't need `get_x()`/`set_x()` boilerplate from day one.

---

## 14. Abstract Base Classes (`abc` module)

```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass                          # no implementation — subclasses MUST override this

class Rectangle(Shape):
    def __init__(self, w, h):
        self.w = w
        self.h = h

    def area(self):
        return self.w * self.h

# shape = Shape()          # TypeError — can't instantiate an abstract class
r = Rectangle(4, 5)
print(r.area())              # 20
```

Abstract classes enforce a contract: any concrete subclass **must** implement every method decorated with `@abstractmethod`, or Python refuses to let you instantiate it.

---

## 15. Composition vs Inheritance — "has-a" vs "is-a"

```python
# Inheritance — "is-a" relationship
class Vehicle:
    def start(self):
        return "Vehicle starting"

class Car(Vehicle):        # a Car IS-A Vehicle
    pass

# Composition — "has-a" relationship
class Engine:
    def start(self):
        return "Engine started"

class Car:                  # redefined using composition instead
    def __init__(self):
        self.engine = Engine()   # a Car HAS-A Engine

    def start(self):
        return self.engine.start()

car = Car()
print(car.start())     # Engine started
```

Common guideline: **"favor composition over inheritance."** Deep inheritance chains get fragile and hard to change; composition is usually more flexible — you can swap in a different `Engine` without touching `Car`'s class hierarchy at all.

---

## 16. Complete Example — Putting It All Together

```python
from abc import ABC, abstractmethod

class Employee(ABC):
    def __init__(self, name, base_salary):
        self.name = name
        self._base_salary = base_salary     # protected

    @property
    def base_salary(self):
        return self._base_salary

    @abstractmethod
    def calculate_pay(self):
        pass

    def __str__(self):
        return f"{self.name}: ${self.calculate_pay():.2f}/month"

class SalariedEmployee(Employee):
    def calculate_pay(self):
        return self.base_salary / 12

class CommissionEmployee(Employee):
    def __init__(self, name, base_salary, sales, commission_rate=0.05):
        super().__init__(name, base_salary)
        self.sales = sales
        self.commission_rate = commission_rate

    def calculate_pay(self):
        return (self.base_salary / 12) + (self.sales * self.commission_rate)

employees = [
    SalariedEmployee("Alice", 60000),
    CommissionEmployee("Bob", 40000, sales=20000),
]

for emp in employees:
    print(emp)     # polymorphism — same print() call, different calculate_pay() per subclass
```

---

## 17. Common Interview Questions

**Q: What's the difference between a class and an object?**
A class is a blueprint/template defining attributes and behavior; an object is a concrete instance created from that blueprint, with its own copy of the instance data.

**Q: What are the four pillars of OOP?**
Encapsulation (bundling data + behavior, controlling access), Abstraction (hiding implementation details behind a simple interface), Inheritance (reusing/extending a parent class's behavior), and Polymorphism (the same method call behaving differently depending on the object).

**Q: Difference between `__str__` and `__repr__`?**
`__str__` produces a readable string for end users (used by `print()`); `__repr__` produces an unambiguous, debug-oriented string ideally precise enough to recreate the object. If only `__repr__` is defined, `print()` falls back to it.

**Q: Difference between a classmethod and a staticmethod?**
A classmethod receives the class itself (`cls`) and can access/modify class-level state — commonly used for alternative constructors. A staticmethod receives neither `self` nor `cls` — it's just a regular function namespaced inside the class for organizational purposes.

**Q: Does Python support multiple inheritance? How does it resolve conflicts?**
Yes. When two parent classes define the same method, Python resolves which one wins using the Method Resolution Order (MRO), computed via C3 linearization — checkable directly with `ClassName.__mro__`.

**Q: What's the difference between method overloading and method overriding? Does Python support overloading?**
Overriding means a subclass redefines a method already defined in its parent (Python fully supports this). Overloading means defining multiple methods with the same name but different parameter signatures — Python does **not** support true overloading; redefining a method simply replaces the earlier definition. Default arguments or `*args` are used to simulate it.

**Q: How does encapsulation actually work in Python, given there's no `private` keyword?**
Python relies on naming conventions rather than enforcement: a single leading underscore (`_name`) signals "internal use" but is still fully accessible, and a double leading underscore (`__name`) triggers name mangling (renamed internally to `_ClassName__name`), which discourages — but does not truly prevent — outside access.

**Q: What is an abstract class, and when would you use one?**
A class (inheriting from `ABC`) that can't be instantiated directly and defines one or more `@abstractmethod`s that every concrete subclass must implement. Useful for enforcing a consistent interface across multiple related classes.

**Q: When would you prefer composition over inheritance?**
When the relationship is "has-a" rather than "is-a," or when you want to swap out behavior at runtime without restructuring a class hierarchy. Composition tends to be more flexible and avoids the fragility of deep inheritance chains.

**Q: What does `super()` do?**
Calls a method from the parent class from within a subclass — most commonly `super().__init__(...)` — so the subclass can extend, rather than completely rewrite, the parent's behavior.

---

## 18. Quick Reference / Cheat Sheet

```python
class Employee:
    company = "Acme Corp"                 # class variable

    def __init__(self, name, salary):     # constructor
        self.name = name                   # instance variable
        self._salary = salary              # protected
        self.__ssn = "000-00-0000"          # private (name-mangled)

    def raise_salary(self, pct):           # instance method
        self._salary *= (1 + pct)

    @classmethod
    def from_string(cls, data):            # class method — alt constructor
        name, salary = data.split("-")
        return cls(name, float(salary))

    @staticmethod
    def is_valid(name):                    # static method — utility
        return bool(name)

    @property
    def salary(self):                      # getter
        return self._salary

    @salary.setter
    def salary(self, value):               # setter with validation
        if value < 0:
            raise ValueError("Salary can't be negative")
        self._salary = value

    def __str__(self):
        return f"{self.name}: ${self._salary}"

    def __eq__(self, other):
        return self._salary == other._salary


class Manager(Employee):                   # inheritance
    def __init__(self, name, salary, team_size):
        super().__init__(name, salary)     # call parent constructor
        self.team_size = team_size

    def raise_salary(self, pct):           # method overriding
        super().raise_salary(pct * 1.5)    # managers get a bigger raise


from abc import ABC, abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self): pass                   # abstract method — must be overridden
```

**Best practices checklist:**
- Use `_name` for internal attributes, `__name` only when you specifically need name mangling
- Prefer composition over inheritance unless there's a clear "is-a" relationship
- Use `@property` instead of manual `get_x()`/`set_x()` methods
- Use `@classmethod` for alternative constructors, `@staticmethod` for grouped utility functions
- Always call `super().__init__(...)` in a subclass constructor unless you have a specific reason not to
- Use `ABC`/`@abstractmethod` to enforce a shared interface across related classes
- Implement `__repr__` on any class you'll need to debug — it's your fallback for `print()` too
