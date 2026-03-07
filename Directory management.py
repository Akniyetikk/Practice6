import os

print("Location", os.getcwd())


os.makedirs("projects/python/scripts", exist_ok=True)


os.chdir("projects/python")
print("Changed location:", os.getcwd())


items = os.listdir(".")
print("Consist of", items)


os.rmdir("scripts")

