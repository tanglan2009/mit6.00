class Queue(object):
    def __init__(self):
        self.ele = []

    def insert(self, e):
        self.ele.append(e)

    def remove(self):
        try:
            return self.ele.pop(0)
        except:
            raise ValueError

    # def __str__(self):
    #     return str(self.ele)


queue = Queue()
queue.insert(5)
queue.insert(6)
# print queue
print queue.remove()
print queue.remove()
queue.insert(7)
print queue.remove()