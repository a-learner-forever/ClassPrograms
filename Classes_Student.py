class Student:
    def __init__(self, id, sname):
        self.id=id
        self.sname = sname

    def display(self):
        print('The id and name values are:', self.id, self.sname)

ob1 = Student('s001','Arun')
ob1.display()

class Vehicle:
    def __init__(self,vid,vname):
        self.vid = vid
        self.vname = vname

    def display(self):
        print('The id and name of the vehicle are', self.vid, self.vname)

ob1 = Vehicle('v001','Audi')
ob1.display()
