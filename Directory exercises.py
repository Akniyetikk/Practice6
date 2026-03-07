import os
import shutil
from pathlib import Path

root = Path("my_project")
sub = root / "scripts" / "python"
sub.mkdir(parents=True, exist_ok=True)

(sub / "main.py").touch()
(sub / "utils.py").touch()
(sub / "notes.txt").touch()

print(f"Содержимое {sub}: {os.listdir(sub)}")

py_files = list(sub.glob("*.py"))
print(f"Найдены Python файлы: {[f.name for f in py_files]}")

target_dir = root / "important"
target_dir.mkdir(exist_ok=True)
shutil.move(sub / "main.py", target_dir / "main.py")
print(f"--- Файл main.py перемещен в {target_dir}")
