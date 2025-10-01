"""Project-level pytest configuration.

This file ensures the repository root is on sys.path so tests can import
project packages (e.g., `pages`, `utils`) even if pytest is invoked from
an environment that doesn't add the project root automatically.
"""
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))
