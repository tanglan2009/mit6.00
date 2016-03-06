import datetime

class Person(object):

    def __init__(self, name):
        """Create a person"""
        print "this init is clalled when a object is created!"
        self.name = name
        try:
            lastBlank = name.rindex(' ')
            self.lastName = name[lastBlank+1:]
        except:
            self.lastName = name
        self.birthday = None

    def getName(self):
        """Returns self's full name"""
        return self.name

    def getLastName(self):
        """Retruns self's last name"""
        return self.lastName

    def setBirthday(self, birthdate):
        """Assumes birthdate is of type datetime.date
        Sets self's birthday to birthdate"""
        self.birthday = birthdate

    def getAge(self):
        """Returns self's current age in days"""
        if self.birthday == None:
            raise ValueError
        # return (datetime.date.today()) - self.birthday).days

    def _lt_(self, other):
            """Returns True if self's name is lexicographically
            less than other's name, and False otherwise"""
            if self.lastName == other.lastName:
                return self.name < other.name
            return self.lastName < other.lastName

    def _str_(self):
        """Returns self's name"""
        print 'str is called!'
        return self.name


person1 = Person("zhihong")
print person1.getName()

print person1._str_()
print type(person1)