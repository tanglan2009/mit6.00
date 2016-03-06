class Frob(object):
    def __init__(self, name):
        self.name = name
        self.before = None
        self.after = None
    def setBefore(self, before):
        # example: a.setBefore(b) sets b before a
        self.before = before
    def setAfter(self, after):
        # example: a.setAfter(b) sets b after a
        self.after = after
    def getBefore(self):
        return self.before
    def getAfter(self):
        return self.after
    def myName(self):
        return self.name
p = Frob('percival')
print p.myName()



def insert(atMe, newFrob):

    if newFrob.myName() >= atMe.myName():
        newFrob.setBefore(atMe)
        atMe.setAfter(newFrob)

        return newFrob.getAfter()
    if newFrob.myName() < atMe.myName():
        newFrob.setAfter(atMe)
        atMe.setBefore(newFrob)
        return newFrob.getBefore()



eric = Frob('eric')
andrew = Frob('andrew')
ruth = Frob('ruth')
fred = Frob('fred')
martha = Frob('martha')

print insert(eric, andrew)
print insert(eric, ruth)
insert(eric, fred)
insert(ruth, martha)
#
# def findFront(start):
#     """
#     start: a Frob that is part of a doubly linked list
#     returns: the Frob at the beginning of the linked list
#     """
#     if start.getBefore() == None:
#         return start.myName()
#     else:
#         return findFront(start.getBefore())
