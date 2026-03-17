"""
Write a program using match–case to check whether an entered shape is:
•⁠  ⁠"c" → Circle
•⁠  ⁠"r" → Rectangle
•⁠  ⁠"s" → Square
"""
name=input("enter name:")
match name:
    case "c":
        print("circle")
    case "r":
        print("rectangle")
    case "s":
        print("square")
    case _:
        print("invalied")