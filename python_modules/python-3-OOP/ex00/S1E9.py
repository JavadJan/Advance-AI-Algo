from abc import ABC, abstractmethod


class Character(ABC):
    """Character class is an abstract class that represents a character Game of Thrones"""
    @abstractmethod
    def __init__(self, first_name: str, is_alive: bool = True):
        self.first_name = first_name
        self.is_alive = is_alive


class Stark(Character):
    """Stark class is a subclass of Character that represents a Stark character in Game of Thrones"""

    def __init__(self, first_name: str, is_alive: bool = True):
        super().__init__(first_name, is_alive)

    def die(self):
        """die method sets the is_alive attribute to False"""
        self.is_alive = False
