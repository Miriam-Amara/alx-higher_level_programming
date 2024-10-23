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

    def to_json(self, attrs=None):
        """
        Returns the dictionary representation of the Student instance
        attributes.

        Args:
            attrs (Any): A list of strings containing the student instance
            attributes to be retrieved.
        Returns:
            dict: A dictionary representation of the specified
            Student instance attributes, suitable for JSON serialization.
        """
        new_dict = {}
        if isinstance(attrs, list):
            for value in attrs:
                if not isinstance(value, str):
                    return self.__dict__
            for key, value in self.__dict__.items():
                if key in attrs:
                    new_dict[key] = value
            return new_dict
        else:
            return self.__dict__


student_1 = Student("John", "Doe", 23)
student_2 = Student("Bob", "Dylan", 27)

j_student_1 = student_1.to_json()
j_student_2 = student_2.to_json(['first_name', 'age'])
j_student_3 = student_2.to_json(['middle_name', 'age'])

print(j_student_1)
print(j_student_2)
print(j_student_3)
