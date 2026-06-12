Custom Classes in Python (Rectangle)
1. Problem Requirement
Create a clean Python Rectangle class that takes length: int and width: int upon initialization. The class must fully implement Python's iteration protocol, yielding custom dictionary items representing its properties sequentially: first {'length': VALUE}, followed by {'width': VALUE}.

2. Code Implementation (rectangle.py)
class Rectangle:
    def __init__(self, length: int, width: int):
        self.length = length
        self.width = width

    def __iter__(self):
        # Using a generator expression directly fulfills Python's iterator protocol.
        # It handles state tracking internally and yields the required dictionaries.
        return (item for item in [{'length': self.length}, {'width': self.width}])

if __name__ == '__main__':
    # Initialize the class object
    rect = Rectangle(20, 10)

    # Directly loop over the instance
    print("Iterating over the Rectangle instance:")
    for dimension in rect:
        print(dimension)

3. Implementation Logic Justification
Instead of building a separate, verbose iterator object class containing index tracking counters and overriding custom __next__() checks, the clean junior-developer approach is to return a generator expression (item for item in ...). In Python, any generator expression automatically produces a compliant iterator object behind the scenes. When a for loop interacts with the Rectangle instance, it queries __iter__() and seamlessly loops over the sequenced properties.

cd C:\RECTANGLE_PROJECT
python rectangle.py
4. How to Run & Output
Expected Console Output:
Iterating over the Rectangle instance:
{'length': 20}
{'width': 10}

<img width="1724" height="974" alt="image" src="https://github.com/user-attachments/assets/fed74d65-9ea2-4bf2-a575-54dfc2291092" />

<img width="1830" height="544" alt="image" src="https://github.com/user-attachments/assets/286768a0-67ab-423f-af71-0136e5f89d44" />
