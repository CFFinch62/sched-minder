# Settings management and persistence 
from PyQt6.QtCore import QSettings
from constants import APP_ORGANIZATION, APP_NAME, DEFAULT_COLORS, DEFAULT_ADMIN_PASSWORD, ICON_PATH, DEFAULT_MESSAGES

class SettingsManager:
    def __init__(self):
        self.settings = QSettings(APP_ORGANIZATION, APP_NAME)
        
    def get_colors(self):
        colors = {}
        for key, default in DEFAULT_COLORS.items():
            colors[key] = self.settings.value(key, default)
        return colors
        
    def save_colors(self, colors):
        for key, value in colors.items():
            self.settings.setValue(key, value)
            
    def get_admin_password(self):
        return self.settings.value('admin_password', DEFAULT_ADMIN_PASSWORD)
        
    def save_admin_password(self, password):
        self.settings.setValue('admin_password', password)
        
    def get_tray_icon_path(self):
        """Get custom tray icon path or return default"""
        return self.settings.value('tray_icon_path', ICON_PATH)
        
    def save_tray_icon_path(self, path):
        """Save custom tray icon path"""
        self.settings.setValue('tray_icon_path', path)
        
    def get_window_size_name(self):
        """Get the saved window size name or return default"""
        # Convert the value to string to ensure we get the name, not a QSize
        saved_size = self.settings.value('window_size', 'small')
        if isinstance(saved_size, str):
            return saved_size
        return 'small'  # Default if not a valid string
        
    def save_window_size_name(self, size_name):
        """Save the window size name"""
        self.settings.setValue('window_size', size_name)
        
    def get_schedule_messages(self):
        """Get customized schedule messages or return defaults"""
        messages = {}
        for key, default in DEFAULT_MESSAGES.items():
            messages[key] = self.settings.value(f'messages/{key}', default)
        return messages
        
    def save_schedule_messages(self, messages):
        """Save customized schedule messages"""
        for key, message in messages.items():
            self.settings.setValue(f'messages/{key}', message) 