#!/usr/bin/python3

"""
This module defines Student class for representing a student.
"""


class Student:
    """
    A class representing a student.
    """

    def __init__(self, first_name, last_name, age):
        """
        Initializes a student instance with first_name, last_name, age.

        Args:
            first_name (str): The student's first name.
            last_name (str): The student's last name.
            age (int): The student's age.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        Returns the dictionary representation of the Student instance
        attributes.

        Returns:
            dict: A dictionary representation of the Student instance,
            suitable for JSON serialization.
        """
        return self.__dict__


# students = [Student("John", "Doe", 23), Student("Bob", "Dylan", 27)]

# for student in students:
#     j_student = student.to_json()
#     print(type(j_student))
#     print(j_student['first_name'])
#     print(type(j_student['first_name']))
#     print(j_student['age'])
#     print(type(j_student['age']))
