#mutiple inheritance
class Father:
    def __init__(self):
        self.father_name = "Raj"

class Mother:
    def __init__(self):
        self.mother_name = "Priya"

class Child(Father, Mother):
    def __init__(self):
        Father.__init__(self)
        Mother.__init__(self)

    def display(self):
        print(self.father_name)
        print(self.mother_name)


c = Child()
c.display()
