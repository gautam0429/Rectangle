class Rectangle:
    def __init__(self, length: int, width: int):
        # Storing the dimensions directly as instance attributes
        self.length = length
        self.width = width

    def __iter__(self):
        # Returning a generator expression to satisfy Python's iterator protocol.
        # This yields the length dictionary first, then the width dictionary.
        return (item for item in [{'length': self.length}, {'width': self.width}])

if __name__ == '__main__':
    # Initializing a rectangle instance with length=20 and width=10
    rect = Rectangle(20, 10)

    # Iterating over the instance directly using a standard for-loop
    print("Iterating over the Rectangle instance:")
    for dimension in rect:
        print(dimension)
        