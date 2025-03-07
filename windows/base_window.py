# Common window functionality
# Contains shared methods like center_on_screen, save_window_position, etc. 

from PyQt6.QtWidgets import QMainWindow, QApplication
from PyQt6.QtCore import QSettings, QPoint, QSize
from constants import APP_ORGANIZATION, APP_NAME

class BaseWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.settings = QSettings(APP_ORGANIZATION, APP_NAME)
        
    def save_window_position(self):
        pos = self.pos()
        size = self.size()
        self.settings.setValue('window_position_x', pos.x())
        self.settings.setValue('window_position_y', pos.y())
        self.settings.setValue('window_width', size.width())
        self.settings.setValue('window_height', size.height())

    def restore_window_position(self):
        pos_x = self.settings.value('window_position_x', type=int)
        pos_y = self.settings.value('window_position_y', type=int)
        width = self.settings.value('window_width', 300, type=int)
        height = self.settings.value('window_height', 200, type=int)
        
        if pos_x is not None and pos_y is not None:
            screen = QApplication.primaryScreen().availableGeometry()
            if (screen.contains(pos_x, pos_y) and 
                screen.contains(pos_x + width, pos_y + height)):
                self.move(pos_x, pos_y)
                self.resize(width, height)
            else:
                self.center_on_screen()

    def center_on_screen(self):
        self.adjustSize()
        screen = QApplication.primaryScreen().availableGeometry()
        x = screen.center().x() - (self.frameGeometry().width() // 2)
        y = screen.center().y() - (self.frameGeometry().height() // 2)
        x = max(screen.left(), min(x, screen.right() - self.frameGeometry().width()))
        y = max(screen.top(), min(y, screen.bottom() - self.frameGeometry().height()))
        self.move(x, y) 