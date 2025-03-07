# Main window class for schedule event tracking
from PyQt6.QtWidgets import (QWidget, QVBoxLayout, QLabel, QSystemTrayIcon, 
                            QMenu, QPushButton, QHBoxLayout, QSizePolicy,
                            QInputDialog, QLineEdit, QMessageBox, QTimeEdit,
                            QDialog, QSpinBox, QFileDialog, QWIDGETSIZE_MAX)
from PyQt6.QtCore import QTimer, Qt, QTime
from PyQt6.QtGui import QIcon, QAction
from windows.base_window import BaseWindow
from dialogs.color_settings import ColorSettingsDialog
from dialogs.schedule_editor import ScheduleEditorDialog
from utils.schedule_manager import ScheduleManager
from utils.settings_manager import SettingsManager
from utils.test_file_helper import TestFileHelper
from utils.ui_helper import create_event_display
from constants import (ICON_PATH, DEFAULT_WINDOW_SIZE, DEFAULT_TEST_SIZE, 
                    COMMON_STYLES, TEST_FILES_DIR, ASSETS_DIR, WINDOW_SIZES, APP_NAME,
                    REGULAR_SCHEDULE, DELAY_SCHEDULE, HOMEROOM_SCHEDULE)
from datetime import datetime
from PyQt6.QtWidgets import QApplication
from pathlib import Path
import os
from dialogs.window_size_dialog import WindowSizeDialog
from dialogs.about_dialog import AboutDialog
from dialogs.message_settings import MessageSettingsDialog

