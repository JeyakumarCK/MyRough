import turtle

def draw_square(jim, rtangle): 
    i=0
    while i < 4 :
        jim.fd(100)
        jim.rt(90)
        i += 1
    jim.right(rtangle)
    
def draw_circle():
    angie = turtle.Turtle()
    angie.shape("circle")
    angie.color("red")
    angie.circle(60)
        
def draw_triangle1(ram, rpt, leng):
    print rpt, leng
    oleng = leng
    for x in range(0,3):
        for a in range(1, rpt):
            #a += 1
            print "rpt", a
            leng = leng/a
            for i in range(0,3):
                ram.forward(leng)
                ram.left(120)
        leng = oleng
        ram.forward(oleng)
        ram.left(120)

def draw_triangle(ram, leng):
    for i in range(0,3):
        ram.forward(leng)
        ram.left(120)

def draw_cent_inv_triangle(ram, leng):
    #angl = 60
    #for i in range(1,4):
    ram.color("blue", "green")
    ram.forward(leng)
    ram.left(60)
    ram.forward(leng)
    ram.left(120)
    ram.forward(leng)
    ram.left(120)
    ram.forward(leng)
    ram.left(60)
    ram.backward(leng)

def draw_one_set_nofill_triangles(ram, leng):
    draw_triangle(ram, leng)
    leng = leng/2
    draw_cent_inv_triangle(ram, leng)

def draw_one_set_triangles(ram, leng):
    draw_triangle(ram, leng)
    leng = leng/2
    draw_cent_inv_triangle(ram, leng)

def draw_three_set_triangles(ram, leng):
    draw_one_set_triangles(ram, leng)
    leng = leng/2
    draw_one_set_triangles(ram, leng)
    leng = leng/2
    draw_one_set_triangles(ram, leng)

def draw_five_set_triangles(ram, leng):
    draw_one_set_triangles(ram, leng)
    leng = leng/2
    draw_one_set_triangles(ram, leng)
    leng = leng/2
    ram.color("blue", "white")
    ram.begin_fill()
    draw_one_set_triangles(ram, leng)
    ram.forward(leng)
    ram.color("blue", "white")
    draw_one_set_triangles(ram, leng)
    ram.backward(leng)
    ram.left(60)
    ram.forward(leng)
    ram.right(60)
    ram.color("blue", "white")
    draw_one_set_triangles(ram, leng)
    ram.left(60)
    ram.backward(leng)
    ram.right(60)
    ram.end_fill()
    
def draw_triangles(ram, leng):
    oleng = leng
    for i in range(0,3):
        draw_five_set_triangles(ram, oleng)
        ram.forward(oleng)
        ram.left(120)

window = turtle.Screen()
window.bgcolor("#a8bddd")
jim = turtle.Turtle()
jim.shape("classic")
jim.speed(0)
jim.color('black')
#for i in range(1,37):
#    draw_square(jim, 10)
#draw_circle()
draw_triangles(jim, 200)
window.exitonclick()