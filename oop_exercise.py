import random as rd
import threading
from pymongo import MongoClient

# Generate random triples
Digit_list = [[rd.randint(1, 200), rd.randint(1, 200), rd.randint(1, 200)] for i in range(10)]

# MongoDB Connection
client = MongoClient("mongodb://localhost:27017/")  # Adjust if needed
db = client["geometry_db"]
collection = db["shapes"]

data = collection.find()

# Display each document
for obj in data:
    print(obj)

# Trapezoid Class
class Trapezoid:
    def __init__(self, base1, base2, height):
        self.base1 = base1
        self.base2 = base2
        self.height = height

    def __str__(self):
        return f"{self.base1} {self.base2} {self.height}"

    @property
    def area(self):
        return (self.base1 + self.base2) / 2 * self.height

    def __le__(self, other):
        return self.area <= other.area

    def __ge__(self, other):
        return self.area >= other.area

    @area.deleter
    def area(self):
        print("Area can't be deleted (calculated property)")


# Rectangle inherits Trapezoid
class Rectangle(Trapezoid):
    def __init__(self, base1, base2):
        super().__init__(base1, base2, None)

    def __str__(self):
        return f"{self.base1} {self.base2}"

    @property
    def area(self):
        return self.base1 * self.base2


# Square inherits Rectangle
class Square(Rectangle):
    def __init__(self, base1):
        super().__init__(base1, None)

    def __str__(self):
        return f"{self.base1}"

    @property
    def area(self):
        return self.base1 ** 2


# Thread Target Function
def create_and_insert(index):
    data = Digit_list[index]
    shape_type = rd.choice(["Trapezoid", "Rectangle", "Square"])

    if shape_type == "Trapezoid":
        shape = Trapezoid(data[0], data[1], data[2])
    elif shape_type == "Rectangle":
        shape = Rectangle(data[0], data[1])
    else:
        shape = Square(data[0])

    print(f"Inserting {shape_type} with area {shape.area}")

    # Insert into MongoDB
    collection.insert_one({
        "type": shape_type,
        "base1": shape.base1,
        "base2": shape.base2,
        "height": shape.height,
        "area": shape.area
    })


# Creating and Running Threads
threads = []

for i in range(len(Digit_list)):
    t = threading.Thread(target=create_and_insert, args=(i,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

print("All shapes inserted into MongoDB!")
