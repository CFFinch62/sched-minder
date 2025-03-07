from PyQt6.QtWidgets import (QDialog, QVBoxLayout, QLabel, 
                           QHBoxLayout, QWidget)
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt
import os
from constants import ASSETS_DIR
from utils.about_manager import AboutManager

class AboutDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.about_manager = AboutManager()
        self.about_info = self.about_manager.about_info
        self.setWindowTitle(f"About {self.about_info['app_name']}")
        self.setup_ui()
        
    def setup_ui(self):
        layout = QVBoxLayout(self)
        layout.setSpacing(10)
        layout.setContentsMargins(20, 20, 20, 20)
        
        # Image and text container
        container = QWidget()
        container_layout = QHBoxLayout(container)
        
        # Load and display image
        image_path = os.path.join(ASSETS_DIR, 'images', self.about_info['logo_file'])
        image_label = QLabel()
        pixmap = QPixmap(image_path)
        image_label.setPixmap(pixmap.scaled(100, 100, Qt.AspectRatioMode.KeepAspectRatio))
        container_layout.addWidget(image_label)
        
        # Text information
        text_layout = QVBoxLayout()
        
        app_name = QLabel(self.about_info['app_name'])
        app_name.setStyleSheet("font-size: 16pt; font-weight: bold;")
        
        version = QLabel(f"Version {self.about_info['version']}")
        company = QLabel(self.about_info['company'])
        author = QLabel(self.about_info['author'])
        website = QLabel(f'<a href="http://{self.about_info["website"]}">{self.about_info["website"]}</a>')
        website.setOpenExternalLinks(True)
        
        text_layout.addWidget(app_name)
        text_layout.addWidget(version)
        text_layout.addWidget(company)
        text_layout.addWidget(author)
        text_layout.addWidget(website)
        
        container_layout.addLayout(text_layout)
        layout.addWidget(container)
        
        self.setFixedSize(self.sizeHint()) 