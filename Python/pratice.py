class Tiger:
    def walk(self):
        print("Tiger is walking")
    def talk(self):
        print("Tiger is talking")

class Eagle:
    def walk(self):
        print("Eagle is walking")
    def talk(self):
        print("Eagle is talking")

class Person:
    def catch(self,duck):
        duck.walk()
        duck.talk()
        print("So basically this is duck typing")

tiger=Tiger()
eagle=Eagle()
person=Person()
person.catch(tiger)
person.catch(eagle)