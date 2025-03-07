# Main entry point and app initialization
from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox
import sys
import os
import json
from constants import SCHEDULES_FILE

# Add the current directory to Python path
current_dir = os.path.dirname(os.path.abspath(__file__))
if current_dir not in sys.path:
    sys.path.append(current_dir)

from windows.schedule_window import ScheduleWindow  # Import the window class

def main():
    app = QApplication(sys.argv)
    
    # Create and show the main window
    window = ScheduleWindow(SCHEDULES_FILE)
    window.show()
    
    # Enable normal window closing behavior
    app.setQuitOnLastWindowClosed(True)
    
    sys.exit(app.exec())

if __name__ == '__main__':
    main() 