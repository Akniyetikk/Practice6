#"a" - Append - will append to the end of the file
#"w" - Write - will overwrite any existing content

ex1
with open("demofile.txt", "a") as f:
  f.write("Now the file has more content!")

#open and read the file after the appending:
with open("demofile.txt") as f:
  print(f.read())

#RESULT:
Hello! Welcome to demofile.txt
This file is for testing purposes.
Good Luck!Now the file has more content!

ex2
with open("demofile.txt", "w") as f:
  f.write("Woops! I have deleted the content!")

#open and read the file after the overwriting:
with open("demofile.txt") as f:
  print(f.read())

#RESULT:
Woops! I have deleted the content!

ex3
#This will create a new file:

f = open("myfile.txt", "x")

#If the file already exist, an error will be raised.

