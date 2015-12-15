import logging
import select # Allow IO multiplexing to handle multiple connections on one thread
import socket # Obviously need a network server
import sys
from collections import deque

# Globals
BIND_ADDR = "localhost"
BIND_PORT = 54363

if len(sys.argv) == 2:
    BIND_PORT = int(sys.argv[1])
elif len(sys.argv) == 3:
    BIND_ADDR = sys.argv[1]
    BIND_PORT = sys.argv[2]

# Logging Objects
log = logging.getLogger()
log.setLevel(logging.DEBUG)
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
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
headers = "HTTP/1.1 200 OK\n\n"

def closeconn(sock):
    inputs.remove(sock)
    if s in outputs:
       outputs.remove(s)
    del message_queue[sock]
    sock.close()

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
            message_queue[connection].append(headers.encode())
            message_queue[connection].append("Hello Turtle, I'm World.\n".encode())
            log.debug("Created message queue")
            outputs.append(connection)

        else:
            data = s.recv(1024)

            if data:
                log.debug(str("Received %s" % data))


                # Process Data
                # Respond with approiate message

    for s in writable:
        try:
            next_msg = message_queue[s].popleft()

        except IndexError:
            log.info("Bye Bye " + s.getpeername()[0] + "!")
            closeconn(s)

        else:
            log.debug("Sent '" + next_msg.decode() + "' to "+ s.getpeername()[0])
            s.send(next_msg)

    for s in exceptional:
        log.error(s.getpeername[0] + " disconnected with an exception")
        closeconn(s)

