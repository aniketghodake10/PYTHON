### Extras ###
"""
* multuple line code backslash or ()
* Typecasting - explicit  - we tell python by using function str, int
               implicit - python dies it by own, int+float = float
* F STRING
* enumerate - gives tuple of (index, value))
* with - __enter__() method → runs setup and returns the resource.
         __exit__() method → runs cleanup when the block ends.
         useful while open('file', 'r')
"""
x=1+2\
    +3
x=(1+2
   +3)

strx = 'aniket'
print("hi {strx}".format(strx=strx))
print(f"hi {strx}")

for i, j in enumerate(strx):
    print(i, j)


class Demo:
    def __enter__(self):
        print("Entering context...")
        return "Hello from __enter__"

    def __exit__(self, exc_type, exc_value, traceback):
        print("Exiting context...")
with Demo() as val:
    print(val)



### PRINT ###
""" 
* escape char backslash , single quote can be used without backslash if we use double quote outside
* sep, end, triple quote
"""
print('\'aa',1,2,24,sep="  'ANIKET'  ", end='    THIS IS END')
print("""1
2
""")



### Variables ###
""" 
* multiple assignments
"""
x,y,z = 1,2,3
x=y=z=3



### STRING ###
"""
* indexing - for reverse, negative iterator is MUST (by default - positive)
             iteraor sign DECIDES and FIXES the direction
* string functions - strx.upper(), lower, replace, split, endswith, startswith, count
                     isnumeric, isalnum
"""
strx="ANIKETghodake"
print(strx[-1:4:-3])
print(strx[::-1])
print(strx[:0:-1])
print(strx[-2::-1])
print(strx[:4])
print(strx[-2::])
print(strx.replace("A", "REPLACE"))
print(strx.split("A"))



### IF-ELSE, for , while, break, continue ###
"""
* continue - if condition is met, it will skip below code and start new interation
* break - we can use break in while loop also
"""
for i in range(1,10,3):
    print(i)
i=1
while (i<11):
    print(i)
    i=i+3



### LIST ###
"""
* functions - append, pop (add and delete at end)
              insert
              reverse list - reversed(lst), lst.reverse(), lst[::-1]
              list comprehension
"""
lst = [1,2,3,4,5]
print(lst[:0:-1])
lst.insert(-1, 1000) # insert adds element just element with provided index
print(lst)
print([i**2 for i in lst if i!=1 if i!=2])



### DICTIONARY ###
"""
* functions - del, mydict.pop('z')
              mydict.keys(), values, items (list of key value pair)
              empty dict a={}
"""
mydict = {'x':1, 'y':2, 'z':3}
print(mydict)
del mydict['z']
print(mydict.items())



### SETS ###
"""
* functions - union a.union(b), intersection
              add, remove
              empty set a=set()
"""
myset = {1,2,3,4,5}
myset2 = set([1,2,3,4,5,5,6])
print(type(myset), type(myset2))
print(myset, myset2, myset.intersection(myset2))



### TUPLE ###
"""
* functions - count
"""
mytuple = (1,2,3,4,5)
mytuple2 = mytuple[::-1]
print(mytuple, mytuple2, mytuple2.count(5))



### FUNCTION ###
"""
* function arguments - positional arguments - exact position of arg
                       keyword arguments - explicitly naming the parameter
                       Arbitrary Positional Arguments (*args)- tuple of infinite positional arguments
                       Arbitrary Keyword Arguments (**kwargs) - dictionary of infinite keyword arguments
                       Mixing Argument Types
"""
y = 89 #outside function is always global
def func1():
    global y
    y = 55
    print(y)
func1()



### LAMBDA FUNCTION, MAP, FILTER, REDUCE ###
"""
* map - Applies a function to each item in an iterable (like a list) and returns a new iterable (map object).
* filter - Filters items in an iterable based on a condition (returns only those for which the function is True).
* reduce - Applies a function cumulatively to the items of an iterable (reducing it to a single value).
           Unlike map and filter, reduce is not a built-in; it’s in the functools module.
"""
addition = lambda x, y: x + y
print(addition(1, 2))

numbers = [1, 2, 3, 4, 5]
squared = map(lambda x: x**2, numbers)

numbers = [1, 2, 3, 4, 5, 6]
evens = filter(lambda x: x % 2 == 0, numbers)

from functools import reduce
total = reduce(lambda x, y: x + y, evens)



### EXCEPTION HANDLING ###
"""
* finally - Always runs (cleanup tasks, closing files, releasing resources), even if return in a function is called before
* raise a error - ValueError('This is Value error')
"""
try:
    num = 0
    result = 10 / num
except Exception as e:
    print("ERROR is ", e)
except ZeroDivisionError:
    print("You cannot divide by zero.")
else:
    print("Result is:", result)
finally:
    print("Execution completed.")
    #raise ValueError("This is Value error")



### OOPS ###
"""
* self - object itself is passed as parameter
* Instance methods - part of object
  Static method - not a part of object, just normal methods which is attached to class
* 1) Encapsulation - getter and setter to hide private variable (property decorator)
  2) Inheritance - subclass - inherit attributes and methods from another class
                 single, multiple - inherit from two classes class1(class2, class3), multilevel - class2(class1), class3(class2)
                 we have to include parent class params in child class constructor
                 super - call methods (usually the constructor) from its parent class. - super().method_from_parent_class()
                         or use class name - parentclass.method()
"""
class Car:
    xx = 5 # class variable
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def start(self):
        print(f"{self.brand} {self.model} is starting...")

    def setxx(self, xx):
        self.xx = xx

    @staticmethod
    def add(a, b):
        return a + b

    @classmethod
    def change_xx(cls, xx):
        cls.xx = xx
