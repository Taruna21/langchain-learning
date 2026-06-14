import json

nb_path = r"c:\Users\HP\Langchain-learning\updateslangchain\1-langchainintro.ipynb"
with open(nb_path, "r", encoding="utf-8") as f:
    nb = json.load(f)

for cell_idx, cell in enumerate(nb.get("cells", [])):
    print(f"=== Cell {cell_idx} ({cell.get('cell_type')}) ===")
    source = cell.get("source", [])
    for line_idx, line in enumerate(source):
        print(f"{line_idx + 1}: {line}", end="")
    print("\n")
