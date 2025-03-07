from PyQt6.QtWidgets import (QDialog, QVBoxLayout, QTextBrowser, 
                            QPushButton, QHBoxLayout)
from PyQt6.QtCore import Qt

class UserGuideDialog(QDialog):
    def __init__(self, content, parent=None):
        super().__init__(parent)
        self.setWindowTitle("User Guide")
        self.setModal(True)
        self.resize(800, 600)  # Larger size for better readability
        
        # Create layout
        layout = QVBoxLayout(self)
        
        # Create text browser for content
        self.text_browser = QTextBrowser()
        self.text_browser.setOpenExternalLinks(True)
        self.text_browser.setMarkdown(content)
        layout.addWidget(self.text_browser)
        
        # Add close button
        button_layout = QHBoxLayout()
        close_button = QPushButton("Close")
        close_button.clicked.connect(self.accept)
        button_layout.addStretch()
        button_layout.addWidget(close_button)
        layout.addLayout(button_layout)
        
        # Style
        self.setStyleSheet("""
            QDialog {
                background-color: white;
            }
            QTextBrowser {
                font-size: 12pt;
                border: none;
            }
            QPushButton {
                padding: 6px 12px;
                min-width: 80px;
            }
        """) 