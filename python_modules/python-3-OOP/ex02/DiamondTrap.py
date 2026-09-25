from S1E7 import Baratheon, Lannister

class King(Baratheon, Lannister):
	"""DiamondTrap class is a subclass of Baratheon and Lannister that represents a DiamondTrap character in Game of Thrones"""

	def __init__(self, first_name: str, is_alive: bool = True):
		super().__init__(first_name, is_alive)

	def die(self):
		"""die method sets the is_alive attribute to False"""
		self.is_alive = False

	def set_family_name(self, family_name: str):
		"""set_family_name method sets the family_name attribute"""
		self.family_name = family_name

	def set_eyes(self, eyes: str):
		"""set_eyes method sets the eyes attribute"""
		self.eyes = eyes	

	def set_hairs(self, hairs: str):
		"""set_hairs method sets the hairs attribute"""
		self.hairs = hairs

	def get_eyes(self):
		"""get_eyes method returns the eyes attribute"""
		return self.eyes

	def get_hairs(self):
		"""get_hairs method returns the hairs attribute"""
		return self.hairs
	
	def __str__(self):
		"""__str__ method returns a string representation of the DiamondTrap character"""
		return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

	def __repr__(self):
		"""__repr__ method returns a string representation of the DiamondTrap character"""
		return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"