# import another_module
# print(another_module.another_variable)

# import turtle
# from turtle import Turtle,Screen
#
# # timmy=turtle.Turtle()
# timmy = Turtle()
# print(timmy)
# timmy.shape("turtle")
# timmy.color("coral")
# timmy.fd(100)
#
# my_screen=Screen()
# print(my_screen.canvheight,"x",my_screen.canvheight)
# my_screen.exitonclick()

from prettytable import PrettyTable

table = PrettyTable()
table.add_column("Pokemon Name", ["Pikachu","Siquirtle","Charmande"])
table.add_column("Type", ["æElectric","Water","Fire"])

table.align = "l"







print((table))
