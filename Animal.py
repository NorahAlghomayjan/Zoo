
from sys import implementation


class Animal:
    def __init__(self,name,age=1,happiness_level=0,health_level=0) -> None:
        self.name = name
        self.age = age
        self.happiness_level = happiness_level
        self.health_level = health_level

    def display_info(self):
        print(f"name: {self.name} , happiness level:{self.happiness_level} , health level: {self.health_level}")
    
    def feed(self):
        raise NotImplementedError