import PyQt6
from pathlib import Path
from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QPushButton
from PyQt6.QtGui import QIcon
from PyQt6.QtCore import QSize

class functionalButton(QPushButton):
    def __init__(self, parent=None, option = None, icon=None):
        super().__init__(parent)
        self.option = option
        self.setFixedSize(32,32)
        self.icon = QIcon(f"icons/{icon}")
        self.setIcon(self.icon)
        self.setIconSize(QSize(32, 32))