class Chicken:
    def walk(self):
        print("Chicken is walking")
    def talk(self):
        print("Chicken is talking")

class Tiger:
    def walk(self):
        print("Tiger is walking")
    def talk(self):
        print("Tiger is talking")
    
class Parent:
    def __init__(self,duck_typing):
        duck_typing.walk()
        duck_typing.talk()
        print("This is duck typing\n")
chicken=Chicken()
tiger=Tiger()
parent=Parent(tiger)
parent_1=Parent(chicken)
