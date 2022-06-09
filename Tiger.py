
from Animal import Animal

class Tiger (Animal):
    def __init__(self,name,orgin="",age=1,happiness_level=0,health_level=0,) -> None:
        super().__init__(name,age,happiness_level,health_level)
        self.orgin = orgin

    def feed(self):
        self.happiness_level += 1
        self.health_level += 1
