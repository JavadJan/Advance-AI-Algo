from abc import ABC, abstractmethod
from S1E9 import Character


class Baratheon(Character):
    """Baratheon class is a subclass of Character that represents a Baratheon character in Game of Thrones"""

    def __init__(self, first_name: str, is_alive: bool = True, family_name: str = "Baratheon", eyes: str = "brown", hairs: str = "dark"):
        super().__init__(first_name, is_alive)
        self.family_name = family_name
        self.eyes = eyes
        self.hairs = hairs

    def die(self):
        """die method sets the is_alive attribute to False"""
        self.is_alive = False

    # <bound method Baratheon.__str__ of Vector: ('Baratheon', 'brown', 'dark')>
    def __str__(self):
        """__str__ method returns a string representation of the Baratheon character"""
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    # <bound method Baratheon.__repr__ of Vector: ('Baratheon', 'brown', 'dark')>
    def __repr__(self):
        """__repr__ method returns a string representation of the Baratheon character"""
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"


class Lannister(Character):
    """Lannister class is a subclass of Character that represents a Lannister character in Game of Thrones"""

    def __init__(self, first_name: str, is_alive: bool = True, family_name: str = "Lannister", eyes: str = "blue", hairs: str = "light"):
        super().__init__(first_name, is_alive)
        self.family_name = family_name
        self.eyes = eyes
        self.hairs = hairs

    def create_lannister(first_name: str, is_alive: bool = True):
        """create_lannister method creates a new Lannister character"""
        return Lannister(first_name, is_alive)

    def die(self):
        """die method sets the is_alive attribute to False"""
        self.is_alive = False

    def __str__(self):
        """__str__ method returns a string representation of the Lannister character"""
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    def __repr__(self):
        """__repr__ method returns a string representation of the Lannister character"""
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"
