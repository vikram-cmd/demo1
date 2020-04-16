class Fan():

    def __init__(self,wings,stand):
        self.wings = wings
        self.stand = stand
    def __str__(self):
        return f"{self.wings} often {self.stand}"

g = Fan("This fan rotates well","now")
print(g)