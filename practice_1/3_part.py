from turtle import *

def Bezie (coordinates):
    coordinate = lambda t: coordinates[1] + (1 - t)**2 * (coordinates[0] - coordinates[1]) + t**2 * (coordinates[2] - coordinates[1])
    point = 0
    while point <= 1:
        position = coordinate(point)
        setheading(towards(position))
        goto(position)
        point += 0.1


def DrawSymbol(x, y, palett):
    # Main body
    color("black", "#8b65d2")
    fillcolor(palett)
    pensize(3)
    penup()
    goto(x, y+10)
    pendown()
    begin_fill()
    Bezie([Vec2D(x, y+10), Vec2D(x-120, y-60), Vec2D(x+5, y+70)])
    setpos(x, y+45)
    Bezie([Vec2D(x, y+45), Vec2D(x-5, y+40), Vec2D(x+70, y+70)])
    Bezie([Vec2D(x+70, y+70), Vec2D(x+90, y+75), Vec2D(x+85, y+60)])
    Bezie([Vec2D(x+85, y+60), Vec2D(x+70, y), Vec2D(x+80, y-60)])
    Bezie([Vec2D(x+80, y-60), Vec2D(x+80, y-80), Vec2D(x+65, y-80)])
    setpos(x-80, y-100)
    Bezie([Vec2D(x-80, y-100), Vec2D(x-90, y-105), Vec2D(x-80, y-80)])
    setpos(x-70, y-50)
    setpos(x+40, y-40)
    Bezie([Vec2D(x+40, y-40), Vec2D(x+70, y+50), Vec2D(x, y+10)])
    end_fill()
    penup()
    # Up symbol 1
    goto(x+90, y+75)
    pendown()
    begin_fill()
    setpos(x+70, y+80)
    Bezie([Vec2D(x+70, y+80), Vec2D(x+75, y+100), Vec2D(x+90, y+120)])
    setpos(x+120, y+117)
    Bezie([Vec2D(x+120, y+117), Vec2D(x+110, y+112), Vec2D(x+90, y+75)])
    end_fill()
    penup()
    # Up symbol 2
    goto(x+100, y+75)
    pendown()
    begin_fill()
    Bezie([Vec2D(x+100, y+75), Vec2D(x+110, y+68), Vec2D(x+115, y+60)])
    Bezie([Vec2D(x+115, y+60), Vec2D(x+140, y+65), Vec2D(x+160, y+100)])
    setpos(x+140, y+110)
    setpos(x+100, y+75)
    end_fill()
    penup()


s = Screen()
s.bgpic('jojo.gif')
DrawSymbol(-300, 200, "#c93be7")
DrawSymbol(-300, -100, "#8b65d2")
data = 2

done()



