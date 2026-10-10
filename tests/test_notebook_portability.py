"""Keep the notebook runnable from the repository and notebook directories."""

import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
NOTEBOOK = ROOT / "notebooks" / "data_cleaning.ipynb"


class NotebookPaths(unittest.TestCase):
    def test_notebook_json_and_python_cells(self):
        notebook = json.loads(NOTEBOOK.read_text(encoding="utf-8"))
        sources = [
            "".join(cell["source"]) if isinstance(cell["source"], list)
            else cell["source"]
            for cell in notebook["cells"] if cell["cell_type"] == "code"
        ]
        for source in sources:
            compile(source, str(NOTEBOOK), "exec")
        combined = "\n".join(sources)
        self.assertNotIn("C:\\\\Users", combined)
        self.assertIn('df = pd.read_csv(source_path)', combined)
        self.assertIn('df.to_csv(output_path, index=False)', combined)

    def test_source_csv_exists(self):
        self.assertTrue((ROOT / "data" / "brut" / "bank-transactions.csv").is_file())


if __name__ == "__main__":
    unittest.main()
