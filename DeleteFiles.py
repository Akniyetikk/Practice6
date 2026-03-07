ex1
import os
os.remove("demofile.txt")

ex2
import os
if os.path.exists("demofile.txt"):
  os.remove("demofile.txt")
else:
  print("The file does not exist")

ex3
import os
os.rmdir("myfolder")
#Note: You can only remove empty folders.
