import pandas as pd
import numpy as np
from pathlib import Path

def find_input_file(filename):
    """Busca el archivo en directorios estándar."""
    roots = [Path("../data/raw"), Path("/kaggle/input"), Path("/mnt/data"), Path.cwd()]
    for root in roots:
        if not root.exists():
            continue
        exact = root / filename
        if exact.exists():
            return exact
        matches = list(root.rglob(filename))
        if matches:
            return matches[0]
    raise FileNotFoundError(f"No se encontró '{filename}'.")
