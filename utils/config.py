from pathlib import Path
import json


CONFIG_PATH = Path(__file__).resolve().parents[1] / "configs" / "config.json"


def load_config():
    """Load and return the project configuration as a dict.

    Caches are intentionally omitted to keep it simple and predictable in tests.
    """
    with open(CONFIG_PATH, "r") as f:
        return json.load(f)


def get(key, default=None):
    cfg = load_config()
    return cfg.get(key, default)
