# Schedule editor dialog
from PyQt6.QtWidgets import (QDialog, QVBoxLayout, QHBoxLayout, QPushButton, 
                            QTableWidget, QTableWidgetItem, QComboBox, QHeaderView, QMessageBox, QLineEdit, QLabel)
from PyQt6.QtCore import Qt
from datetime import datetime

class ScheduleEditorDialog(QDialog):
    """Dialog for editing schedule events and times"""
    def __init__(self, schedules, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Schedule Editor")
        self.schedules = schedules.copy()  # Work with a copy
        
        # Set minimum and initial size (75% of 800x600)
        self.setMinimumSize(600, 450)  # Width: 600px, Height: 450px
        
        self.setup_ui()
        
    def setup_ui(self):
        layout = QVBoxLayout(self)
        
        # Schedule selector and name editor
        selector_layout = QHBoxLayout()
        
        self.schedule_combo = QComboBox()
        # Use internal schedule keys for combo box
        self.schedule_combo.addItems(['schedule_1', 'schedule_2', 'schedule_3'])
        self.schedule_combo.currentTextChanged.connect(self.schedule_selected)
        
        self.name_edit = QLineEdit()
        self.name_edit.setPlaceholderText("Schedule Name")
        self.name_edit.textChanged.connect(self.schedule_name_changed)
        
        selector_layout.addWidget(QLabel("Schedule:"))
        selector_layout.addWidget(self.schedule_combo)
        selector_layout.addWidget(QLabel("Name:"))
        selector_layout.addWidget(self.name_edit)
        
        layout.addLayout(selector_layout)
        
        # Event table
        self.event_table = QTableWidget()
        self.event_table.setColumnCount(3)
        self.event_table.setHorizontalHeaderLabels(["Event", "Start Time", "End Time"])
        header = self.event_table.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        
        # Connect cell change handler
        self.event_table.cellChanged.connect(self.handle_cell_change)
        
        layout.addWidget(self.event_table)
        
        # Add buttons
        button_layout = QHBoxLayout()
        add_btn = QPushButton("Add Event")
        remove_btn = QPushButton("Remove Event")
        ok_btn = QPushButton("OK")
        cancel_btn = QPushButton("Cancel")
        
        add_btn.clicked.connect(self.add_event)
        remove_btn.clicked.connect(self.delete_event)
        ok_btn.clicked.connect(self.accept)
        cancel_btn.clicked.connect(self.reject)
        
        button_layout.addWidget(add_btn)
        button_layout.addWidget(remove_btn)
        button_layout.addStretch()
        button_layout.addWidget(ok_btn)
        button_layout.addWidget(cancel_btn)
        
        layout.addLayout(button_layout)
        
        # Load initial schedule
        self.load_schedule()
        
    def load_schedule(self):
        schedule_key = self.schedule_combo.currentText()
        schedule = self.schedules[schedule_key]
        
        # Update name
        self.name_edit.setText(schedule.get('name', ''))
        
        # Sort and load events
        events = schedule.get('events', [])
        sorted_events = self.sort_events(events)
        
        # Temporarily disconnect cell change handler
        self.event_table.cellChanged.disconnect(self.handle_cell_change)
        
        # Clear and populate table
        self.event_table.setRowCount(len(sorted_events))
        for row, event in enumerate(sorted_events):
            self.event_table.setItem(row, 0, QTableWidgetItem(event.get('name', '')))
            self.event_table.setItem(row, 1, QTableWidgetItem(event.get('start', '')))
            self.event_table.setItem(row, 2, QTableWidgetItem(event.get('end', '')))
            
        # Reconnect cell change handler
        self.event_table.cellChanged.connect(self.handle_cell_change)
        
    def sort_events(self, events):
        """Sort events by start time"""
        return sorted(events, key=lambda x: x.get('start', '') or '00:00')
        
    def schedule_selected(self):
        self.load_schedule()
        
    def schedule_name_changed(self, name):
        schedule_key = self.schedule_combo.currentText()
        self.schedules[schedule_key]['name'] = name
        
    def add_event(self):
        """Add new event to schedule"""
        row = self.event_table.rowCount()
        self.event_table.insertRow(row)
        for col in range(3):
            self.event_table.setItem(row, col, QTableWidgetItem(''))
            
    def delete_event(self):
        """Delete selected event"""
        current_row = self.event_table.currentRow()
        if current_row >= 0:
            self.event_table.removeRow(current_row)
            
    def handle_cell_change(self, row, column):
        self.update_schedule_data()
        
    def update_schedule_data(self):
        schedule_key = self.schedule_combo.currentText()
        events = []
        
        for row in range(self.event_table.rowCount()):
            name = self.event_table.item(row, 0)
            start = self.event_table.item(row, 1)
            end = self.event_table.item(row, 2)
            
            if name and start and end:
                events.append({
                    'name': name.text().strip(),
                    'start': start.text().strip(),
                    'end': end.text().strip()
                })
                
        self.schedules[schedule_key]['events'] = events
        
    def get_updated_schedules(self):
        return self.schedules 