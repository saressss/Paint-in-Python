from PyQt6 import QtWidgets
from PyQt6.QtCore import Qt, QPoint
from PyQt6.QtGui import QPixmap, QPainter, QPen, QColor, QMouseEvent, QImage, QFont
from PyQt6.QtWidgets import QLabel, QPushButton, QInputDialog


class CanvasWidget(QLabel):
    def __init__(self, parent=None, option="pencil", main = None):
        super().__init__(parent)
        self.main_ui = parent
        self.main = main
        self.last_mouse_position = QPoint()
        self.option = option

        self.zoom_factor = 1.0

        self.canvas = QPixmap(1920, 1000)
        self.canvas.fill(Qt.GlobalColor.white)
        self.setPixmap(self.canvas)

        self.pen = QPen(QColor("black"), 4, Qt.PenStyle.SolidLine,
                        Qt.PenCapStyle.RoundCap, Qt.PenJoinStyle.RoundJoin)
        self.pen1 = QPen(QColor("black"), 4, Qt.PenStyle.SolidLine,
                         Qt.PenCapStyle.RoundCap, Qt.PenJoinStyle.RoundJoin)

    def set_tool(self, tool_name):
        self.option = tool_name

    def mousePressEvent(self, event: QMouseEvent):
        pos = event.position().toPoint()

        transformed_pos = QPoint(int(pos.x() / self.zoom_factor), int(pos.y() / self.zoom_factor))
        self.last_mouse_position = transformed_pos

        if self.option == "glass":
            old_zoom = self.zoom_factor

            # Змінюємо рівень зуму
            if event.button() == Qt.MouseButton.LeftButton:
                self.zoom_factor = min(self.zoom_factor + 0.5, 5.0)
            elif event.button() == Qt.MouseButton.RightButton:
                self.zoom_factor = max(self.zoom_factor - 0.5, 1.0)

            if old_zoom != self.zoom_factor:
                scroll_area = self.parent().parent()

                if scroll_area and hasattr(scroll_area, 'horizontalScrollBar'):
                    visible_pos = self.mapTo(scroll_area.widgetResizable() and scroll_area or self.parent(), pos)

                    self.update_canvas_display()

                    new_h_bar = int(transformed_pos.x() * self.zoom_factor - event.position().x() + (
                                event.position().x() - pos.x()))
                    new_v_bar = int(transformed_pos.y() * self.zoom_factor - event.position().y() + (
                                event.position().y() - pos.y()))

                    scroll_area.horizontalScrollBar().setValue(
                        int(transformed_pos.x() * self.zoom_factor - pos.x() + scroll_area.horizontalScrollBar().value()))
                    scroll_area.verticalScrollBar().setValue(
                        int(transformed_pos.y() * self.zoom_factor - pos.y() + scroll_area.verticalScrollBar().value()))
                else:
                    self.update_canvas_display()
            return

        elif self.option == "floodfill" and event.button() == Qt.MouseButton.LeftButton:
            self.flood_fill(transformed_pos, self.pen.color())

        elif self.option == "pipette":
            image = self.canvas.toImage()
            if image.valid(transformed_pos):
                color = image.pixelColor(transformed_pos)
                if self.main is not None:
                    self.main.primaryColor = color.name()
                self.pen.setColor(color)

        elif self.option == "text" and event.button() == Qt.MouseButton.LeftButton:
            text, ok = QInputDialog.getText(self, "Введення тексту", "Введіть текст:")
            if ok and text:
                painter = QPainter(self.canvas)
                painter.setPen(self.pen)
                painter.setFont(QFont("Arial", int(self.pen.width() * 3)))
                painter.drawText(transformed_pos, text)
                painter.end()
                self.update_canvas_display()

    def mouseMoveEvent(self, event: QMouseEvent):
        pos = event.position().toPoint()
        current_position = QPoint(int(pos.x() / self.zoom_factor), int(pos.y() / self.zoom_factor))

        if self.option in ["pencil", "pen", "rubber"]:
            painter = QPainter(self.canvas)

            if self.option == "rubber":
                eraser_pen = QPen(Qt.GlobalColor.white, self.pen.width(), Qt.PenStyle.SolidLine,
                                  Qt.PenCapStyle.RoundCap, Qt.PenJoinStyle.RoundJoin)
                painter.setPen(eraser_pen)
            else:
                if event.buttons() & Qt.MouseButton.LeftButton:
                    painter.setPen(self.pen)
                elif event.buttons() & Qt.MouseButton.RightButton:
                    painter.setPen(self.pen1)
                else:
                    painter.end()
                    return

            painter.drawLine(self.last_mouse_position, current_position)
            painter.end()

            self.last_mouse_position = current_position
            self.update_canvas_display()

    def update_canvas_display(self):
        new_width = int(self.canvas.width() * self.zoom_factor)
        new_height = int(self.canvas.height() * self.zoom_factor)

        self.resize(new_width, new_height)

        if self.zoom_factor == 1.0:
            self.setPixmap(self.canvas)
        else:
            scaled_pixmap = self.canvas.scaled(new_width, new_height,
                                               Qt.AspectRatioMode.KeepAspectRatio,
                                               Qt.TransformationMode.FastTransformation)
            self.setPixmap(scaled_pixmap)

    def flood_fill(self, start_point, fill_color):
        image = self.canvas.toImage()
        width, height = image.width(), image.height()

        target_color = image.pixelColor(start_point)
        if target_color == fill_color:
            return

        queue = [start_point]
        target_rgb = target_color.rgba()
        fill_rgb = fill_color.rgba()

        while queue:
            p = queue.pop(0)
            x, y = p.x(), p.y()

            if image.pixel(x, y) == target_rgb:
                image.setPixel(x, y, fill_rgb)

                if x > 0: queue.append(QPoint(x - 1, y))
                if x < width - 1: queue.append(QPoint(x + 1, y))
                if y > 0: queue.append(QPoint(x, y - 1))
                if y < height - 1: queue.append(QPoint(x, y + 1))

        self.canvas = QPixmap.fromImage(image)
        self.update_canvas_display()


class ColorButton(QPushButton):
    def __init__(self, parent=None, color=None):
        super().__init__()
        self.setStyleSheet(f"background-color:{color};border-radius:0px;border:1px solid grey;")
        self.setGeometry(0, 0, 40, 40)


class sliders(QtWidgets.QLabel):
    def __init__(self, parent=None, text=None):
        super().__init__(parent)
        self.setStyleSheet("font-size: 20px;")
        self.setText(f"{text}")


class radialColorButton(QPushButton):
    def __init__(self, parent=None, color="black"):
        super().__init__(parent)
        self.setStyleSheet(f"background-color:{color};")

    def colorChange(self, color):
        self.setStyleSheet(f"background-color:{color};border:1px solid grey;")