my_car = Car("Toyota", "Corolla")
my_car.start()  # Output: Toyota Corolla is starting...
print(my_car.xx, my_car.brand, my_car.model)
my_car.xx,my_car.brand = 79,97
print(my_car.xx, my_car.brand, my_car.model)
Car.xx = 6666
print(my_car.xx, my_car.brand, my_car.model)
my_car.setxx(555)
print(my_car.xx, my_car.brand, my_car.model)
my_car.change_xx(666)
print(my_car.xx, my_car.brand, my_car.model, Car.xx)

class Student:
    def __init__(self, name):
        self.__name = name  # private variable

    # Getter
    def get_name(self):
        return self.__name

    # Setter
    def set_name(self, name):
        if len(name) > 0:
            self.__name = name
        else:
            print("Name cannot be empty!")
s = Student("Aniket")
print(s.get_name())  # Output: Aniket
s.set_name("Rahul")
print(s.get_name())  # Output: Rahul

#using property decorator
class Student:
    def __init__(self, name):
        self.__name = name

    @property  # Getter
    def name(self):
        return self.__name

    @name.setter  # Setter
    def name(self, value):
        if len(value) > 0:
            self.__name = value
        else:
            print("Name cannot be empty!")
s = Student("Aniket")
print(s.name)  # Access without parentheses (getter)
s.name = "Rahul"  # Modify using setter
print(s.name)     # Output: Rahul
s.name = ""       # Output: Name cannot be empty!



### MULTITHREADING ###
"""
* When to use - I/O-bound tasks:
                  Downloading files from the internet
                  Reading/writing files
                  Waiting for APIs / database queries
* ThreadPoolExecutor - I/O-bound tasks, ProcessPoolExecutor - CPU bound tasks
"""
import time
from concurrent.futures import ThreadPoolExecutor
import threading

class MyThread(threading.Thread):
    def __init__(self, name):
        threading.Thread.__init__(self)
        self.name = name

    def run(self):
        for i in range(3):
            print(f"Thread {self.name} is running")
            time.sleep(1)
t1 = MyThread("A")
t2 = MyThread("B")
t1.start()
t2.start()
t1.join() # Wait for both to finish
t2.join() # Wait for both to finish
print("All threads completed.")

def task(name):
    print(f"Starting task {name}")
    time.sleep(2)
    print(f"Finished task {name}")

# Create a ThreadPoolExecutor with 3 worker threads
with ThreadPoolExecutor(max_workers=3) as executor:
    executor.submit(task, "A")
    executor.submit(task, "B")
    executor.submit(task, "C")
    executor.submit(task, "D")  # Will wait until a worker is free
#OR
print("BELOW using map")
with ThreadPoolExecutor(max_workers=3) as executor:
    executor.map(task, ['A', 'B', 'C', 'D'])



### REQUESTS and OS ###
"""
* 
"""
import requests

response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
print(response.status_code)  # HTTP status code (e.g., 200)
print(response.text)         # Response as text
print(response.json())       # Convert JSON response to Python dict

data = {"title": "foo", "body": "bar", "userId": 1}
response = requests.post("https://jsonplaceholder.typicode.com/posts", json=data)
print(response.status_code)  # 201
print(response.json())       # Created resource

import os

print("=== 1. Current Working Directory ===")
print(os.getcwd())

print("\n=== 2. Change Directory ===")
# Change to a known directory (use your path)
os.chdir(os.path.expanduser("~"))  # Change to home directory
print("Changed to:", os.getcwd())

print("\n=== 3. List Files & Directories ===")
print(os.listdir())  # Current directory
# print(os.listdir("C:/"))  # Example for specific path

print("\n=== 4. Create & Remove Directories ===")
if not os.path.exists("test_folder"):
    os.mkdir("test_folder")
    print("Folder 'test_folder' created")
if not os.path.exists("folder1/folder2"):
    os.makedirs("folder1/folder2")
    print("Nested folders created")

# Remove folders (only if empty)
os.rmdir("test_folder")
os.removedirs("folder1/folder2")
print("Folders removed")

print("\n=== 5. Create & Remove Files ===")
with open("sample.txt", "w") as f:
    f.write("Hello World")
print("File 'sample.txt' created")

os.remove("sample.txt")
print("File 'sample.txt' removed")

print("\n=== 6. Rename File/Folder ===")
with open("old_name.txt", "w") as f:
    f.write("Rename me")
os.rename("old_name.txt", "new_name.txt")
print("File renamed to 'new_name.txt'")
os.remove("new_name.txt")  # cleanup

print("\n=== 7. Path Operations ===")
path = os.path.join(os.getcwd(), "example.txt")
print("Path:", path)
print("Basename:", os.path.basename(path))
print("Dirname:", os.path.dirname(path))
print("Split:", os.path.split(path))
print("Splitext:", os.path.splitext(path))

print("\n=== 8. Check Path Existence ===")
print("Does 'example.txt' exist?", os.path.exists("example.txt"))

print("\n=== 9. Environment Variables ===")
print("PATH:", os.environ.get("PATH"))
os.environ["MY_VAR"] = "Hello"
print("MY_VAR:", os.environ.get("MY_VAR"))

print("\n=== 10. Run System Command ===")
if os.name == "nt":  # Windows
    os.system("dir")
else:  # Linux/Mac
    os.system("ls")