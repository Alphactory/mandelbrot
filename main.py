import turtle
from Imaginary_number import *


def diverges(x, y, iterations, divergence_heuristic):
    # z_n+1 = z_n^2 + C
    #   where z_0 = C
    C = ImaginaryNumber(x, y)
    Z_n = C
    for i in range(0, iterations):
        Z_np1 = add_imag(multiply_imag(Z_n, Z_n), C)
        Z_n = Z_np1
        if Z_n.real > divergence_heuristic or Z_n.imag > divergence_heuristic:
            break
        # print(f"{Z_n.real} + {Z_n.imag}i")

    if abs(Z_n.real) < divergence_heuristic and abs(Z_n.imag) < divergence_heuristic:
        # print("converges")
        return 0, 0, 0
    else:
        # print("diverges")
        #print(divergence_heuristic / abs(Z_n.real))
        return .2, 0, divergence_heuristic/(abs(Z_n.real)+abs(Z_n.imag))
        #return "white"


def draw_square(size=10):
    turtle.begin_fill()
    for i in range(0, 4):
        turtle.forward(size)
        turtle.left(90)
    turtle.end_fill()


def draw_fractal(iterations, divergence_heuristic):
    print(turtle.screensize())
    xrange, yrange = turtle.screensize()
    zoom = 50
    screen_size_mul=2

    for x in range(-xrange, xrange):
        for y in range(-yrange, yrange):
            print(x, y)
            turtle.penup()
            newx = x / zoom
            newy = y / zoom
            turtle.goto(x*screen_size_mul, y*screen_size_mul)
            turtle.pendown()
            turtle.color(diverges(newx, newy, iterations, divergence_heuristic))
            draw_square(screen_size_mul)


def main():
    turtle.screensize(200, 200)
    turtle.speed(0)
    turtle.tracer(False)
    draw_fractal(25, 1)
    turtle.update()
    turtle.done()
    input("done")


main()
