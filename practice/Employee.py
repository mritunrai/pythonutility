class Employee:
    def __init__(self, name, empid):
        self.name = name
        self.empid = empid

    def displayemployeeinfor(self):
        print("name " + self.name)
        print(self.empid)
