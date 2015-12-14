# TurtleNET
A project aimed to add functionity to ComputerCraft turtles with an external http control server.

This was added from *within* my IDE. (just checking)
## The plan

    Client
      |
      API
    (python socket)
      v
    Control Server
       ^
       |
    Intermittent
    HTTP POST/GET
    instructions
       |
    CC Turtle/Computer
       |
     Doing stuff