"""10. Write a Python program to copy the contents of one file to another file."""

source = open("task/task/mar2/q10.txt","r")
destination = open("task/task/mar2/q10copy.txt","w")
data = source.read()
destination.write(data)