# pathlib quick tour
# ------------------
from pathlib import Path

base = Path("project_data")
csv_path = base / "concrete" / "samples.csv"

print("path           :", csv_path)
print("exists()       :", csv_path.exists())
print("name           :", csv_path.name)
print("suffix         :", csv_path.suffix)
print("parent         :", csv_path.parent)
print("with_suffix(.json):", csv_path.with_suffix(".json"))
print("absolute       :", csv_path.resolve())
