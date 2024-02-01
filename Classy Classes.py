class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    @property
    def info(self):
     print('{}s age is {}'.format(self.name, self.age))
classproperty('age is')