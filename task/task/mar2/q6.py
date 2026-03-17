"""6. Write a Python program to create a file and write 5 lines of text into it.
"""

fw = open("task/task/mar2/q6.txt","w")

names = ["akshay","srk","mohanlal","mamooty","henry"]
for n in names:
    fw.write(n+"\n")