"""
Write a program that takes a traffic light color as input and prints the corresponding 
action using match–case.

"""

traffic_light=input("enter tarffic light:")

match traffic_light:
    case "red":
        print("stop")
    case "green":
        print("go")
    case "yellow":
        print("wait")
    case _:
        print("invalied")

