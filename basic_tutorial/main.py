import string_utils


# print("Hello, World!")
# x = 5
# y = 10
# if x > y:
#     print("x is greater than y!")
# else:
#     print("y is greater than x!")
#
# # This is a comment
# name = "dang dinh long"
# print(name)
#
# print(type(x))

# x = "awesome"
#
# def myfunc():
#   x = "fantastic"
#   print("Python is " + x)
#
# myfunc()
#
# print("Python is " + x)

# xoa_tuple = ('x', 'o', 'a', 't', 'a', 't', 'c', 'a')
#
# print(len(xoa_tuple))

# a = """Lorem ipsum dolor sit amet,
# consectetur adipiscing elit,
# sed do eiusmod tempor incididunt
# ut labore et dolore magna aliqua."""
# print(a)

# txt = "The best things in life are free!"
# print("free" in txt)

# txt = "The best things in life are free!"
# if "expensive" not in txt:
#   print("No, 'expensive' is NOT present.")

# a = "Hello, World!"
# print(a.upper())

# this_list = ["apple", "banana", "cherry"]
# print(this_list)

# def add_numbers(a, b):
#     result = a + b
#     return result
#
#
# def subtract_numbers(a, b):
#     result = a - b
#     return result
#
#
# add_result = add_numbers(1, 3)
# print(add_result)
#
# subtract_result = subtract_numbers(5, 4)
# print(subtract_result)

# this_list = ["apple", "banana", "cherry"]
# this_list[1:2] = ["blackcurrant", "watermelon"]
# print(this_list)

# this_tuple = ("apple", "banana", "cherry")
# y = list(this_tuple)
# y.append("orange")
# this_tuple = tuple(y)
# print(this_tuple)

# this_list = ["apple", "banana", "cherry"]
# for item in this_list:
#     print(item)

# this_dict = {
#     "brand": "Ford",
#     "model": "Mustang",
#     "year": 1964
# }
#
# for key in this_dict:
#     print("key: %s, value: %s" % (key, this_dict[key]))

# x = lambda a, b: a * b
# print(x(5, 6))


# class Car:
#     def __init__(self, make, model):
#         self.make = make
#         self.model = model
#
#     def display_info(self):
#         print("this car is made from: %s, with model: %s" % (self.make, self.model))
#
#
# toyota_vios = Car("steel", "vios 2024")
# toyota_vios.display_info()


# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def __str__(self):
#         return f"{self.name}({self.age})"
#
#     def print_name(self):
#         print(self.name, self.age)
#
#
# class Student(Person):
#     pass
#
#
# p1 = Person("John", 36)
# p1.age = 50
# print(p1)

# student1 = Student("Mike", 50)
# student1.full_name = "v1"
# student1.print_name()
# print(student1.full_name)

# string_utils.greeting("Dang Long")

# import platform
#
# x = platform.version()
# print(x)

# from numpy import random
# import numpy as np
#
# arr = np.array([1, 2, 3, 4, 5])
#
# random.shuffle(arr)
#
# print(arr)

import numpy

speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]

x = numpy.mean(speed)

print(x)