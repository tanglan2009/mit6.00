import datetime

class Person(object):
    def __init__(self, name):
        """Create a person called name"""
        self.name = name
        self.birthday = None
        self.lastName = name.split(' ')[-1]

    def getLastName(self):
        """return self's last name"""
        return self.lastName

    def setBirthday(self, monty, day, year):
        """sets self's birthday to birthDate"""
        self.birthday = datetime.date(year, monty, day)

    def getAge(self):
        """returns self's current age in days"""
        if self.birthday == None:
            raise ValueError
        return (datetime.date.today() - self.birthday).days

    def __lt__(self, other):
        """retun True if self's name is lexicographically less
        than other's name, and False otherwise.
        """
        if self.lastName == other.lastName:
            return self.name < other.name
        return self.lastName < other.lastName

    def __str__(self):
        """return self's name"""
        return self.name


me = Person('William Eric Grimson')
print me
print me.getLastName()
print me.setBirthday(1,2,1927)
print me.getAge()/365

her = Person("Cher")
print her.getLastName()
print"------------------"
plist = [me, her]
for p in plist:
    print p
plist.sort()
for p in plist:
    print p
print"------------------"


class MITPerson(Person):
    nextIdNum = 0 # next ID number to assign

    def __init__(self, name):
        Person.__init__(self, name) # initialize Person attributes
        # new MITPerson attribute: a unique ID number
        self.idNum = MITPerson.nextIdNum
        MITPerson.nextIdNum += 1

    def getIdNum(self):
        return self.idNum

    # sorting MIT people uses their ID number, not name!
    def __lt__(self, other):
        return self.idNum < other.idNum


p1 = MITPerson('Eric')
p2 = MITPerson('John')
p3 = MITPerson('John')
p4 = Person('John')

print p1
print p1.getIdNum()
print p2.getIdNum()
print p1 < p2  # equivalent to p1.__lt__(p2)
print p3 < p2
print p4 < p1  # equivalent to p4.__lt__(p1)
#print p1 < p4  # equivalent to p1.__lt__(p4)











