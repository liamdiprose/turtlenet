# TurtleNET
A project aimed to add functionity to ComputerCraft turtles with an external http control server.

This was added from *within* my IDE. (just checking)
## The plan

![Plan Graphic](http://i.imgur.com/q52iOza.png)

## CC API's <http://www.computercraft.info/wiki/Category:APIs>


## Native Turtle commands

Commmand | Description
---------|--------------
craft  | craft item from inventory
equip  | trys to equip a tool
go     | Move to location
refuel | Refeul with items in inventory
turn   | Rotate turtle
unequip| Unequip tool


## Server - Turtle Connection

Turtles have little functionality, they ask what to do, do it,
provide updates, then ask for a new job

### Sample exchange between turtle and server:
1. *turtle is created and script is run*
2. Turtle connects to server, with null id.
3. Server detects turtle is new, creates new object for turtle
and sets ID to index in list
4. Server adds update jobs to queue (location, inventory etc)
5. Turtle asks for job, but job_queue is empty, server instructs turtle to do nothing (later: go to garage)
6. Turtle continues to ask for jobs
7. Job ID is generated (from global job count), and added to job_queue
8. Turtle asks for job, server assigns job from queue
9. Turtle connects with updates (if massive moveTo fucntion). If server responds with a job override, start doing new job.
10. Turtle completes job, connects to server with complete flag and job id,
server deletes job and replys with new job, or nothing.
11. Repeat steps 6 - 10
