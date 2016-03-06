import datetime
class Person(object):
    def __init__(self, name):
        self.name = name
        self.birthday = None
        self.lastName = name.split(' ')[-1]

    def getLastNme(self):
        return self.lastName

    def setBirthday(self, month, day, year):
        self.birthday = datetime.date(year, month, year)

    def getAge(self):
        if self.birthday == None:
            raise ValueError
        return (datetime.date.today() - self.birthday).days

    def __lt__(self, other):
        if self.lastName == other.lastName:
            return self.name < other.name
        return self.lastName < other.lastName

    def __str__(self):
        return self.name

class MITPerson(Person):
    nextIdNum = 0

    def __init__(self, name):
        Person.__init__(self, name)
        self.idNum = MITPerson.nextIdNum
        MITPerson.nextIdNum += 1

    def getIdNum(self):
        return self.idNum

    def __lt__(self, other):
        return self.idNum < other.idNum
class UG(MITPerson):
    def __init__(self, name, classYear):
        MITPerson.__init__(self, name)
        self.year = classYear
    def getClass(self):
        return self.year



class Grad(MITPerson):
    pass
class TransferStudent(MITPerson):
    pass

def isStudent(obj):
    return isinstance(obj, UG) or isinstance(obj, Grad)





class Grades(object):
    """A mapping from students to a list of grades"""
    def __init__(self):
        """Create empty grade book"""
        self.students = [] # list of Student objects
        self.grades = {} # maps idNume -> list of grades
        self.isSorted = True  # true if self.students is sorted

    def addStudent(self, student):
        """Assumes: student is of type Student
           Add student to the grade book"""
        if student in self.students:
            raise ValueError('Duplicate student')
        self.students.append(student)
        self.grades[student.getIdNum()] = []
        self.isSorted = False


    def addGrade(self, student, grade):
        """Assumes: grade is a float
           Add grade to the list of grades for student"""


        try:
            self.grades[student.getIdNum()].append(grade)
        except KeyError:
            raise ValueError('Student not in grade book')

    def getGrades(self, student):
        """Returen a list of grades for student"""
        try:    # return copy of student's grades
            return self.grades[student.getIdNum()] [:]
        except KeyError:
            raise ValueError('Student not in grade book')




    def allStudents(self):
        """ Return a list of the students in the grade book"""

        if not self.isSorted:
            self.students.sort()
            self.isSorted = True
        return self.students[:]  # return copy of list of students




def gradeReport(course):
    """Assumes: course if of type grades"""
    report = []
    for s in course.allStudents():
        tot = 0.0
        numGrades = 0
        for g in course.getGrades(s):
            tot += g
            numGrades += 1
        try:
            average = tot/numGrades
            report.append(str(s) + '\'s mean grade is ' + str(average))

        except ZeroDivisionError:
            report.append(str(s) + ' has no grades')
    return '\n'.join(report)


ug1 = UG('Jane Doe', 2014)
ug2 = UG('John Doe', 2015)
ug3 = UG('David Henry', 2003)
g1 = Grad('John Henry')
g2 = Grad('George Steinbrenner')

six00 = Grades()
six00.addStudent(g1)
six00.addStudent(ug2)
six00.addStudent(ug1)
six00.addStudent(g2)

for s in six00.allStudents():
    six00.addGrade(s, 75)
six00.addGrade(g1, 100)
six00.addGrade(g2, 25)

six00.addStudent(ug3)

print gradeReport(six00)




















