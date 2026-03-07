Hello! Welcome to demofile.txt
This file is for testing purposes.
Good Luck!

ex1
f = open("demofile.txt", "r")

print(f.read())

#Result: 
#Hello! Welcome to demofile.txt
#This file is for testing purposes.
#Good Luck!

ex2
f = open("D:\\myfiles\welcome.txt", "r")

print(f.read())

#Result:
#Welcome to this text file!
#This file is located in a folder named "myfiles", on the D drive.
#Good Luck!

ex3
with open("demofile.txt", "r") as f:
  print(f.read())

ex4
f = open("demofile.txt", "r")

print(f.readline())

f.close()

#Result:
#Hello! Welcome to demofile.txt

ex5
with open("demofile.txt", "r") as f:
  print(f.read(5))

#Result:
#Hello

ex6
with open("demofile.txt") as f:
  print(f.readline())

#Result:
#Hello! Welcome to demofile.txt

ex7
with open("demofile.txt") as f:
  print(f.readline())
  print(f.readline())

#Result:
#Hello! Welcome to demofile.txt

#This file is for testing purposes.

ex8
with open("demofile.txt") as f:
  for x in f:
    print(x)

#Result:
#Hello! Welcome to demofile.txt

#This file is for testing purposes.

#Good Luck!
