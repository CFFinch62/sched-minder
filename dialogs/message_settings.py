from PyQt6.QtWidgets import (QDialog, QVBoxLayout, QFormLayout, 
                            QLineEdit, QPushButton, QLabel, QHBoxLayout)
from constants import DEFAULT_MESSAGES

class MessageSettingsDialog(QDialog):
    def __init__(self, settings_manager, parent=None):
        super().__init__(parent)
        self.settings_manager = settings_manager
        self.setWindowTitle("Schedule Messages")
        self.setup_ui()
        
    def setup_ui(self):
        layout = QVBoxLayout(self)
        form_layout = QFormLayout()
        
        self.message_inputs = {}
        current_messages = self.settings_manager.get_schedule_messages()
        
        # Create input fields for each message type with updated labels
        message_labels = {
            'before_schedule': 'Before Schedule',
            'during_event': 'During Event',      # Changed from during_period
            'between_events': 'Between Events',  # Changed from between_periods
            'after_schedule': 'After Schedule'
        }
        
        for key, default in DEFAULT_MESSAGES.items():
            label = QLabel(message_labels[key])
            input_field = QLineEdit(current_messages.get(key, default))
            self.message_inputs[key] = input_field
            form_layout.addRow(label, input_field)
            
            # Add helper text with updated placeholders
            if key == 'during_event':  # Changed from during_period
                helper = QLabel("Use {event_name} for event name")
                form_layout.addRow('', helper)
            elif key == 'between_events':  # Changed from between_periods
                helper = QLabel("Use {prev_event} and {next_event}")
                form_layout.addRow('', helper)
        
        layout.addLayout(form_layout)
        
        # Buttons
        button_layout = QHBoxLayout()
        save_btn = QPushButton("Save")
        cancel_btn = QPushButton("Cancel")
        reset_btn = QPushButton("Reset to Default")
        
        save_btn.clicked.connect(self.save_messages)
        cancel_btn.clicked.connect(self.reject)
        reset_btn.clicked.connect(self.reset_to_default)
        
        button_layout.addWidget(reset_btn)
        button_layout.addStretch()
        button_layout.addWidget(save_btn)
        button_layout.addWidget(cancel_btn)
        
        layout.addLayout(button_layout)
        
    def save_messages(self):
        messages = {key: input_field.text() 
                   for key, input_field in self.message_inputs.items()}
        self.settings_manager.save_schedule_messages(messages)
        self.accept()
        
    def reset_to_default(self):
        for key, input_field in self.message_inputs.items():
            input_field.setText(DEFAULT_MESSAGES[key]) 