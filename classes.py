from PyQt6 import QtWidgets
from PyQt6.QtCore import Qt, QPoint
from PyQt6.QtGui import QPixmap, QPainter, QPen, QColor, QMouseEvent
from PyQt6.QtWidgets import QLabel, QPushButton


class CanvasWidget(QLabel):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.last_mouse_position = QPoint()

        self.canvas = QPixmap(1920, 1000)
        self.canvas.fill(Qt.GlobalColor.white)
        self.setPixmap(self.canvas)

        self.pen = QPen(QColor("black"), 4, Qt.PenStyle.SolidLine,
                        Qt.PenCapStyle.RoundCap, Qt.PenJoinStyle.RoundJoin)
        self.pen1 = QPen(QColor("black"), 4, Qt.PenStyle.SolidLine,
                        Qt.PenCapStyle.RoundCap, Qt.PenJoinStyle.RoundJoin)

    def mousePressEvent(self, event: QMouseEvent):
        if event.button() == Qt.MouseButton.LeftButton:
            self.last_mouse_position = event.position().toPoint()
        elif event.button() == Qt.MouseButton.RightButton:
            self.last_mouse_position = event.position().toPoint()

    def mouseMoveEvent(self, event: QMouseEvent):
        buttons = event.buttons().value
        right_pressed = Qt.MouseButton.RightButton.value

        if event.buttons() & Qt.MouseButton.LeftButton:
            current_position = event.position().toPoint()

            painter = QPainter(self.canvas)
            painter.setPen(self.pen)
            painter.drawLine(self.last_mouse_position, current_position)
            painter.end()

            self.setPixmap(self.canvas)
            self.last_mouse_position = current_position

        elif buttons & right_pressed:
            current_position = event.position().toPoint()

            painter = QPainter(self.canvas)
            painter.setPen(self.pen1)
            painter.drawLine(self.last_mouse_position, current_position)
            painter.end()

            self.setPixmap(self.canvas)
            self.last_mouse_position = current_position

class ColorButton(QPushButton):
    def __init__(self, parent=None, color = None):
        super().__init__()
        self.setStyleSheet(f"background-color:{color};border-radius:0px;border:1px solid grey;")
        self.setGeometry(0, 0, 40, 40)


class sliders(QtWidgets.QLabel):
    def __init__(self, parent=None, text = None):
        super().__init__(parent)
        self.setStyleSheet("font-size: 20px;")
        self.setText(f"{text}")

class radialColorButton(QPushButton):
    def __init__(self, parent=None, color = "black"):
        super().__init__(parent)
        self.setStyleSheet(f"background-color:{color};")

    def colorChange(self, color):
        self.setStyleSheet(f"background-color:{color};border:1px solid grey;")

