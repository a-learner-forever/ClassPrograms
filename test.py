class Student:
    def __init__(self, id, sname):
        self.id=id
        self.sname = sname

    def display(self):
        print('The id and name values are:', self.id, self.sname)

ob1 = Student('s001','Arun')
ob1.display()