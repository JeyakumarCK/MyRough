import turtle

def draw_diamond(ram, leng):
    for i in range (0, 4):
        ram.forward(leng)
        if i % 2 == 1 :
            ram.right(150)
        else:
            ram.right(30)
    #End of draw_diamond
    
def draw_flower(ram, leng):
    for i in range (0, 45):
        draw_diamond(ram, leng)
        ram.right(8)
    ram.right(90)
    ram.forward(3*leng)
    #End of draw_flower
    
window = turtle.Screen()
window.bgcolor("#a8bddd")
jim = turtle.Turtle()
jim.shape("circle")
jim.speed(0)
jim.color('brown')
draw_flower(jim, 75)
window.exitonclick()