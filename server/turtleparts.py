from collections import deque
class CCMachine(object):
    """Base Object for Computer Craft Machines"""
    def __init__(self):
        # TODO List of basic parameters both turtles and computers have in common
        self.job_list = deque()

class Turtle(CCMachine):
    """Class for managing Turtles. Attacking not implemented"""
    def __init__(self):
        self.inventory = [None]*16
        self.location = self.locate()
        self.currentslot = self.getSelectedSlot()
        # TODO List of basic parameters specifiic to turtles

    def move(self, direction):


    def locate(self):


    def equip(self, side, slot):

    def craft(self, number):

    def select(self, slot):

    def getSelectedSlot(self):

    def getItemCount(self, slot):

    def getItemSpace(self, slot):

    def getItemDetail(self, slot):

    def equip(self, side='left'):

    def dig(self, direction):

    def place(self, direction='forward', text=''):

    def detect(self, direction='forward'):

    def inspect(self, direction):

    def drop(self, count, slot=self.currentslot, direction='forward'):

    def suck(self, count=None, direction='forward'):

    def refuel(self, quanitity):

    def transfer(self, slot, number=None):

t = Turtle
t.move('back')


class Computer(CCMachine):
    """Class for controlling Computers"""
    def __init__(self):
        # TODO List of basic parameters specific to computers
