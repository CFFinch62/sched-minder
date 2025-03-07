# Schedule Minder API Reference

## Windows Package

### BaseWindow
Base class for application windows providing common functionality.

```python
class BaseWindow(QMainWindow):
    """Base window class with common window management features"""
    
    def save_window_position(self):
        """Save current window position and size to settings"""
        
    def restore_window_position(self):
        """Restore window position and size from settings"""
        
    def center_on_screen(self):
        """Center window on the primary screen"""
```

### ScheduleWindow
Main application window handling schedule display and management.

```python
class ScheduleWindow(BaseWindow):
    """Main application window"""
    
    def __init__(self, enable_test_mode=False):
        """Initialize main window
        
        Args:
            enable_test_mode (bool): Start in test mode if True
        """
    
    def setup_ui(self):
        """Create and configure UI elements"""
        
    def update_periods(self):
        """Update all period displays"""
        
    def create_menu_bar(self):
        """Create application menu bar"""
        
    def setup_system_tray(self):
        """Initialize system tray icon and menu"""
        
    def setup_test_controls(self):
        """Create test mode UI elements"""
```

## Dialogs Package

### ColorSettingsDialog
Dialog for customizing application colors.

```python
class ColorSettingsDialog(QDialog):
    """Color customization dialog"""
    
    def setup_ui(self):
        """Create color selection interface"""
        
    def create_color_button(self, label_text, setting_name, layout):
        """Create a color selection button
        
        Args:
            label_text (str): Button label
            setting_name (str): Setting key for color
            layout (QLayout): Parent layout
        """
        
    def reset_colors(self):
        """Reset all colors to defaults"""
```

### ScheduleEditorDialog
Dialog for editing schedule periods and times.

```python
class ScheduleEditorDialog(QDialog):
    """Schedule editing dialog"""
    
    def __init__(self, schedules, parent=None):
        """Initialize editor
        
        Args:
            schedules (dict): Schedule data
            parent (QWidget): Parent widget
        """
    
    def setup_ui(self):
        """Create schedule editing interface"""
        
    def add_event(self):
        """Add new event to schedule"""
        
    def delete_event(self):
        """Delete selected event"""
```

## Utils Package

### ScheduleManager
Handles schedule data and period calculations.

```python
class ScheduleManager:
    """Schedule data management and calculations"""
    
    def load_schedules(self):
        """Load schedules from file
        
        Returns:
            dict: Schedule data
        """
        
    def save_schedules(self, schedules):
        """Save schedules to file
        
        Args:
            schedules (dict): Schedule data to save
        """
        
    def get_current_event(self, schedule_type, current_time=None):
        """Get current event for schedule
        
        Args:
            schedule_type (str): Schedule identifier
            current_time (datetime, optional): Time to check
            
        Returns:
            str: Current event or status
        """
```

### SettingsManager
Manages application settings and persistence.

```python
class SettingsManager:
    """Application settings management"""
    
    def get_colors(self):
        """Get color settings
        
        Returns:
            dict: Color settings
        """
        
    def save_colors(self, colors):
        """Save color settings
        
        Args:
            colors (dict): Color values to save
        """
        
    def get_window_size_name(self):
        """Get saved window size name
        
        Returns:
            str: Size name ('small', 'medium', 'large')
        """
```

### TestFileHelper
Utilities for test mode file operations.

```python
class TestFileHelper:
    """Test file management utilities"""
    
    @staticmethod
    def get_test_file_path(file_name):
        """Get full path to test file
        
        Args:
            file_name (str): Test file name
            
        Returns:
            str: Full file path
        """
        
    @staticmethod
    def get_available_test_files():
        """Get list of available test files
        
        Returns:
            list: Test file names
        """
```

### UIHelper
Common UI creation functions.

```python
def create_event_display(label_text, name):
    """Create labeled event display
    
    Args:
        label_text (str): Label text
        name (str): Object name for styling
        
    Returns:
        tuple: (container widget, event label)
    """
```

## Constants

### Window Sizes
```python
WINDOW_SIZES = {
    'small': QSize(305, 230),
    'medium': QSize(445, 355),
    'large': QSize(675, 555),
    'test_mode': QSize(385, 320)
}
```

### Colors
```python
DEFAULT_COLORS = {
    "window_bg_color": "#000000",
    "window_text_color": "#FFFFFF",
    "message_bg_color": "#000066",
    "message_text_color": "#FFFFFF"
}
```

### File Paths
```python
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ASSETS_DIR = os.path.join(BASE_DIR, 'assets')
DATA_DIR = os.path.join(BASE_DIR, 'data')
SCHEDULES_FILE = os.path.join(DATA_DIR, 'schedules.json')
```

## Message System

### MessageSettingsDialog
```python
class MessageSettingsDialog(QDialog):
    """Dialog for customizing schedule messages
    
    Attributes:
        settings_manager (SettingsManager): Manager for message settings
        message_inputs (dict): Dictionary of message input fields
    """
    
    def setup_ui(self):
        """Create and configure the dialog UI"""
        
    def save_messages(self):
        """Save modified messages to settings"""
        
    def reset_to_default(self):
        """Reset messages to default values"""
```

### SettingsManager Message Methods
```python
def get_schedule_messages(self):
    """Get customized schedule messages or return defaults
    
    Returns:
        dict: Message type to message text mapping
    """
    
def save_schedule_messages(self, messages):
    """Save customized schedule messages
    
    Args:
        messages (dict): Message type to message text mapping
    """
```

### ScheduleManager Message Integration
```python
def get_current_period(self, schedule_type, current_time=None):
    """Get formatted message for current schedule state
    
    Messages are formatted using the following templates:
    - Before schedule: messages['before_schedule']
    - During event: messages['during_period'].format(event_name=name)
    - Between events: messages['between_periods'].format(
        prev_event=prev, next_event=next)
    - After schedule: messages['after_schedule']
    """
``` 