signal=input("enter signal:")

match signal:
    case "red":
        print("STOP")
    case "green":
        print("GO")
    case "yellow":
        print("WAIT")
    case _:
        print("invalied")
        
    
    