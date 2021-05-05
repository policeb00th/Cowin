from enum import Enum
import pathlib

class CONSTANTS(Enum):
    path=str(pathlib.Path(__file__).parent.absolute())
    email="your_email@gmail.com"
    password="your_password"