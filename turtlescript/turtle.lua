--
-- Created by IntelliJ IDEA.
-- User: liam
-- Date: 12/15/15
-- Time: 3:18 PM
--
headers = {
    ["User-Agent"] = "Turtle"
}

h = {}
dat = {}

while true do
    h = http.get("localhost:54363", headers)
    dat = textutils.unserialize(h.readAll())
    if dat.api == 'move' then
        if dat.c == 0 then turtle.forward()
        elseif dat.c == 1 then turtle.back()
        elseif dat.c == 2 then turtle.up()
        elseif dat.c == 3 then turtle.down()
        elseif dat.c == 4 then turtle.turnLeft()
        elseif dat.c == 5 then turtle.turnRight()
        else print("Incorrect Command")
        end
    end
end