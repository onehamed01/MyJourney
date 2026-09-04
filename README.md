# Software Engineering Journey

As a Self-taught Software developer who spent years starting, stopping, changing direction and rebuilding plans instead of finishing the path properly, I'm breaking this cycle of death that has lasted for several years.

This repository marks the point where I stop repeating that cycle.

**My goal is simple:**

> *Build the foundation I should have built years ago and become a real Backend Engineer through consistent self-study, problem solving, and real-world project development.*

---

# Roadmap

```text
Python Refresh
   ↓
Solid Python
OOP / Collections / Exceptions
Modules / Packages / Type Hints
Debugging
   ↓
Data Structures & Algorithms
Problem Solving / Big-O
   ↓
SQL + PostgreSQL
   ↓
HTTP / REST / JSON
   ↓
Django
   ↓
Django REST Framework
   ↓
Build Real Backend APIs
   ↓
Testing + Debugging
   ↓
Authentication / Authorization / Security
   ↓
Git + GitHub
   ↓
Docker
   ↓
CI/CD Basics
   ↓
AWS / Cloud Basics
   ↓
Architecture + System Design
   ↓
BACKEND ENGINEER
```

---



## Python Refresh

The Python Refresh stage focused on checking and strengthening my existing Python fundamentals instead of restarting from zero.

Coding exercises are stored in:

```text
PythonRefresh.py
```



### Problems

1. `analyze_orders()` — Calculate total, largest, smallest, and orders above a value.
2. `count_order_statuses()` — Dynamically count order statuses.
3. `customer_totals()` — Group orders by customer and calculate totals.
4. `paid_customers_totals()` — Filter paid orders and calculate customer totals.
5. `customer_summary()` — Build nested customer summaries.
6. `unique_words()` — Remove duplicate words while preserving order.
7. `product_info()` — Practice tuple unpacking and structured data.
8. `sales_report()` — Combine filtering, accumulation, grouping, and nested dictionaries.



# Theory

Theory is kept separate from coding exercises.

Topics covered during Python Refresh:

- Mutable vs immutable objects
- Object references
- Assignment vs copying
- `copy()`
- `is` vs `==`
- Local and global scope
- Mutable function arguments
- Basic debugging
- State tracking
- Choosing suitable data structures

---

## Solid Python

Solid Python is the current stage of this journey. The focus is on understanding Python more deeply through practical design, not just learning syntax.

The OOP work has been developed incrementally in one evolving project. I pushed the current full version of the code rather than creating a separate commit for every small edit.

### OOP — Current Progress

1. `Product` — Class structure, instance state, class attributes, class methods, stock control, and pricing behaviour.
2. `OrderItem` — Composition with `Product`, quantity, and line-total calculation.
3. `Order` — Composition with multiple order items and full-order total calculation.
4. `DiscountProduct` — Inheritance, `super()`, additional state, and method overriding.
5. Polymorphic pricing — Different product types responding to the same `final_price()` interface.

### Theory

Topics covered so far during OOP:

- Classes, objects, and instances
- `__init__` and `self`
- Instance attributes and methods
- Class attributes and `@classmethod`
- `self` vs `cls`
- Attribute shadowing
- Encapsulation
- Public and internal attributes
- `@property`
- Getters, setters, and read-only properties
- State-changing methods and validation
- Composition and HAS-A relationships
- Inheritance and IS-A relationships
- `super()`
- Method overriding
- Polymorphism
- Class responsibilities
- Object design and class relationships

### Current Position

```text
Python Refresh ✅
   ↓
Solid Python
   └── OOP ← CURRENT
```

OOP is still in progress. After the remaining object-design work, the next step will be practical OOP reinforcement projects before continuing through the rest of Solid Python.
