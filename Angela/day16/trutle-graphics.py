from turtle import *

timmy = Turtle()
#timmy is object of the class 
# print(timmy) #<turtle.Turtle object at 0x707977b21ed0>
# print(type(timmy)) #<class 'turtle.Turtle'>
timmy.shape("turtle")
my_screen = Screen()
# timmy.color("aquamarine")
# for steps in range(100):
#     for c in ('blue', 'red', 'green'):
#         color(c)
#         forward(steps)
#         right(30)
color('red')
fillcolor('yellow')
begin_fill()
while True:
  forward(200)
  left(150)
  if(abs(pos) < 1):
    break
end_fill()
        
my_screen.exitonclick()
