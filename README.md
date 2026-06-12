__init__ Method: The constructor method that initializes each new Rectangle object with the mandatory length and width integer values.
__iter__ Method: To make a custom class iterable in Python, it must implement the __iter__ method. Instead of writing a whole separate iterator class with tracking indexes and a __next__ method, using a generator expression (item for item in ...) handles everything automatically. Generators implicitly create the required iterator state machine behind the scenes, yielding the configured dictionaries in the exact sequence requested.
To Run this file 
cd C:\RECTANGLE_PROJECT
python rectangle.py
Once you press Enter, your terminal will immediately print the following output:
Iterating over the Rectangle instance:
{'length': 20}
{'width': 10}
<img width="1830" height="544" alt="image" src="https://github.com/user-attachments/assets/e6b83928-c5c3-4190-812c-97a4ab1a835e" />
<img width="1830" height="544" alt="image" src="https://github.com/user-attachments/assets/286768a0-67ab-423f-af71-0136e5f89d44" />
