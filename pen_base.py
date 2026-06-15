from PyQt6.QtCore import Qt, QPoint
from PyQt6.QtGui import QPixmap, QPainter, QPen, QColor, QMouseEvent
from PyQt6.QtWidgets import  QLabel


class CanvasWidget(QLabel):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.last_mouse_position = QPoint()

        self.canvas = QPixmap(1920, 1000)
        self.canvas.fill(Qt.GlobalColor.white)
        self.setPixmap(self.canvas)

        self.pen = QPen(QColor("black"), 4, Qt.PenStyle.SolidLine,
                        Qt.PenCapStyle.RoundCap, Qt.PenJoinStyle.RoundJoin)

    def mousePressEvent(self, event: QMouseEvent):
        if event.button() == Qt.MouseButton.LeftButton:

            self.last_mouse_position = event.position().toPoint()

    def mouseMoveEvent(self, event: QMouseEvent):
        if event.buttons() == Qt.MouseButton.LeftButton:
            current_position = event.position().toPoint()

            painter = QPainter(self.canvas)
            painter.setPen(self.pen)
            painter.drawLine(self.last_mouse_position, current_position)
            painter.end()

            self.setPixmap(self.canvas)
            self.last_mouse_position = current_position

