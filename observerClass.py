__author__ = 'jeremyk23SR'

class Observer(object):
    def __init__(self):
        pass
    def update(self, other):
        pass
class Observable(object):
    def __init__(self):
        self.observers = list()
    def notifyObservers(self):
        for o in self.observers:
            o.update(self)
    def addObserver(self, o):
        self.observers.append(o)
    def removeObserver(self, o):
        self.observers.remove(self, o)
