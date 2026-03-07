import os

print("Я тут:", os.getcwd())


os.makedirs("projects/python/scripts", exist_ok=True)


os.chdir("projects/python")
print("Теперь я тут:", os.getcwd())


items = os.listdir(".")
print("Содержимое:", items)


os.rmdir("scripts")
