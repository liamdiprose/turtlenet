import logging
import select # Allow IO multiplexing to handle multiple connections on one thread
import socket # Obviously need a network server
import sys
from collections import deque

# Globals
BIND_ADDR = "127.0.0.1"
BIND_PORT = 54363

if len(sys.argv) == 2:
    BIND_PORT = int(sys.argv[1])
elif len(sys.argv) == 3:
    BIND_ADDR = sys.argv[1]
    BIND_PORT = sys.argv[2]

# Logging Objects
log = logging.getLogger()
log.setLevel(logging.INFO)
ch = logging.StreamHandler()
ch.setLevel(logging.INFO)
log.addHandler(ch)

# Initiate Server Socket
server = socket.socket()
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind((BIND_ADDR, BIND_PORT))
log.info("Server started on {}:{}".format(BIND_ADDR, BIND_PORT))

# Listen for incoming connections
server.listen()

# Initiate IO Monitoring
inputs = [server]
outputs = []
message_queue = {}

while inputs:
    readable, writable, exceptional = select.select(inputs, outputs, inputs)
    for s in readable:
        if s is server:
            connection, client_address = s.accept()
            log.debug("New connection from {}".format(client_address))
            connection.setblocking(0)
            inputs.append(connection)
            message_queue[connection] = deque()
            # message_queue[connection].append(HEADERS.encode()) TODO: Add heders to server
            log.debug("Created message queue")

        else:
            data = s.recv(1024)

            if data:
                log.debug(str("Received %s" % data))

            for line in open('index.html').readlines():
                message_queue[s].append(line.strip().encode())

            if s not in outputs:
                outputs.append(s)

    for s in writable:
        try:
            next_msg = message_queue[s].popleft()

        except IndexError:
            log.info("Bye Bye " + s.getpeername()[0] + "!")
            outputs.remove(s)
            inputs.remove(s)
            s.close()

        else:
            log.log(5,"Sent data to "+ s.getpeername()[0])
            s.send(next_msg)