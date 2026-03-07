import shutil
from pathlib import Path

file = Path("test_data.txt")
file.write_text("Line 1: Initial data\n", encoding="utf-8")
print("-File is created.")

with file.open("a", encoding="utf-8") as f:
    f.write("Line 2: Added data\n")
print("-Data is added.")

content = file.read_text(encoding="utf-8")
print(f"-Content:\n{content}")

backup_file = Path("test_data_backup.txt")
shutil.copy(file, backup_file)
print(f"-Backup file: {backup_file.name}")

if backup_file.exists():
    backup_file.unlink()
    print("-Backup was deleted")
