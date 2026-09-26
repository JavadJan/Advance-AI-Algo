import random
import string
from dataclasses import dataclass, field
def generate_id() -> str:
	return "".join(random.choices(string.ascii_lowercase, k = 15))



#name='Edward', surname='agle', active=True, login='Eagle', id='trannxhndgtolvh'

@dataclass
class Student:
    name: str
    surname: str
    student_id: str = ""
    active: bool = True
    login: str = ""

    def __post_init__(self):
        self.login = self.name[0].upper() + self.surname
        self.student_id = generate_id()