promt=input("enter promt:")

match promt:
    case "start":
        print("starting...")
    case "stop":
        print("stoping...")
    case "restarting":
        print("restarting...")
    case _:
        print("invalied")
        