class ScheduleWindow(BaseWindow):
    def __init__(self, schedule_file, enable_test_mode=False):
        super().__init__()
        self.setWindowTitle(APP_NAME)
        self.setWindowFlags(Qt.WindowType.WindowStaysOnTopHint)
        
        # Initialize managers
        self.settings_manager = SettingsManager()
        self.schedule_manager = ScheduleManager(schedule_file)
        
        # Test mode initialization
        self.test_mode = False
        self.test_time = datetime.now()
        self.test_container = None
        
        # Create menu bar
        self.create_menu_bar()
        
        # Create central widget and layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        self.main_layout = QVBoxLayout(central_widget)
        
        # Set up UI
        self.setup_ui()
        
        # Set up system tray
        self.setup_system_tray()
        
        # Set up timer
        self.setup_timer()
        
        # Restore window position
        self.restore_window_position()
        
        # If test mode is enabled, set up test controls
        if enable_test_mode:
            self.setup_test_controls()
            
    def setup_ui(self):
        schedule_container = QWidget()
        schedule_layout = QVBoxLayout(schedule_container)
        schedule_layout.setSpacing(1)
        schedule_layout.setContentsMargins(1, 1, 1, 1)
        
        # Create displays using helper function
        regular_container, self.regular_label = create_event_display("Regular", "regular_label")
        delay_container, self.delay_label = create_event_display("2-Hr Delay", "delay_label")
        homeroom_container, self.homeroom_label = create_event_display("Homeroom", "homeroom_label")
        
        schedule_layout.addWidget(regular_container)
        schedule_layout.addWidget(delay_container)
        schedule_layout.addWidget(homeroom_container)
        
        self.main_layout.addWidget(schedule_container)
        
        # Set window properties
        self.setMinimumWidth(300)
        self.setMinimumHeight(200)
        self.resize(DEFAULT_WINDOW_SIZE)
        
        # Set window size from settings
        size_name = self.settings_manager.get_window_size_name()
        self.resize(WINDOW_SIZES[size_name])
        
        # Apply styles
        self.apply_styles()

    def create_menu_bar(self):
        menubar = self.menuBar()
        tools_menu = menubar.addMenu('Tools')
        
        # Add menu items in alphabetical order (except Exit which goes last):
        # 1. Change Admin Password
        change_password_action = QAction('Change Admin Password', self)
        change_password_action.triggered.connect(self.change_password)
        tools_menu.addAction(change_password_action)
        
        # 2. Change Tray Icon
        change_icon_action = QAction('Change Tray Icon', self)
        change_icon_action.triggered.connect(self.change_tray_icon)
        tools_menu.addAction(change_icon_action)
        
        # 3. Color Settings
        color_settings_action = QAction('Color Settings', self)
        color_settings_action.triggered.connect(self.show_color_settings)
        tools_menu.addAction(color_settings_action)
        
        # 4. Enable Test Mode
        self.test_mode_action = QAction('Enable Test Mode', self)
        self.test_mode_action.setCheckable(True)
        self.test_mode_action.triggered.connect(self.toggle_test_mode)
        tools_menu.addAction(self.test_mode_action)
        
        # 5. Message Settings (moved here for alphabetical order)
        message_settings_action = QAction('Message Settings', self)
        message_settings_action.triggered.connect(self.show_message_settings)
        tools_menu.addAction(message_settings_action)
        
        # 6. Schedule Editor
        edit_schedules_action = QAction('Schedule Editor', self)
        edit_schedules_action.triggered.connect(self.show_schedule_editor)
        tools_menu.addAction(edit_schedules_action)
        
        # 7. Window Size
        window_size_action = QAction('Window Size', self)
        window_size_action.triggered.connect(self.change_window_size)
        tools_menu.addAction(window_size_action)
        
        # Last: Exit (always at the end)
        exit_action = QAction('Exit', self)
        exit_action.triggered.connect(self.quit_application)
        tools_menu.addAction(exit_action)
        
        # Add Help menu
        help_menu = menubar.addMenu('Help')
        
        # Add User Guide action
        user_guide_action = QAction("User Guide", self)
        user_guide_action.triggered.connect(self.show_documentation)
        help_menu.addAction(user_guide_action)
        
        # Add About action
        about_action = QAction('About', self)
        about_action.triggered.connect(self.show_about)
        help_menu.addAction(about_action)

    def setup_system_tray(self):
        self.tray_icon = QSystemTrayIcon(self)
        icon_path = self.settings_manager.get_tray_icon_path()
        icon = QIcon(icon_path)
        self.tray_icon.setIcon(icon)
        self.tray_icon.show()
        self.tray_icon.activated.connect(self.tray_icon_activated)

    def setup_timer(self):
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_events)
        self.timer.start(60000)  # Update every minute
        self.update_events()  # Initial update

    def update_events(self):
        """Update all event displays"""
        current_time = self.get_current_time()
        regular = self.schedule_manager.get_current_event(REGULAR_SCHEDULE, current_time)
        delay = self.schedule_manager.get_current_event(DELAY_SCHEDULE, current_time)
        homeroom = self.schedule_manager.get_current_event(HOMEROOM_SCHEDULE, current_time)
        
        time_status = "TEST MODE" if self.test_mode else "LIVE"
        
        self.regular_label.setText(regular)
        self.delay_label.setText(delay)
        self.homeroom_label.setText(homeroom)
        
        self.setWindowTitle(f"{APP_NAME} - {current_time} ({time_status})")
        
        tooltip = f"Current Time: {current_time} ({time_status})\nRegular: {regular}\n2-Hour Delay: {delay}\nHomeroom: {homeroom}"
        self.tray_icon.setToolTip(tooltip)

    def get_current_time(self):
        if self.test_mode:
            return self.test_time.strftime("%H:%M")
        return datetime.now().strftime("%H:%M")

    def apply_styles(self):
        # Apply styles to the window and widgets
        colors = self.settings_manager.get_colors()
        self.setStyleSheet(COMMON_STYLES % colors)

    def setup_test_controls(self):
        if self.test_container is None:
            self.test_container = QWidget()
            test_layout = QVBoxLayout(self.test_container)
            test_layout.setSpacing(2)
            test_layout.setContentsMargins(2, 2, 2, 2)
            
            # Top row: Time control layout
            time_control = QHBoxLayout()
            time_control.setSpacing(2)
            
            self.time_edit = QTimeEdit()
            self.time_edit.setDisplayFormat("HH:mm")  # Use 24-hour format
            self.time_edit.setMinimumHeight(20)
            self.time_edit.setMinimumWidth(80)
            
            set_time_btn = QPushButton("Set")
            set_time_btn.setMinimumHeight(20)
            set_time_btn.setMinimumWidth(40)
            set_time_btn.clicked.connect(self.set_test_time)
            
            # Add stop button to top row
            stop_btn = QPushButton("Stop")
            stop_btn.setMinimumHeight(20)
            stop_btn.setMinimumWidth(40)
            stop_btn.clicked.connect(self.stop_test)
            
            time_control.addWidget(self.time_edit)
            time_control.addWidget(set_time_btn)
            time_control.addWidget(stop_btn)  # Add stop button here
            time_control.addStretch()
            
            # Bottom row: Test controls layout
            test_controls = QHBoxLayout()
            test_controls.setSpacing(2)
            
            # Add delay spinner with label
            delay_label = QLabel("Delay (seconds):")
            self.delay_spinner = QSpinBox()
            self.delay_spinner.setMinimum(1)
            self.delay_spinner.setMaximum(3600)  # Allow up to 1 hour in seconds
            self.delay_spinner.setValue(1)
            self.delay_spinner.setMinimumHeight(20)
            self.delay_spinner.setMinimumWidth(40)
            
            # Add test file load button
            load_file_btn = QPushButton("Load File")
            load_file_btn.setMinimumHeight(20)
            load_file_btn.setMinimumWidth(60)
            load_file_btn.clicked.connect(self.load_test_file)
            
            test_controls.addWidget(delay_label)
            test_controls.addWidget(self.delay_spinner)
            test_controls.addWidget(load_file_btn)
            test_controls.addStretch()
            
            test_layout.addLayout(time_control)
            test_layout.addLayout(test_controls)
            self.main_layout.addWidget(self.test_container)
            
            # Resize window to accommodate test controls
            self.resize(DEFAULT_TEST_SIZE)
            
            self.test_mode = True
            self.test_timer = None  # For automated testing
            self.set_test_time()
            self.update_events()

    def tray_icon_activated(self, reason):
        if reason in (QSystemTrayIcon.ActivationReason.Trigger, 
                     QSystemTrayIcon.ActivationReason.DoubleClick):
            if self.isVisible():
                self.hide()
            else:
                self.show()
                self.activateWindow()

    def show_schedule_editor(self):
        password, ok = QInputDialog.getText(
            self, 
            'Schedule Editor Access',
            'Enter password to access schedule editor:',
            QLineEdit.EchoMode.Password
        )
        
        if not ok:
            return
        
        if password != self.settings_manager.get_admin_password():
            QMessageBox.warning(self, 'Error', 'Incorrect password')
            return
        
        editor = ScheduleEditorDialog(self.schedule_manager.schedules, self)
        if editor.exec() == QDialog.DialogCode.Accepted:
            try:
                updated_schedules = editor.get_updated_schedules()
                self.schedule_manager.schedules = updated_schedules  # Update in memory first
                self.schedule_manager.save_schedules(updated_schedules)  # Then save to file
                self.update_events()
            except Exception as e:
                QMessageBox.critical(self, "Error", f"Failed to save schedules: {str(e)}")

    def change_password(self):
        current_pwd, ok = QInputDialog.getText(
            self,
            'Change Password',
            'Enter current password:',
            QLineEdit.EchoMode.Password
        )
        
        if not ok:
            return
        
        if current_pwd != self.settings_manager.get_admin_password():
            QMessageBox.warning(self, 'Error', 'Incorrect password')
            return
        
        new_pwd, ok = QInputDialog.getText(
            self,
            'Change Password',
            'Enter new password:',
            QLineEdit.EchoMode.Password
        )
        
        if not ok or not new_pwd:
            return
        
        confirm_pwd, ok = QInputDialog.getText(
            self,
            'Change Password',
            'Confirm new password:',
            QLineEdit.EchoMode.Password
        )
        
        if not ok:
            return
        
        if new_pwd != confirm_pwd:
            QMessageBox.warning(self, 'Error', 'Passwords do not match')
            return
        
        self.settings_manager.save_admin_password(new_pwd)
        QMessageBox.information(self, 'Success', 'Password changed successfully')

    def show_color_settings(self):
        dialog = ColorSettingsDialog(self)
        if dialog.exec() == QDialog.DialogCode.Accepted:
            self.apply_styles()

    def closeEvent(self, event):
        """Handle the window close event"""
        reply = QMessageBox.question(self, 'Exit', 'Are you sure you want to exit?',
                                     QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
                                     QMessageBox.StandardButton.No)
        if reply == QMessageBox.StandardButton.Yes:
            event.accept()
            QApplication.quit()  # Ensure the application quits
        else:
            event.ignore()

    def quit_application(self):
        """Show confirmation dialog before quitting"""
        # Instead of duplicating the dialog, trigger the close event
        self.close()  # This will trigger closeEvent

    def toggle_test_mode(self, checked):
        if checked:
            password, ok = QInputDialog.getText(
                self, 
                'Test Mode Access',
                'Enter password to enable test mode:',
                QLineEdit.EchoMode.Password
            )
            
            if ok and password == self.settings_manager.get_admin_password():
                self.test_mode_action.setText('Disable Test Mode')
                # Save current size before switching to test mode
                self.pre_test_size_name = self.settings_manager.get_window_size_name()
                self.setup_test_controls()
                # Force test mode size
                self.resize(WINDOW_SIZES['test_mode'])
            else:
                self.test_mode_action.setChecked(False)
                if ok:  # Only show error if user didn't cancel
                    QMessageBox.warning(self, 'Error', 'Incorrect password')
        else:
            self.test_mode_action.setText('Enable Test Mode')
            if self.test_container:
                self.main_layout.removeWidget(self.test_container)
                self.test_container.deleteLater()
                self.test_container = None
                # Restore previous size
                saved_size = self.settings_manager.get_window_size_name()
                self.resize(WINDOW_SIZES[saved_size])
            self.test_mode = False
            self.update_events()

    def restore_window_position(self):
        super().restore_window_position()

    def set_test_time(self):
        if self.test_mode:
            time = self.time_edit.time()
            self.test_time = datetime.now().replace(
                hour=time.hour(),
                minute=time.minute(),
                second=0
            )
            self.update_events()

    def load_test_file(self):
        """Load and process a test file"""
        file_dialog = QFileDialog()
        file_path, _ = file_dialog.getOpenFileName(
            self,
            "Select Test File",
            str(Path(TEST_FILES_DIR)),
            "Text Files (*.txt)"
        )
        
        if file_path:
            try:
                with open(file_path, 'r') as f:
                    times = f.readlines()
                
                # Clean up times and validate format
                self.test_times = []
                for t in times:
                    t = t.strip()
                    if t:
                        try:
                            # Validate time format
                            datetime.strptime(t, "%H:%M")
                            self.test_times.append(t)
                        except ValueError:
                            continue
                
                if self.test_times:
                    self.current_test_index = 0
                    self.test_time = datetime.strptime(self.test_times[0], "%H:%M")
                    self.time_edit.setTime(QTime(self.test_time.hour, self.test_time.minute))
                    
                    # Start timer for automated testing
                    if self.test_timer is None:
                        self.test_timer = QTimer()
                        self.test_timer.timeout.connect(self.advance_test_time)
                    
                    delay_seconds = self.delay_spinner.value()
                    self.test_timer.start(delay_seconds * 1000)  # Convert to milliseconds
                    self.update_events()
                else:
                    QMessageBox.warning(self, "Error", "No valid times found in file")
            except Exception as e:
                QMessageBox.warning(self, "Error", f"Failed to load test file: {str(e)}")

    def stop_test(self):
        """Stop automated testing"""
        if self.test_timer:
            self.test_timer.stop()
            self.test_timer = None
            self.test_times = None
            self.current_test_index = None

    def advance_test_time(self):
        """Advance to next time in test sequence"""
        if self.test_times and self.current_test_index is not None:
            self.current_test_index += 1
            if self.current_test_index < len(self.test_times):
                try:
                    time_str = self.test_times[self.current_test_index].strip()
                    self.test_time = datetime.strptime(time_str, "%H:%M")
                    self.time_edit.setTime(QTime(self.test_time.hour, self.test_time.minute))
                    self.set_test_time()  # This will trigger the proper period updates
                except ValueError as e:
                    print(f"Error parsing time: {e}")
                    self.stop_test()
            else:
                self.stop_test()

    def change_tray_icon(self):
        """Allow user to select a new tray icon"""
        icons_dir = os.path.join(ASSETS_DIR, 'icons')
        file_path, _ = QFileDialog.getOpenFileName(
            self,
            "Select Tray Icon",
            icons_dir,
            "Image Files (*.png *.jpg *.jpeg *.ico);;All Files (*.*)"
        )
        
        if file_path:
            try:
                # Test if the file can be loaded as an icon
                icon = QIcon(file_path)
                if icon.isNull():
                    raise Exception("Invalid icon file")
                    
                # Save the new icon path
                self.settings_manager.save_tray_icon_path(file_path)
                
                # Update the tray icon
                self.tray_icon.setIcon(icon)
                
                QMessageBox.information(self, "Success", "Tray icon updated successfully")
            except Exception as e:
                QMessageBox.critical(self, "Error", f"Failed to set new icon: {str(e)}")

    def change_window_size(self):
        """Show dialog to change window size"""
        current_size = self.settings_manager.get_window_size_name()
        dialog = WindowSizeDialog(current_size, self)
        
        if dialog.exec() == QDialog.DialogCode.Accepted:
            size_name = dialog.get_selected_size()
            self.settings_manager.save_window_size_name(size_name)
            
            # Resize the window
            new_size = WINDOW_SIZES[size_name]
            self.setFixedSize(new_size)  # Force the size
            self.adjustSize()  # Make sure contents adjust
            
            # After a brief delay, remove the fixed size constraint
            QTimer.singleShot(100, lambda: self.setFixedSize(QWIDGETSIZE_MAX, QWIDGETSIZE_MAX))
            
            # Center the window
            self.center_on_screen()
            
    def show_about(self):
        """Show the About dialog"""
        dialog = AboutDialog(self)
        dialog.exec()

    def show_documentation(self):
        """Show the user guide"""
        try:
            # Get the path to the user guide markdown file
            user_guide_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 
                                         'docs', 'user_guide.md')
            
            # Read the user guide content
            with open(user_guide_path, 'r') as f:
                content = f.read()
            
            # Show the guide in a proper dialog
            from dialogs.user_guide_dialog import UserGuideDialog
            dialog = UserGuideDialog(content, self)
            dialog.exec()
            
        except Exception as e:
            QMessageBox.warning(
                self,
                "Error",
                f"Could not load user guide: {str(e)}",
                QMessageBox.StandardButton.Ok
            )

    def show_message_settings(self):
        dialog = MessageSettingsDialog(self.settings_manager, self)
        if dialog.exec() == QDialog.DialogCode.Accepted:
            # Refresh messages in schedule manager
            self.schedule_manager.messages = self.settings_manager.get_schedule_messages()
            # Update display
            self.update_events() 