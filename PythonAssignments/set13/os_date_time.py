import os
from datetime import datetime

folder = "."  # Current folder

print("File\t\t\tSize\tLast Modified")
print("-" * 50)

count = 0

for file in os.listdir(folder):
    if file.endswith(".py"):
        size = os.path.getsize(file)

        if size >= 1024:
            size = f"{round(size/1024,1)} KB"
        else:
            size = f"{size} B"

        modified = os.path.getmtime(file)
        modified = datetime.fromtimestamp(modified)
        modified = modified.strftime("%d-%m-%Y %H:%M")

        print(f"{file}\t{size}\t{modified}")
        count += 1

print("-" * 50)
print("Total:", count, "files")