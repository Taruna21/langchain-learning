import json
import sys

nb_path = r"c:\Users\HP\Langchain-learning\updateslangchain\1-langchainintro.ipynb"
with open(nb_path, "r", encoding="utf-8") as f:
    nb = json.load(f)

# We will execute each code cell in a shared global dictionary to simulate Jupyter
globals_dict = {}

for idx, cell in enumerate(nb.get("cells", [])):
    if cell.get("cell_type") == "code":
        print(f"Executing Cell {idx}...")
        source_code = "".join(cell.get("source", []))
        try:
            exec(source_code, globals_dict)
        except Exception as e:
            print(f"Error executing Cell {idx}: {type(e).__name__}: {e}", file=sys.stderr)
            sys.exit(1)

print("All cells executed successfully!")
