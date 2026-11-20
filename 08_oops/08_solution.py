class Father:
    def __init__(self, father_name):
        self.father_name = father_name

class Mother:
    def __init__(self, mother_name):
        self.mother_name = mother_name

class Child(Father, Mother):
    def __init__(self, father_name, mother_name):
        Father.__init__(self, father_name)
        Mother.__init__(self, mother_name)

    def display(self):
        print("Father:", self.father_name)
        print("Mother:", self.mother_name)


obj = Child("Rahul", "Priya")
obj.display()