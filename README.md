# TurtleNET
A project aimed to add functionity to ComputerCraft turtles with an external http control server.

## The plan

![Plan Graphic](http://i.imgur.com/q52iOza.png)

[An explanation of the current branch can  be found here](branch.md)

## CC API's <http://www.computercraft.info/wiki/Category:APIs>


## Native Turtle program

Commmand | Description
---------|--------------
craft  | craft item from inventory
equip  | trys to equip a tool
go     | Move to location
refuel | Refeul with items in inventory
turn   | Rotate turtle
unequip| Unequip tool

## Turtle Commands
*t is subsitited for turtle*

Function Call       | Description
--------------------|-------------
`t.craft(number)`     | Craft using any items in turtles inventory
`t.direction`         | Move in that direction
`t.turnDirection`     | Move in that direction
`t.select(slot)`      | Select item in inventory at that slot
`t.getItemCount(slot)`| Find how many items in that stack
`t.getItemSpace(slot)`| Gets how many items left to fill that slot
`t.getItemDetail`     | Returns ID string, count, damage
`t.equipSide()`       | Attempts to equip item at current slot
`t.attackDirection`   | Attack!
`t.digDirection`      | Dig.
`t.placeDirection([string])`| Place block in front, optional engrave text on signs
`t.detectdirection`   | Detects if a block is in front of turtle
`t.inspect()`         | Returns ID string and metadata of the block in front of the turtle
`t.drop([number])`    | Drops amount of items in selected slot
`t.suck([number])`    | Pick Up items off ground
`t.refeul([number])`  | Refeults the turtle with stuff inside it
`t.transferTo(slot1, [number]` | Transfer from selected slot to `slot1`


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
