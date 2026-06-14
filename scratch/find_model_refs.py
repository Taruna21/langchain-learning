import json

nb_path = r"c:\Users\HP\Langchain-learning\updateslangchain\1-langchainintro.ipynb"
with open(nb_path, "r", encoding="utf-8") as f:
    nb = json.load(f)

for cell_idx, cell in enumerate(nb.get("cells", [])):
    if cell.get("cell_type") == "code":
        source = cell.get("source", [])
        for line_idx, line in enumerate(source):
            if "model" in line:
                print(f"Cell {cell_idx}, Line {line_idx + 1}: {line.strip()}")
