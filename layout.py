import sys
from PyQt6 import QtCore
from PyQt6.QtCore import QTimer
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QScrollArea, QFileDialog, QMessageBox
from classes import *
from RadialColorMenu import EditPaletteDialog
from functional_buttons import functionalButton


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("Paint")
        MainWindow.resize(1920, 1080)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)

        self.gridLayoutWidget = QtWidgets.QWidget(parent=self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 20, 26, 210))
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(2, 2, 2, 2)

        self.gridLayoutWidget_4 = QtWidgets.QWidget(parent=self.centralwidget)
        self.gridLayoutWidget_4.setGeometry(QtCore.QRect(46, 20, 26, 210))
        self.gridLayout_6 = QtWidgets.QGridLayout(self.gridLayoutWidget_4)
        self.gridLayout_6.setContentsMargins(2, 2, 2, 2)

        self.radialMenu = None
        self.primaryColor = "black"
        self.secondaryColor = "black"

        self.color_swap_1 = ColorButton(parent=self.gridLayoutWidget, color="black")
        self.gridLayout.addWidget(self.color_swap_1, 0, 0, 1, 1)
        self.color_swap_1.pressed.connect(lambda: setattr(self, 'primaryColor', "black"))

        self.color_swap_2 = ColorButton(parent=self.gridLayoutWidget, color="blue")
        self.gridLayout.addWidget(self.color_swap_2, 1, 0, 1, 1)
        self.color_swap_2.pressed.connect(lambda: setattr(self, 'primaryColor', "blue"))

        self.color_swap_3 = ColorButton(parent=self.gridLayoutWidget, color="red")
        self.gridLayout.addWidget(self.color_swap_3, 2, 0, 1, 1)
        self.color_swap_3.pressed.connect(lambda: setattr(self, 'primaryColor', "red"))

        self.color_swap_4 = ColorButton(parent=self.gridLayoutWidget, color="green")
        self.gridLayout.addWidget(self.color_swap_4, 3, 0, 1, 1)
        self.color_swap_4.pressed.connect(lambda: setattr(self, 'primaryColor', "green"))

        self.color_swap_5 = ColorButton(parent=self.gridLayoutWidget, color="yellow")
        self.gridLayout.addWidget(self.color_swap_5, 4, 0, 1, 1)
        self.color_swap_5.pressed.connect(lambda: setattr(self, 'primaryColor', "yellow"))

        self.color_swap_6 = ColorButton(parent=self.gridLayoutWidget, color="orange")
        self.gridLayout.addWidget(self.color_swap_6, 5, 0, 1, 1)
        self.color_swap_6.pressed.connect(lambda: setattr(self, 'primaryColor', "orange"))

        self.color_swap_7 = ColorButton(parent=self.gridLayoutWidget, color="pink")
        self.gridLayout.addWidget(self.color_swap_7, 6, 0, 1, 1)
        self.color_swap_7.pressed.connect(lambda: setattr(self, 'primaryColor', "pink"))

        self.color_swap_8 = ColorButton(parent=self.gridLayoutWidget, color="purple")
        self.gridLayout.addWidget(self.color_swap_8, 7, 0, 1, 1)
        self.color_swap_8.pressed.connect(lambda: setattr(self, 'primaryColor', "purple"))

        self.color_swap_9 = ColorButton(parent=self.gridLayoutWidget_4, color="cyan")
        self.gridLayout_6.addWidget(self.color_swap_9, 0, 0, 1, 1)
        self.color_swap_9.pressed.connect(lambda: setattr(self, 'primaryColor', "cyan"))

        self.color_swap_10 = ColorButton(parent=self.gridLayoutWidget_4, color="DarkBlue")
        self.gridLayout_6.addWidget(self.color_swap_10, 1, 0, 1, 1)
        self.color_swap_10.pressed.connect(lambda: setattr(self, 'primaryColor', "DarkBlue"))

        self.color_swap_11 = ColorButton(parent=self.gridLayoutWidget_4, color="brown")
        self.gridLayout_6.addWidget(self.color_swap_11, 2, 0, 1, 1)
        self.color_swap_11.pressed.connect(lambda: setattr(self, 'primaryColor', "brown"))

        self.color_swap_12 = ColorButton(parent=self.gridLayoutWidget_4, color="DarkGoldenRod")
        self.gridLayout_6.addWidget(self.color_swap_12, 3, 0, 1, 1)
        self.color_swap_12.pressed.connect(lambda: setattr(self, 'primaryColor', "DarkGoldenRod"))

        self.color_swap_13 = ColorButton(parent=self.gridLayoutWidget_4, color="DeepPink")
        self.gridLayout_6.addWidget(self.color_swap_13, 4, 0, 1, 1)
        self.color_swap_13.pressed.connect(lambda: setattr(self, 'primaryColor', "DeepPink"))

        self.color_swap_14 = ColorButton(parent=self.gridLayoutWidget_4, color="grey")
        self.gridLayout_6.addWidget(self.color_swap_14, 5, 0, 1, 1)
        self.color_swap_14.pressed.connect(lambda: setattr(self, 'primaryColor', "grey"))

        self.color_swap_15 = ColorButton(parent=self.gridLayoutWidget_4, color="Coral")
        self.gridLayout_6.addWidget(self.color_swap_15, 6, 0, 1, 1)
        self.color_swap_15.pressed.connect(lambda: setattr(self, 'primaryColor', "Coral"))

        self.color_swap_16 = ColorButton(parent=self.gridLayoutWidget_4, color="DarkOrange")
        self.gridLayout_6.addWidget(self.color_swap_16, 7, 0, 1, 1)
        self.color_swap_16.pressed.connect(lambda: setattr(self, 'primaryColor', "DarkOrange"))

        self.scroll_area = QScrollArea(parent=self.centralwidget)
        self.scroll_area.setGeometry(QtCore.QRect(0, 230, 1920, 800))
        self.scroll_area.setWidgetResizable(False)

        self.canvas = CanvasWidget(parent=self.scroll_area, option="pencil", main=self)
        self.scroll_area.setWidget(self.canvas)

        self.colorShow_Choose = radialColorButton(parent=self.centralwidget)
        self.colorShow_Choose.setGeometry(QtCore.QRect(90, 40, 60, 60))
        self.colorShow_Choose.pressed.connect(self.open_ColorRadialMenu)

        self.colorShow_Choose1 = radialColorButton(parent=self.centralwidget)
        self.colorShow_Choose1.setGeometry(QtCore.QRect(90, 120, 60, 60))
        self.colorShow_Choose1.pressed.connect(self.open_ColorRadialMenu1)

        self.brushComboBox = QtWidgets.QComboBox(parent=self.centralwidget)
        self.brushComboBox.setGeometry(QtCore.QRect(180, 90, 200, 30))

        self.brushComboBox.addItems([
            "Пензель",
            "Каліграфічний пензель",
            "Каліграфічне перо",
            "Розпилювач",
            "Пензель для олії",
            "Пастель",
            "Маркер",
            "Звичайний олівець",
        ])

        self.brushComboBox.setStyleSheet("""
                    QComboBox {
                        background-color: #2d2d2d;
                        color: white;
                        border: 1px solid #3e3e3e;
                        border-radius: 4px;
                        padding-left: 6px;
                        font-family: Arial;
                        font-size: 12px;
                    }
                    QComboBox QAbstractItemView {
                        background-color: #2d2d2d;
                        color: white;
                        selection-background-color: #2b5b84;
                    }
                """)

        self.brushComboBox.currentTextChanged.connect(self.canvas.set_brush_style)

        self.verticalLayoutWidget = QtWidgets.QWidget(parent=self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(400, 0, 330, 200))

        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(10, 0, 10, 10)

        self.width = sliders(parent=self.verticalLayoutWidget, text="Width")
        self.verticalLayout.addWidget(self.width)

        self.widthSlide = QtWidgets.QSlider(parent=self.verticalLayoutWidget)
        self.widthSlide.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.widthSlide.setMinimum(1)
        self.widthSlide.setMaximum(100)
        self.verticalLayout.addWidget(self.widthSlide)

        self.opacity = sliders(parent=self.verticalLayoutWidget, text="Opacity")
        self.verticalLayout.addWidget(self.opacity)

        self.opacitySlider = QtWidgets.QSlider(parent=self.verticalLayoutWidget)
        self.opacitySlider.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.verticalLayout.addWidget(self.opacitySlider)
        self.opacitySlider.setMinimum(1)
        self.opacitySlider.setMaximum(255)
        self.opacitySlider.setValue(255)

        self.gridLayoutWidget_3 = QtWidgets.QWidget(parent=self.centralwidget)
        self.gridLayoutWidget_3.setGeometry(QtCore.QRect(750, 20, 270, 200))
        self.gridLayoutWidget_3.setObjectName("gridLayoutWidget_3")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.gridLayoutWidget_3)
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)

        self.funcButton1 = functionalButton(option="pencil", icon="pencil.jpg")
        self.gridLayout_5.addWidget(self.funcButton1, 0, 0, 1, 1)
        self.funcButton2 = functionalButton(option="glass", icon="glass.png")
        self.gridLayout_5.addWidget(self.funcButton2, 1, 0, 1, 1)
        self.funcButton3 = functionalButton(option="pipette", icon="pipiette.png")
        self.gridLayout_5.addWidget(self.funcButton3, 2, 0, 1, 1)
        self.funcButton4 = functionalButton(option="rubber", icon="rubber.png")
        self.gridLayout_5.addWidget(self.funcButton4, 0, 1, 1, 1)
        self.funcButton5 = functionalButton(option="floodfill", icon="floodfill.png")
        self.gridLayout_5.addWidget(self.funcButton5, 1, 1, 1, 1)
        self.funcButton6 = functionalButton(option="text", icon="text.png")
        self.gridLayout_5.addWidget(self.funcButton6, 2, 1, 1, 1)

        self.funcButton1.pressed.connect(lambda: self.canvas.set_tool("instrument","pencil"))
        self.funcButton2.pressed.connect(lambda: self.canvas.set_tool("instrument","glass"))
        self.funcButton3.pressed.connect(lambda: self.canvas.set_tool("instrument","pipette"))
        self.funcButton4.pressed.connect(lambda: self.canvas.set_tool("instrument","rubber"))
        self.funcButton5.pressed.connect(lambda: self.canvas.set_tool("instrument","floodfill"))
        self.funcButton6.pressed.connect(lambda: self.canvas.set_tool("instrument","text"))

        self.scroll =  QtWidgets.QScrollArea(parent=self.centralwidget)
        self.scroll.setGeometry(QtCore.QRect(1050, 20, 300, 200))
        self.scroll.setFixedWidth(300)
        self.gridLayoutWidget1 = QtWidgets.QGridLayout(parent=self.scroll)
        self.gridLayoutWidget1.setContentsMargins(5, 5, 5, 5)
        self.gridLayoutWidget1.setSpacing(5)

        self.iconArray = [
            QIcon("iconsDraw/line.png"),QIcon("iconsDraw/curve.png"),QIcon("iconsDraw/circle.png"),QIcon("iconsDraw/square.png"),QIcon("iconsDraw/roundSquare.png"),QIcon("iconsDraw/choose.png"),
            QIcon("iconsDraw/triangle.png"), QIcon("iconsDraw/righttriangle.png"), QIcon("iconsDraw/diamond.png"), QIcon("iconsDraw/pentagon.png"), QIcon("iconsDraw/hexagon.png"), QIcon("iconsDraw/arrowR.png"),
            QIcon("iconsDraw/arrowL.png"), QIcon("iconsDraw/arrowU.png"), QIcon("iconsDraw/arrowD.png"), QIcon("iconsDraw/star4.png"), QIcon("iconsDraw/star.png"), QIcon("iconsDraw/star6.png"),
            QIcon("iconsDraw/chat_Bublble.png"), QIcon("iconsDraw/cloudRound.png"), QIcon("iconsDraw/cloud.png"), QIcon("iconsDraw/favorite.png"), QIcon("iconsDraw/bolt.png"),
        ]

        j = -1
        for i in range(23):
            btn = QtWidgets.QPushButton()
            btn.setFixedSize(48, 48)

            btn.setIconSize(QtCore.QSize(44, 44))
            btn.setIcon(self.iconArray[i])
            btn.pressed.connect(lambda checked=False, idx=i: self.canvas.set_tool("shape", f"{idx+1}"))

            if(i%6 == 0):
                j += 1

            self.gridLayoutWidget1.addWidget(btn, j, i%6, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.timer = QTimer()
        self.timer.timeout.connect(self.Update)
        self.timer.start(10)

    def open_ColorRadialMenu(self):
        dialog = EditPaletteDialog()
        if dialog.exec():
            chosen_color = dialog.get_selected_color()
            self.primaryColor = chosen_color

    def open_ColorRadialMenu1(self):
        dialog = EditPaletteDialog()
        if dialog.exec():
            chosen_color = dialog.get_selected_color()
            self.secondaryColor = chosen_color

    def closeEvent(self, event):
        main_win = self.centralwidget.window()

        reply = QMessageBox.question(
            main_win,
            "Вихід з програми",
            "У вас є незбережені зміни. Бажаєте зберегти малюнок перед виходом?",
            QMessageBox.StandardButton.Save |
            QMessageBox.StandardButton.Discard |
            QMessageBox.StandardButton.Cancel
        )

        if reply == QMessageBox.StandardButton.Save:
            file_path, _ = QFileDialog.getSaveFileName(
                main_win,
                caption="Зберегти малюнок перед виходом",
                directory="canvas_image.png",
                filter="PNG Files (*.png);;All Files (*)"
            )

            if file_path:
                if hasattr(self.canvas, 'save_to_png'):
                    saved = self.canvas.save_to_png(file_path)
                else:
                    saved = self.canvas.canvas.save(file_path, "PNG")

                if saved:
                    event.accept()
                else:
                    QMessageBox.warning(main_win, "Помилка", "Не вдалося зберегти файл.")
                    event.ignore()
            else:
                event.ignore()
        elif reply == QMessageBox.StandardButton.Discard:
            event.accept()
        else:
            event.ignore()


    def Update(self):

        color_Op_pr = QColor(QColor(self.primaryColor).red(), QColor(self.primaryColor).green(), QColor(self.primaryColor).blue(), self.opacitySlider.value())
        color_Op_se = QColor(QColor(self.secondaryColor).red(), QColor(self.secondaryColor).green(),QColor(self.secondaryColor).blue(), self.opacitySlider.value())

        self.canvas.pen1 = QPen(color_Op_se, self.widthSlide.value(), Qt.PenStyle.SolidLine)
        self.canvas.pen = QPen(color_Op_pr, self.widthSlide.value(), Qt.PenStyle.SolidLine)
        self.colorShow_Choose.colorChange(self.primaryColor)
        self.colorShow_Choose1.colorChange(self.secondaryColor)

    def change_primary_color(self, color_name):
        self.primaryColor = color_name

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)

    MainWindow.closeEvent = ui.closeEvent
    MainWindow.show()
    sys.exit(app.exec())
