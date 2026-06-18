import sys
from PyQt6 import QtCore
from PyQt6.QtCore import QTimer
from classes import *
from RadialColorMenu import EditPaletteDialog

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("Paint")
        MainWindow.resize(1920, 1080)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)

        self.gridLayoutWidget = QtWidgets.QWidget(parent=self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 10, 26, 210))
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(2, 2, 2, 2)

        self.gridLayoutWidget_4 = QtWidgets.QWidget(parent=self.centralwidget)
        self.gridLayoutWidget_4.setGeometry(QtCore.QRect(46, 10, 26, 210))
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

        self.canvas = CanvasWidget(parent=self.centralwidget)
        self.canvas.setGeometry(QtCore.QRect(0, 230, 1920, 1000))

        self.colorShow_Choose = radialColorButton(parent=self.centralwidget)
        self.colorShow_Choose.setGeometry(QtCore.QRect(90, 40, 60, 60))
        self.colorShow_Choose.pressed.connect(self.open_ColorRadialMenu)

        self.colorShow_Choose1 = radialColorButton(parent=self.centralwidget)
        self.colorShow_Choose1.setGeometry(QtCore.QRect(90, 100, 60, 60))
        self.colorShow_Choose1.pressed.connect(self.open_ColorRadialMenu1)

        self.verticalLayoutWidget = QtWidgets.QWidget(parent=self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(260, 0, 330, 200))

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

        self.gridLayoutWidget_3 = QtWidgets.QWidget(parent=self.centralwidget)
        self.gridLayoutWidget_3.setGeometry(QtCore.QRect(1100, 0, 271, 201))
        self.gridLayoutWidget_3.setObjectName("gridLayoutWidget_3")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.gridLayoutWidget_3)
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_5.setObjectName("gridLayout_5")

        self.horizontalLayoutWidget = QtWidgets.QWidget(parent=self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(570, 0, 161, 91))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.pushButton_2 = QtWidgets.QPushButton(parent=self.horizontalLayoutWidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_3.addWidget(self.pushButton_2)
        self.pushButton = QtWidgets.QPushButton(parent=self.horizontalLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_3.addWidget(self.pushButton)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1747, 21))
        self.menubar.setObjectName("menubar")
        self.menuPaint = QtWidgets.QMenu(parent=self.menubar)
        self.menuPaint.setObjectName("menuPaint")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuPaint.menuAction())

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

    def Update(self):
        self.canvas.pen1 = QPen(QColor(self.secondaryColor), self.widthSlide.value(), Qt.PenStyle.SolidLine, Qt.PenCapStyle.RoundCap, Qt.PenJoinStyle.RoundJoin)
        self.canvas.pen = QPen(QColor(self.primaryColor), self.widthSlide.value(), Qt.PenStyle.SolidLine, Qt.PenCapStyle.RoundCap, Qt.PenJoinStyle.RoundJoin)
        self.colorShow_Choose.colorChange(self.primaryColor)
        self.colorShow_Choose1.colorChange(self.secondaryColor)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
