# Notes on exercises from 'Think Python'




# chapter 4 turtle

import turtle

bob = turtle.Turtle()

def square(t):
    for i in range(4):
        t.fd(100)
        t.lt(90)

square(bob)
turtle.mainloop()


# exercise 3-3

def do_twice(f):
    f()
    f()


def do_four(f):
    do_twice(f)
    do_twice(f)


def print_beam():
    print('+ - - - -', end = ' ')


def print_post():
    print('|        ', end = ' ')


def print_beams():
    do_twice(print_beam)
    print('+')


def print_posts():
    do_twice(print_post)
    print('|')


def print_row():
    print_beams()
    do_four(print_posts)


def print_grid():
    do_twice(print_row)
    print_beams()


print_grid()
