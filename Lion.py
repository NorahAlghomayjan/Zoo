
from Animal import Animal

class Lion (Animal):
    def __init__(self,name,owner="",age=1,happiness_level=0,health_level=0,) -> None:
        super().__init__(name,age,happiness_level,health_level)
        self.owner = owner

    def feed(self):
        self.happiness_level += 1
        self.health_level += 1
