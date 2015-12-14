import socket # Obviously need a network server
import select # Allow IO multiplexing to handle multiple connections on one thread
import collections # Immport Queues and stacks

DEBUG = False
JOB_COUNT = 0
MACHINE_COUNT = 0

def debug(message, sender):
    if DEBUG:
        print("[{}] {}: {}".format(time, sender, message))


def get_job_id():
    JOB_COUNT += 1
    debug("Job ID {} assigned".format(JOB_COUNT))
    return JOB_COUNT

def get_machine_id():
    MACHINE_COUNT += 1
    debug("Machine ID assigned".format(MACHINE_COUNT))
    return MACHINE_COUNT

class Turtle(object)
    def __init__(self):
        self.location = (None, None, None)
        self.inventory = []
        self.jobs = collections.deque() # Queue for jobs
        self.current_job = 0000
        self.id = get_machine_id()  # Used to handle each turtle without getting confused

    def dig(self, direction="front", override=False):
        if override:
            # Queue Job at front of list
        else:
            # Queue job at back of list

    def move(self, direction="forward", override=False):
        if override:
            # Queue Job at front of list
        else:
            # Queue job at back of list

    def getSurroundings(self, override=False):
        if override:
            # Add current job to front of list
            # Queue Job at front of list,
            # Resume handing out jobs from queue
        else:
            # Queue job at back of list

