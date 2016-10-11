import turtle

def draw_c(leng):
    ram = turtle.Turtle()
    ram.shape()
    ram.speed(0)
    ram.color('blue')
    ram.forward(leng/2)
    ram.backward(leng/2)
    ram.left(90)
    ram.forward(leng)
    ram.right(90)
    ram.forward(leng/2)
    
    
    #End of function

def draw_k(leng):
    ram = turtle.Turtle()
    ram.penup()
    ram.setx(leng+10)
    ram.shape()
    ram.speed(0)
    ram.color('red')
    ram.pendown()
    ram.left(90)
    ram.forward(leng)
    ram.penup()
    ram.backward(leng/2)
    ram.right(45)
    ram.pendown()
    ram.forward(leng*2/3)
    ram.backward(leng*2/3)
    ram.right(90)
    ram.forward(leng*2/3)
        
    #End of function

def draw_j(leng):
    ram = turtle.Turtle()
    ram.penup()
    ram.setx(2*leng+20)
    ram.shape()
    ram.speed(0)
    ram.color('red')
    ram.pendown()
    ram.forward(leng/2)
    ram.left(90)
    ram.forward(leng)
    ram.left(90)
    ram.backward(leng/2)
    ram.forward(leng)
    #End of function
    
window = turtle.Screen()
window.bgcolor("#a8bdaa")
draw_c(75)
draw_k(75)
draw_j(75)
window.exitonclick()