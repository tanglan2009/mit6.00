__author__ = 'tanglan'

class Person(object):

    def __init__(self, name, birthday, race):
        self.name = name
        self.birthday = birthday
        self.race = race

    def getName(self):
        return self.name

    def getAge(self):
        return now() - self.birthday




me = Person("zhihong", 30, "east asia")

print me
print me.getName()
print me.getAge()