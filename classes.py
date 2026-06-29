import math
import random
from collections import deque
from PyQt6 import QtWidgets
from PyQt6.QtCore import Qt, QPoint, QPointF
from PyQt6.QtGui import QPixmap, QPainter, QPen, QColor, QMouseEvent, QFont, QPolygon, QPainterPath, QGuiApplication, QPolygonF, QBrush, QCursor
from PyQt6.QtWidgets import QLabel, QInputDialog, QPushButton


class CanvasWidget(QLabel):
    def __init__(self, parent=None, option="instrument", main=None, optionaddit="pencil"):
        super().__init__(parent)
        self.main_ui = parent
        self.main = main
        self.last_mouse_position = QPoint()

        self.option = option
        self.ShapeOption = optionaddit
        self.is_drawing = False
        self.zoom_factor = 1.0

        self.canvas = QPixmap(1920, 1000)
        self.canvas.fill(Qt.GlobalColor.white)
        self.setPixmap(self.canvas)

        self.history = []

        self.canvas_preview = QPixmap(self.canvas)

        self.pen = QPen(QColor("black"), 4, Qt.PenStyle.SolidLine,
                        Qt.PenCapStyle.RoundCap, Qt.PenJoinStyle.RoundJoin)
        self.pen1 = QPen(QColor("black"), 4, Qt.PenStyle.SolidLine,
                         Qt.PenCapStyle.RoundCap, Qt.PenJoinStyle.RoundJoin)

        self.brush_style = "Пензель"

    def save_to_png(self, file_path):
        if hasattr(self, 'canvas') and not self.canvas.isNull():
            success = self.canvas.save(file_path, "PNG")
            return success
        return False

    def set_tool(self, toolArr, optionAddit):
        self.option = toolArr
        self.ShapeOption = optionAddit

    def set_brush_style(self, style_name):
        self.brush_style = style_name

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

    def save_to_history(self):
        self.history.append(QPixmap(self.canvas))

        if len(self.history) > 30:
            self.history.pop(0)

    def keyPressEvent(self, event):
        if event.modifiers() == Qt.KeyboardModifier.ControlModifier and event.key() == Qt.Key.Key_Z:
            if self.history:
                previous_canvas = self.history.pop()

                self.canvas = previous_canvas
                self.canvas_preview = QPixmap(self.canvas)

                self.update_canvas_display()
                event.accept()
            else:
                event.ignore()

        elif event.modifiers() == Qt.KeyboardModifier.ControlModifier and event.key() == Qt.Key.Key_V:
            clipboard = QGuiApplication.clipboard()
            mime_data = clipboard.mimeData()

            if mime_data.hasImage():
                self.save_to_history()
                image = clipboard.image()
                pasted_pixmap = QPixmap.fromImage(image)

                global_mouse_pos = QCursor.pos()
                local_mouse_pos = self.mapFromGlobal(global_mouse_pos)

                canvas_x = int(local_mouse_pos.x() / self.zoom_factor)
                canvas_y = int(local_mouse_pos.y() / self.zoom_factor)

                spawn_x = canvas_x - (pasted_pixmap.width() // 2)
                spawn_y = canvas_y - (pasted_pixmap.height() // 2)

                painter = QPainter(self.canvas)
                painter.drawPixmap(spawn_x, spawn_y, pasted_pixmap)
                painter.end()

                self.update_canvas_display()
                event.accept()
            else:
                event.ignore()
        else:
            super().keyPressEvent(event)

    def mousePressEvent(self, event: QMouseEvent):
        self.setFocus()

        pos = event.position().toPoint()
        transformed_pos = QPoint(int(pos.x() / self.zoom_factor), int(pos.y() / self.zoom_factor))
        self.last_mouse_position = transformed_pos

        if event.button() == Qt.MouseButton.LeftButton or event.button():
            self.save_to_history()
            self.is_drawing = True
            self.canvas_preview = QPixmap(self.canvas)

        if self.option == "instrument":
            if self.ShapeOption == "glass":
                old_zoom = self.zoom_factor
                if event.button() == Qt.MouseButton.LeftButton:
                    self.save_to_history()
                    self.zoom_factor = min(self.zoom_factor + 0.5, 5.0)
                elif event.button() == Qt.MouseButton.RightButton:
                    self.save_to_history()
                    self.zoom_factor = max(self.zoom_factor - 0.5, 1.0)

                if old_zoom != self.zoom_factor:
                    scroll_area = self.parent().parent()
                    if scroll_area and hasattr(scroll_area, 'horizontalScrollBar'):
                        self.update_canvas_display()
                        scroll_area.horizontalScrollBar().setValue(
                            int(transformed_pos.x() * self.zoom_factor - pos.x() + scroll_area.horizontalScrollBar().value()))
                        scroll_area.verticalScrollBar().setValue(
                            int(transformed_pos.y() * self.zoom_factor - pos.y() + scroll_area.verticalScrollBar().value()))
                    else:
                        self.update_canvas_display()
                return

            elif self.ShapeOption == "floodfill" and event.button() == Qt.MouseButton.LeftButton:
                self.save_to_history()
                self.flood_fill(transformed_pos, self.pen.color())

            elif self.ShapeOption == "pipette":
                image = self.canvas.toImage()
                if image.valid(transformed_pos):
                    color = image.pixelColor(transformed_pos)
                    if self.main is not None:
                        self.main.primaryColor = color.name()
                    self.pen.setColor(color)

            elif self.ShapeOption == "text" and event.button() == Qt.MouseButton.LeftButton:
                self.save_to_history()
                text, ok = QInputDialog.getText(self, "Введення тексту", "Введіть текст:")
                if ok and text:
                    painter = QPainter(self.canvas)
                    painter.setPen(self.pen)
                    painter.setFont(QFont("Arial", int(self.pen.width() * 3)))
                    painter.drawText(transformed_pos, text)
                    painter.end()
                    self.update_canvas_display()

    def mouseMoveEvent(self, event: QMouseEvent):
        if not self.is_drawing:
            return

        pos = event.position().toPoint()
        current_position = QPoint(int(pos.x() / self.zoom_factor), int(pos.y() / self.zoom_factor))

        if self.option == "instrument":
            if self.ShapeOption in ["pencil", "rubber"]:
                painter = QPainter(self.canvas)

                if self.ShapeOption == "rubber":
                    painter.setRenderHint(QPainter.RenderHint.Antialiasing)
                    eraser_pen = QPen(Qt.GlobalColor.white, self.pen.width(), Qt.PenStyle.SolidLine,
                                      Qt.PenCapStyle.RoundCap, Qt.PenJoinStyle.RoundJoin)
                    painter.setPen(eraser_pen)
                    painter.drawLine(self.last_mouse_position, current_position)
                else:
                    active_pen = self.pen if (event.buttons() & Qt.MouseButton.LeftButton) else self.pen1
                    color = active_pen.color()
                    width = active_pen.width()

                    if self.brush_style == "Пензель":
                        painter.setRenderHint(QPainter.RenderHint.Antialiasing)
                        painter.setPen(active_pen)
                        painter.drawLine(self.last_mouse_position, current_position)

                    elif self.brush_style == "Каліграфічний пензель":
                        painter.setRenderHint(QPainter.RenderHint.Antialiasing)
                        steps = max(abs(current_position.x() - self.last_mouse_position.x()),
                                    abs(current_position.y() - self.last_mouse_position.y())) * 2
                        painter.setBrush(QBrush(color))
                        painter.setPen(Qt.PenStyle.NoPen)

                        for step in range(steps + 1):
                            t = step / max(steps, 1)
                            cx = int(self.last_mouse_position.x() + (
                                        current_position.x() - self.last_mouse_position.x()) * t)
                            cy = int(self.last_mouse_position.y() + (
                                        current_position.y() - self.last_mouse_position.y()) * t)

                            painter.save()
                            painter.translate(cx, cy)
                            painter.rotate(-30)
                            painter.drawEllipse(QPoint(0, 0), int(width * 1.5), int(width * 0.3))
                            painter.restore()

                    elif self.brush_style == "Каліграфічне перо":
                        painter.setRenderHint(QPainter.RenderHint.Antialiasing)
                        painter.setPen(Qt.PenStyle.NoPen)
                        painter.setBrush(QBrush(color))

                        steps = max(abs(current_position.x() - self.last_mouse_position.x()),
                                    abs(current_position.y() - self.last_mouse_position.y()))
                        for step in range(steps + 1):
                            t = step / max(steps, 1)
                            cx = self.last_mouse_position.x() + (
                                        current_position.x() - self.last_mouse_position.x()) * t
                            cy = self.last_mouse_position.y() + (
                                        current_position.y() - self.last_mouse_position.y()) * t
                            points = QPolygonF([
                                QPointF(cx - width, cy - width / 2),
                                QPointF(cx + width, cy - width / 2),
                                QPointF(cx + width / 2, cy + width / 2),
                                QPointF(cx - width / 2, cy + width / 2)
                            ])
                            painter.drawPolygon(points)

                    elif self.brush_style == "Пензель для олії":
                        painter.setRenderHint(QPainter.RenderHint.Antialiasing)
                        steps = max(abs(current_position.x() - self.last_mouse_position.x()),
                                    abs(current_position.y() - self.last_mouse_position.y()))

                        for step in range(steps + 1):
                            t = step / max(steps, 1)
                            cx = self.last_mouse_position.x() + (
                                        current_position.x() - self.last_mouse_position.x()) * t
                            cy = self.last_mouse_position.y() + (
                                        current_position.y() - self.last_mouse_position.y()) * t

                            for offset in range(-width, width, max(1, width // 4)):
                                alpha_color = QColor(color.red(), color.green(), color.blue(), 40)
                                painter.setPen(QPen(alpha_color, max(1, width // 5), Qt.PenStyle.SolidLine))
                                painter.drawEllipse(QPoint(int(cx + offset), int(cy + (offset // 2))),
                                                    max(1, width // 4), max(1, width // 4))

                    elif self.brush_style == "Пастель":
                        import random
                        steps = max(abs(current_position.x() - self.last_mouse_position.x()),
                                    abs(current_position.y() - self.last_mouse_position.y()))

                        for step in range(steps + 1):
                            t = step / max(steps, 1)
                            cx = self.last_mouse_position.x() + (
                                        current_position.x() - self.last_mouse_position.x()) * t
                            cy = self.last_mouse_position.y() + (
                                        current_position.y() - self.last_mouse_position.y()) * t

                            for _ in range(int(width * 1.5)):
                                rx = random.gauss(0, width / 2)
                                ry = random.gauss(0, width / 2)
                                if rx * rx + ry * ry <= (width * width):
                                    alpha = random.randint(30, 100)
                                    painter.setPen(QPen(QColor(color.red(), color.green(), color.blue(), alpha), 1))
                                    painter.drawPoint(int(cx + rx), int(cy + ry))

                    elif self.brush_style == "Маркер":
                        marker_color = QColor(color.red(), color.green(), color.blue(), 80)
                        painter.setPen(QPen(marker_color, width * 2, Qt.PenStyle.SolidLine, Qt.PenCapStyle.SquareCap))
                        painter.drawLine(self.last_mouse_position, current_position)

                    elif self.brush_style == "Розпилювач":
                        import random
                        steps = max(abs(current_position.x() - self.last_mouse_position.x()),
                                    abs(current_position.y() - self.last_mouse_position.y())) // 2

                        for step in range(max(1, steps + 1)):
                            t = step / max(steps, 1)
                            cx = self.last_mouse_position.x() + (
                                        current_position.x() - self.last_mouse_position.x()) * t
                            cy = self.last_mouse_position.y() + (
                                        current_position.y() - self.last_mouse_position.y()) * t

                            painter.setPen(QPen(QColor(color.red(), color.green(), color.blue(), 120), 1))
                            radius = width * 3
                            for _ in range(int(width * 2)):
                                angle = random.uniform(0, 2 * math.pi)
                                r = random.uniform(0, radius)
                                dx = int(r * math.cos(angle))
                                dy = int(r * math.sin(angle))
                                painter.drawPoint(int(cx + dx), int(cy + dy))

                    elif self.brush_style == "Звичайний олівець":
                        painter.setRenderHint(QPainter.RenderHint.Antialiasing, False)
                        pencil_pen = QPen(color, max(1, width // 3), Qt.PenStyle.SolidLine, Qt.PenCapStyle.RoundCap)
                        painter.setPen(pencil_pen)
                        painter.drawLine(self.last_mouse_position, current_position)

                painter.end()
                self.last_mouse_position = current_position
                self.update_canvas_display()

        elif self.option == "shape":
            temp_canvas = QPixmap(self.canvas_preview)
            painter = QPainter(temp_canvas)
            painter.setPen(self.pen)

            self.draw_generic_shape(painter, self.ShapeOption, self.last_mouse_position, current_position)
            painter.end()

            if self.zoom_factor == 1.0:
                self.setPixmap(temp_canvas)
            else:
                new_width = int(temp_canvas.width() * self.zoom_factor)
                new_height = int(temp_canvas.height() * self.zoom_factor)
                self.setPixmap(temp_canvas.scaled(new_width, new_height, Qt.AspectRatioMode.KeepAspectRatio,
                                                  Qt.TransformationMode.FastTransformation))

    def mouseReleaseEvent(self, event: QMouseEvent):
        if event.button() == Qt.MouseButton.LeftButton and self.is_drawing:
            self.is_drawing = False

            if self.option == "shape":
                pos = event.position().toPoint()
                current_position = QPoint(int(pos.x() / self.zoom_factor), int(pos.y() / self.zoom_factor))

                self.canvas = QPixmap(self.canvas_preview)
                painter = QPainter(self.canvas)
                painter.setPen(self.pen)

                self.draw_generic_shape(painter, self.ShapeOption, self.last_mouse_position, current_position)
                painter.end()

            self.update_canvas_display()

    def flood_fill(self, start_point, fill_color):
        image = self.canvas.toImage()
        width, height = image.width(), image.height()
        target_color = image.pixelColor(start_point)

        if target_color == fill_color:
            return

        target_rgb = target_color.rgba()
        fill_rgb = fill_color.rgba()


        queue = deque([(start_point.x(), start_point.y())])

        while queue:
            x, y = queue.popleft()

            if x < 0 or x >= width or y < 0 or y >= height:
                continue

            if image.pixel(x, y) == target_rgb:
                image.setPixel(x, y, fill_rgb)

                queue.append((x + 1, y))
                queue.append((x, y + 1))
                queue.append((x - 1, y))
                queue.append((x, y - 1))

        self.canvas = QPixmap.fromImage(image)
        self.update_canvas_display()

    def draw_generic_shape(self, painter, shape_num, start_pt, end_pt):
        x = min(start_pt.x(), end_pt.x())
        y = min(start_pt.y(), end_pt.y())
        w = abs(start_pt.x() - end_pt.x())
        h = abs(start_pt.y() - end_pt.y())
        if w == 0 or h == 0:
            return

        start_f = QPointF(start_pt)
        end_f = QPointF(end_pt)

        if shape_num == "1":
            painter.drawLine(start_pt, end_pt)

        elif shape_num == "2":
            path = QPainterPath()
            path.moveTo(start_f)

            offset_h = h // 2 if start_pt.y() < end_pt.y() else -h // 2
            control1 = QPointF(start_pt.x() + w // 4, start_pt.y() - offset_h)
            control2 = QPointF(end_pt.x() - w // 4, end_pt.y() + offset_h)

            path.cubicTo(control1, control2, end_f)
            painter.drawPath(path)

        elif shape_num == "3":
            painter.drawEllipse(x, y, w, h)

        elif shape_num == "4":
            painter.drawRect(x, y, w, h)

        elif shape_num == "5":
            painter.drawRoundedRect(x, y, w, h, 15, 15)

        elif shape_num == "6":
            painter.drawRect(x, y, w, h)

        elif shape_num == "7":
            points = QPolygon([QPoint(x + w // 2, y), QPoint(x, y + h), QPoint(x + w, y + h)])
            painter.drawPolygon(points)

        elif shape_num == "8":
            points = QPolygon([QPoint(x, y), QPoint(x, y + h), QPoint(x + w, y + h)])
            painter.drawPolygon(points)

        elif shape_num == "9":
            points = QPolygon(
                [QPoint(x + w // 2, y), QPoint(x + w, y + h // 2), QPoint(x + w // 2, y + h), QPoint(x, y + h // 2)])
            painter.drawPolygon(points)

        elif shape_num == "10":
            points = QPolygon([
                QPoint(x + w // 2, y), QPoint(x + w, y + int(h * 0.38)), QPoint(x + int(w * 0.81), y + h),
                QPoint(x + int(w * 0.19), y + h), QPoint(x, y + int(h * 0.38))
            ])
            painter.drawPolygon(points)

        elif shape_num == "11":
            points = QPolygon([
                QPoint(x + w // 2, y), QPoint(x + w, y + h // 4), QPoint(x + w, y + int(h * 0.75)),
                QPoint(x + w // 2, y + h), QPoint(x, y + int(h * 0.75)), QPoint(x, y + h // 4)
            ])
            painter.drawPolygon(points)

        elif shape_num == "12":
            points = QPolygon([
                QPoint(x, y + int(h * 0.3)), QPoint(x + w // 2, y + int(h * 0.3)), QPoint(x + w // 2, y),
                QPoint(x + w, y + h // 2), QPoint(x + w // 2, y + h), QPoint(x + w // 2, y + int(h * 0.7)),
                QPoint(x, y + int(h * 0.7))
            ])
            painter.drawPolygon(points)

        elif shape_num == "13":
            points = QPolygon([
                QPoint(x + w, y + int(h * 0.3)), QPoint(x + w // 2, y + int(h * 0.3)), QPoint(x + w // 2, y),
                QPoint(x, y + h // 2), QPoint(x + w // 2, y + h), QPoint(x + w // 2, y + int(h * 0.7)),
                QPoint(x + w, y + int(h * 0.7))
            ])
            painter.drawPolygon(points)

        elif shape_num == "14":
            points = QPolygon([
                QPoint(x + w // 2, y), QPoint(x + w, y + h // 2), QPoint(x + int(w * 0.7), y + h // 2),
                QPoint(x + int(w * 0.7), y + h), QPoint(x + int(w * 0.3), y + h), QPoint(x + int(w * 0.3), y + h // 2),
                QPoint(x, y + h // 2)
            ])
            painter.drawPolygon(points)

        elif shape_num == "15":
            points = QPolygon([
                QPoint(x + int(w * 0.3), y), QPoint(x + int(w * 0.7), y), QPoint(x + int(w * 0.7), y + h // 2),
                QPoint(x + w, y + h // 2), QPoint(x + w // 2, y + h), QPoint(x, y + h // 2),
                QPoint(x + int(w * 0.3), y + h // 2)
            ])
            painter.drawPolygon(points)

        elif shape_num == "16":
            cx, cy = x + w // 2, y + h // 2
            points = QPolygon([
                QPoint(cx, y), QPoint(cx + int(w * 0.1), cy - int(h * 0.1)), QPoint(x + w, cy),
                QPoint(cx + int(w * 0.1), cy + int(h * 0.1)),
                QPoint(cx, y + h), QPoint(cx - int(w * 0.1), cy + int(h * 0.1)), QPoint(x, cy),
                QPoint(cx - int(w * 0.1), cy - int(h * 0.1))
            ])
            painter.drawPolygon(points)

        elif shape_num == "17":
            cx, cy = x + w // 2, y + h // 2
            pts = []
            for i in range(10):
                r = (w // 2) if i % 2 == 0 else (w // 4)
                angle = i * math.pi / 5 - math.pi / 2
                pts.append(QPoint(int(cx + r * math.cos(angle)), int(cy + r * math.sin(angle))))
            painter.drawPolygon(QPolygon(pts))

        elif shape_num == "18":
            cx, cy = x + w // 2, y + h // 2
            pts = []
            for i in range(12):
                r = (w // 2) if i % 2 == 0 else (w // 3)
                angle = i * math.pi / 6 - math.pi / 2
                pts.append(QPoint(int(cx + r * math.cos(angle)), int(cy + r * math.sin(angle))))
            painter.drawPolygon(QPolygon(pts))

        elif shape_num == "19":
            painter.drawRoundedRect(x, y + int(h * 0.2), w, int(h * 0.6), 10, 10)
            painter.drawPolygon(QPolygon([QPoint(x + int(w * 0.2), y + int(h * 0.8)), QPoint(x + int(w * 0.1), y + h),
                                          QPoint(x + int(w * 0.3), y + int(h * 0.8))]))

        elif shape_num == "20":
            tail = QPolygon([
                QPoint(x + int(w * 0.25), y + int(h * 0.65)),
                QPoint(x + int(w * 0.15), y + h),
                QPoint(x + int(w * 0.45), y + int(h * 0.65))
            ])
            painter.drawPolygon(tail)

            painter.drawEllipse(x, y, w, int(h * 0.75))

        elif shape_num == "21":
            path = QPainterPath()
            path.moveTo(x + int(w * 0.2), y + int(h * 0.3))
            path.quadTo(x + int(w * 0.25), y + int(h * 0.1), x + int(w * 0.5), y + int(h * 0.15))
            path.quadTo(x + int(w * 0.75), y + int(h * 0.05), x + int(w * 0.8), y + int(h * 0.3))
            path.quadTo(x + int(w * 0.98), y + int(h * 0.4), x + int(w * 0.85), y + int(h * 0.6))
            path.quadTo(x + int(w * 0.75), y + int(h * 0.8), x + int(w * 0.5), y + int(h * 0.75))
            path.quadTo(x + int(w * 0.25), y + int(h * 0.85), x + int(w * 0.15), y + int(h * 0.6))
            path.quadTo(x + int(w * 0.02), y + int(h * 0.4), x + int(w * 0.2), y + int(h * 0.3))
            painter.drawPath(path)

            painter.drawEllipse(x + int(w * 0.12), y + int(h * 0.82), int(w * 0.08), int(h * 0.08))
            painter.drawEllipse(x + int(w * 0.05), y + int(h * 0.92), int(w * 0.05), int(h * 0.05))

        elif shape_num == "22":
            path = QPainterPath()
            top_center = QPointF(x + w / 2, y + h * 0.25)
            bottom_center = QPointF(x + w / 2, y + h)

            path.moveTo(top_center)
            path.cubicTo(QPointF(x + w * 0.2, y - h * 0.1), QPointF(x - w * 0.1, y + h * 0.45), bottom_center)
            path.cubicTo(QPointF(x + w + w * 0.1, y + h * 0.45), QPointF(x + w * 0.8, y - h * 0.1), top_center)

            painter.drawPath(path)


        elif shape_num == "23":
            points = QPolygon([
                QPoint(x + int(w * 0.6), y), QPoint(x, y + int(h * 0.55)), QPoint(x + int(w * 0.45), y + int(h * 0.55)),
                QPoint(x + int(w * 0.35), y + h), QPoint(x + w, y + int(h * 0.4)),
                QPoint(x + int(w * 0.55), y + int(h * 0.4))
            ])
            painter.drawPolygon(points)

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