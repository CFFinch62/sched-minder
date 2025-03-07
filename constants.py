import os
from PyQt6.QtCore import QSize

# Base paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ASSETS_DIR = os.path.join(BASE_DIR, 'assets')
DATA_DIR = os.path.join(BASE_DIR, 'data')

# Asset paths
ICON_PATH = os.path.join(ASSETS_DIR, 'icons', 'clock.png')
TEST_FILES_DIR = os.path.join(ASSETS_DIR, 'test_files')
SCHEDULES_FILE = os.path.join(DATA_DIR, 'schedules.json')

# Add to existing paths
ABOUT_FILE = os.path.join(DATA_DIR, 'about.json')

# Application-wide constants, default values, and configuration
DEFAULT_COLORS = {
    "window_bg_color": "#000000",
    "window_text_color": "#FFFFFF",
    "message_bg_color": "#000066",
    "message_text_color": "#FFFFFF"
}

# Window sizes
WINDOW_SIZES = {
    'small': QSize(305, 230),
    'medium': QSize(445, 355),
    'large': QSize(675, 555),
    'test_mode': QSize(385, 320)
}

DEFAULT_WINDOW_SIZE = WINDOW_SIZES['small']
DEFAULT_TEST_SIZE = WINDOW_SIZES['test_mode']

# Application settings
APP_ORGANIZATION = 'Fragillidae Software'
APP_NAME = 'Schedule Minder'
DEFAULT_ADMIN_PASSWORD = 'chucksoft'

# Styles
COMMON_STYLES = """
    QMainWindow {
        background-color: %(window_bg_color)s;
        color: %(window_text_color)s;
    }
    QLabel {
        color: %(window_text_color)s;
    }
    QLabel#regular_label, QLabel#delay_label, QLabel#homeroom_label {
        background-color: %(message_bg_color)s;
        color: %(message_text_color)s;
        border: 1px solid #0000cc;
        border-radius: 4px;
        padding: 2px 5px;
        qproperty-alignment: 'AlignLeft | AlignVCenter';
    }
"""

# Schedule types
REGULAR_SCHEDULE = "Regular Schedule"
DELAY_SCHEDULE = "Two Hour Delay"
HOMEROOM_SCHEDULE = "Homeroom Schedule"

# Add to existing constants
DEFAULT_MESSAGES = {
    "before_schedule": "Before Schedule",
    "during_event": "{event_name}",
    "between_events": "{prev_event} → {next_event}",
    "after_schedule": "After Schedule"
}

# Update Intervals
# Event check: Every 60 seconds
# UI refresh: Every 1000ms
# Test mode: User-defined 