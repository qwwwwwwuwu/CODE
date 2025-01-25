class Horse():
    def __init__(self,
                 name,
                 owner):
        self.name=name
        self.owner=owner

class Person():
    def __init__(self, name):
        self.name=name

mick=Person("Mick Jagger")
stan=Horse("Stanly",
           mick)
print(stan.owner.name)
