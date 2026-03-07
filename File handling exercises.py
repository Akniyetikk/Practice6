import shutil
from pathlib import Path

file = Path("test_data.txt")
file.write_text("Линия 1: Начальные данные\n", encoding="utf-8")
print("--- Файл создан.")

with file.open("a", encoding="utf-8") as f:
    f.write("Линия 2: Добавленные данные\n")
print("--- Данные добавлены.")

content = file.read_text(encoding="utf-8")
print(f"--- Содержимое файла:\n{content}")

backup_file = Path("test_data_backup.txt")
shutil.copy(file, backup_file)
print(f"--- Создана копия: {backup_file.name}")

if backup_file.exists():
    backup_file.unlink()
    print("--- Копия удалена для чистоты.")
