import turtle
turtle.shape("turtle")
turtle.speed(5)
angle = int(input("введите количество углов"))
size = 200
turtle.color("green")
if angle != 5:
  print("углов должно быть пять")
elif angle == 5:
    for i in range(5):
        turtle.forward(size)
        turtle.left(72)