# Color settings dialog
from PyQt6.QtWidgets import (QDialog, QVBoxLayout, QHBoxLayout, QPushButton, 
                            QLabel, QWidget, QColorDialog)
from PyQt6.QtGui import QColor
from constants import DEFAULT_COLORS

class ColorSettingsDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.parent = parent
        self.setup_ui()
        
    def setup_ui(self):
        self.setWindowTitle("Color Settings")
        self.setMinimumWidth(400)
        layout = QVBoxLayout(self)
        
        # Create color selection buttons
        self.create_color_button("Window Background", "window_bg_color", layout)
        self.create_color_button("Window Text", "window_text_color", layout)
        self.create_color_button("Message Background", "message_bg_color", layout)
        self.create_color_button("Message Text", "message_text_color", layout)
        
        # Buttons
        button_layout = QHBoxLayout()
        save_btn = QPushButton("Save")
        cancel_btn = QPushButton("Cancel")
        reset_btn = QPushButton("Reset to Default")
        
        save_btn.clicked.connect(self.accept)
        cancel_btn.clicked.connect(self.reject)
        reset_btn.clicked.connect(self.reset_colors)
        
        button_layout.addWidget(reset_btn)
        button_layout.addStretch()
        button_layout.addWidget(save_btn)
        button_layout.addWidget(cancel_btn)
        
        layout.addLayout(button_layout)
        
        # Apply dark theme to dialog
        self.setStyleSheet("""
            QDialog {
                background-color: #000000;
                color: white;
            }
            QPushButton {
                background-color: #000066;
                color: white;
                border: 1px solid #0000cc;
                padding: 5px 10px;
                min-width: 80px;
            }
            QPushButton:hover {
                background-color: #000099;
            }
        """)
    
    def create_color_button(self, label_text, setting_name, layout):
        container = QWidget()
        h_layout = QHBoxLayout(container)
        
        label = QLabel(label_text)
        button = QPushButton()
        button.setFixedSize(40, 20)
        
        # Get color from settings or use default
        color = QColor(self.parent.settings_manager.get_colors()[setting_name])
        button.setStyleSheet(f"background-color: {color.name()};")
        
        # Store the setting name with the button
        button.setting_name = setting_name
        button.clicked.connect(lambda: self.choose_color(button))
        
        h_layout.addWidget(label)
        h_layout.addWidget(button)
        layout.addWidget(container)
    
    def choose_color(self, button):
        current_color = QColor(button.palette().button().color())
        color = QColorDialog.getColor(current_color, self)
        
        if color.isValid():
            button.setStyleSheet(f"background-color: {color.name()};")
            # Store the color in parent's current colors
            self.parent.settings_manager.save_colors({button.setting_name: color.name()})
    
    def reset_colors(self):
        from constants import DEFAULT_COLORS
        for child in self.findChildren(QPushButton):
            if hasattr(child, 'setting_name'):
                default_color = DEFAULT_COLORS[child.setting_name]
                child.setStyleSheet(f"background-color: {default_color};")
                self.parent.settings_manager.save_colors({child.setting_name: default_color}) 