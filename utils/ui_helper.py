# Common UI creation and styling functions 

from PyQt6.QtWidgets import QLabel, QWidget, QVBoxLayout, QHBoxLayout
from PyQt6.QtCore import Qt

def create_event_display(label_text, name):
    """Create a labeled event display"""
    container = QWidget()
    layout = QVBoxLayout(container)  # Change to VBoxLayout for vertical arrangement
    layout.setSpacing(1)
    layout.setContentsMargins(1, 1, 1, 1)
    
    # Create label with schedule type
    type_label = QLabel(label_text)
    type_label.setMinimumWidth(80)
    type_label.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignVCenter)
    
    # Create event display
    event_label = QLabel()
    event_label.setObjectName(name)  # Set object name for styling
    event_label.setMinimumHeight(30)
    event_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
    
    layout.addWidget(type_label)
    layout.addWidget(event_label)
    
    return container, event_label 