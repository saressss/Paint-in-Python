import sys
from PyQt6.QtWidgets import (QApplication, QDialog, QWidget, QLabel,
                             QLineEdit, QComboBox, QPushButton,
                             QGridLayout, QHBoxLayout, QVBoxLayout)
from PyQt6.QtGui import QColor, QPainter, QLinearGradient, QMouseEvent, QPixmap, QImage
from PyQt6.QtCore import Qt, pyqtSignal
from classes import radialColorButton

class ColorSpectrumWidget(QLabel):
    colorChanged = pyqtSignal(QColor)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setMinimumSize(250, 250)
        self.pixmap_canvas = QPixmap()
        self.image_canvas = QImage()

    def resizeEvent(self, event):
        super().resizeEvent(event)

        pixmap = QPixmap(self.size())
        painter = QPainter(pixmap)

        hue_gradient = QLinearGradient(0, 0, self.width(), 0)
        hue_gradient.setColorAt(0.0, QColor(255, 0, 0))
        hue_gradient.setColorAt(0.16, QColor(255, 255, 0))
        hue_gradient.setColorAt(0.33, QColor(0, 255, 0))
        hue_gradient.setColorAt(0.5, QColor(0, 255, 255))
        hue_gradient.setColorAt(0.66, QColor(0, 0, 255))
        hue_gradient.setColorAt(0.83, QColor(255, 0, 255))
        hue_gradient.setColorAt(1.0, QColor(255, 0, 0))
        painter.fillRect(self.rect(), hue_gradient)

        val_gradient = QLinearGradient(0, 0, 0, self.height())
        val_gradient.setColorAt(0.0, QColor(0, 0, 0, 0))
        val_gradient.setColorAt(1.0, QColor(0, 0, 0, 255))
        painter.fillRect(self.rect(), val_gradient)

        painter.end()

        self.pixmap_canvas = pixmap
        self.image_canvas = pixmap.toImage()
        self.setPixmap(self.pixmap_canvas)

    def handle_mouse_color(self, pos):
        if self.rect().contains(pos):
            color = self.image_canvas.pixelColor(pos)
            if color.isValid():
                self.colorChanged.emit(color)

    def mousePressEvent(self, event: QMouseEvent):
        if event.button() == Qt.MouseButton.LeftButton:
            self.handle_mouse_color(event.position().toPoint())

    def mouseMoveEvent(self, event: QMouseEvent):
        if event.buttons() == Qt.MouseButton.LeftButton:
            self.handle_mouse_color(event.position().toPoint())


class EditPaletteDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Редагувати палітру")
        self.setFixedSize(650, 550)

        self.setStyleSheet("""
            QDialog { background-color: #1e1e1e; }
            QLineEdit { background-color: #2d2d2d; color: white; border: 1px solid #3e3e3e; padding: 4px; border-radius: 4px; }
            QComboBox { background-color: #2d2d2d; color: white; border: 1px solid #3e3e3e; border-radius: 4px; padding: 4px; }
            QPushButton { background-color: #3a3a3a; color: white; border: 1px solid #555555; padding: 6px 15px; border-radius: 4px; }
            QPushButton:hover { background-color: #4a4a4a; }
            QPushButton#okButton { background-color: #2b5b84; }
        """)

        self.init_ui()

    def init_ui(self):
        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(20, 20, 20, 20)
        main_layout.setSpacing(20)

        title_label = QLabel("Редагувати палітру")
        title_label.setStyleSheet("font-size: 18px; font-weight: bold; color: white;")
        main_layout.addWidget(title_label)

        top_layout = QHBoxLayout()
        top_layout.setSpacing(15)

        self.spectrum = ColorSpectrumWidget()
        self.spectrum.colorChanged.connect(self.update_fields)
        top_layout.addWidget(self.spectrum, stretch=2)

        self.brightness_slider = QWidget()
        self.brightness_slider.setFixedWidth(20)
        self.brightness_slider.setStyleSheet("""
            background: qlineargradient(x1:0, y1:0, x2:0, y2:1, 
                                        stop:0 #ffffff, stop:1 #000000);
            border-radius: 10px;
        """)
        top_layout.addWidget(self.brightness_slider)
        fields_layout = QVBoxLayout()
        fields_layout.setSpacing(10)

        self.hex_input = QLineEdit("#000000")
        fields_layout.addWidget(self.hex_input)

        self.rgbLayout = QLabel()
        self.rgbLayout.setText("RGB")
        fields_layout.addWidget(self.rgbLayout)

        self.rgb_inputs = {}
        colors_labels = [("R", "Червоний"), ("G", "Зелений"), ("B", "Синій")]

        for key, label_text in colors_labels:
            row_layout = QHBoxLayout()
            num_input = QLineEdit("0")
            num_input.setFixedWidth(80)

            lbl = QLabel(label_text)
            lbl.setStyleSheet("color: #b3b3b3;")

            row_layout.addWidget(num_input)
            row_layout.addWidget(lbl)
            fields_layout.addLayout(row_layout)

            self.rgb_inputs[key] = num_input

        self.HorizontalLayout = QHBoxLayout()
        main_layout.addLayout(self.HorizontalLayout)

        self.colorButton = radialColorButton()
        self.HorizontalLayout.addWidget(self.colorButton)
        fields_layout.addStretch()
        top_layout.addLayout(fields_layout, stretch=1)
        main_layout.addLayout(top_layout)

        bottom_buttons = QHBoxLayout()
        ok_btn = QPushButton("OK")
        ok_btn.setObjectName("okButton")
        cancel_btn = QPushButton("Скасувати")
        cancel_btn.clicked.connect(self.reject)

        ok_btn.clicked.connect(self.accept)
        cancel_btn.clicked.connect(self.reject)

        bottom_buttons.addWidget(ok_btn)
        bottom_buttons.addWidget(cancel_btn)
        main_layout.addLayout(bottom_buttons)

    def get_selected_color(self):
        return self.currentColor

    def update_fields(self, color: QColor):
        self.hex_input.setText(color.name().upper())
        self.currentColor = color.name()
        self.colorButton.colorChange(color.name())
        self.rgb_inputs["R"].setText(str(color.red()))
        self.rgb_inputs["G"].setText(str(color.green()))
        self.rgb_inputs["B"].setText(str(color.blue()))

        self.brightness_slider.setStyleSheet(f"""
            background: qlineargradient(x1:0, y1:0, x2:0, y2:1, 
                                        stop:0 {color.name()}, stop:1 #000000);
            border-radius: 10px;
        """)