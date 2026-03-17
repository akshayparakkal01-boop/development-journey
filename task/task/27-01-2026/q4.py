triangle = input("enter value: ")

match triangle:
    case "e":
          print("Equilateral")
    case "i":
          print("Isosceles")
    case "s":
          print("Scalene")
    case _: 
          print("invalid ...")