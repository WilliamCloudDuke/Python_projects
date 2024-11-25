# Understanding multiple inheritance

class A:
    def __init__(self):
        super().__init__()
        self.prop1 = "prop1"
        self.name = "class A"

class B:
    def __init__(self):
        super().__init__()
        self.prop2 = "prop2"
        self.name = "class B"

class C(A, B):
    def __init__(self):
        super().__init__()
        
    def showprops(self):
        print(self.name)
        print(self.prop1)
        print(self.prop2)

c = C()
print(C.__mro__)
c.showprops()
