from PyQt6.QtWidgets import (QDialog, QVBoxLayout, QHBoxLayout, 
                           QRadioButton, QPushButton, QButtonGroup)
from constants import WINDOW_SIZES

class WindowSizeDialog(QDialog):
    def __init__(self, current_size_name, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Window Size")
        self.current_size_name = current_size_name
        self.setup_ui()
        
    def setup_ui(self):
        layout = QVBoxLayout(self)
        
        # Create radio buttons for each size
        self.button_group = QButtonGroup(self)
        self.size_buttons = {}
        
        # Only show small, medium, and large options
        size_options = ['small', 'medium', 'large']
        for size_name in size_options:
            button = QRadioButton(size_name.capitalize())
            self.size_buttons[size_name] = button
            self.button_group.addButton(button)
            layout.addWidget(button)
            
            # Select current size
            if size_name == self.current_size_name:
                button.setChecked(True)
        
        # Add OK/Cancel buttons
        button_layout = QHBoxLayout()
        ok_button = QPushButton("OK")
        cancel_button = QPushButton("Cancel")
        
        ok_button.clicked.connect(self.accept)
        cancel_button.clicked.connect(self.reject)
        
        button_layout.addWidget(ok_button)
        button_layout.addWidget(cancel_button)
        layout.addLayout(button_layout)
        
    def get_selected_size(self):
        """Return the name of the selected size"""
        for size_name, button in self.size_buttons.items():
            if button.isChecked():
                return size_name
        return 'small'  # Default if nothing selected 