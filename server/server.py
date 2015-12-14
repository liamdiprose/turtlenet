import socket # Obviously need a network server
import select # Allow IO multiplexing to handle multiple connections on one thread

class Turtle(object)
    def __init__(self):
        self.location = (None, None, None)
        self.inventory = []
        self.id = 00000  # Used to handle each turtle without getting confused

    def dig(self, direction="front"):
        #TODO

    def move(self, direction="forward"):
        #TODO

    def getSurroundings(self):
        #TODO
