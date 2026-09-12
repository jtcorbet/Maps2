import os
from pathlib import Path

# --- Window configuration parameters ---
WINDOW_TITLE = "Modern Maps2 Application"
DEFAULT_WIDTH = 1200
DEFAULT_HEIGHT = 800
MIN_WIDTH = 800
MIN_HEIGHT = 600

# --- CustomTkinter look & feel ---
APPEARANCE_MODE = "System"  # Options: "System", "Dark", "Light"
COLOR_THEME = "blue"        # Options: "blue", "green", "dark-blue"

# --- Project path mapping ---
ROOT_DIR = Path(__file__).resolve().parent
ASSETS_DIR = ROOT_DIR / "assets"
BACKUP_DIR = ROOT_DIR / "src.bak"

