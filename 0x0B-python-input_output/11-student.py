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
            for val in attrs:
                if not isinstance(val, str):
                    return self.__dict__
            for key, value in self.__dict__.items():
                if key in attrs:
                    new_dict[key] = value
            return new_dict
        else:
            return self.__dict__

    def reload_from_json(self, json):
        """
        Replaces the attributes of the Student instance with values
        from the given json dictionary.

        Args:
            json (dict): A dictionary containing attribute names as keys
            and their corresponding values for the Student instance.
        """
        self.__dict__.update(json)
