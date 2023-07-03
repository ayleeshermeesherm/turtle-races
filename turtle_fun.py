import turtle
window = turtle.Screen()
window.title("Turtle Circle")

bob = turtle.Turtle()
bob.shape("turtle")
bob.color('green')
bob.pensize(3)
bob.speed(8)

bob.circle(50)

window.exitonclick()

print("updating for git experiment")