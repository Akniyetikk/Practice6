import os

# Узнаем, где мы
print("Я тут:", os.getcwd())

# Создаем сложную структуру папок
os.makedirs("projects/python/scripts", exist_ok=True)

# Переходим внутрь
os.chdir("projects/python")
print("Теперь я тут:", os.getcwd())

# Смотрим, что внутри (сейчас там только папка 'scripts')
items = os.listdir(".")
print("Содержимое:", items)

# Попробуем удалить папку (она пустая, так что сработает)
os.rmdir("scripts")
