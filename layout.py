import sys
from PyQt6 import QtCore, QtWidgets
from PyQt6.QtCore import QTimer
from pen_base import *

options_dict =  {
    1: "black",
    2: "blue",
    3: "red",
    4: "green",
    5: "yellow",
    6: "orange",
    7: "pink",
    8: "purple",
    9: "cyan",
    10: "DarkBlue",
    11: "brown",
    12: "DarkGoldenRod",
    13: "DeepPink",
    14: "grey",
    15: "Coral",
    16: "DarkOrange"
}

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("Paint")
        MainWindow.resize(1920, 1080)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.gridLayoutWidget = QtWidgets.QWidget(parent=self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 0, 121, 201))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")

        self.gridLayoutWidget_4 = QtWidgets.QWidget(parent=self.centralwidget)
        self.gridLayoutWidget_4.setGeometry(QtCore.QRect(120, 0, 121, 201))
        self.gridLayoutWidget_4.setObjectName("gridLayoutWidget_4")

        self.gridLayout_6 = QtWidgets.QGridLayout(self.gridLayoutWidget_4)
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_6.setObjectName("gridLayout_6")

        self.key = 1

        self.color_swap_1 = QtWidgets.QPushButton(parent=self.gridLayoutWidget)
        self.gridLayout.addWidget(self.color_swap_1, 0, 0, 1, 1)
        self.color_swap_1.setStyleSheet("background-color: black;")
        self.color_swap_1.pressed.connect(lambda: setattr(self, 'key', 1))

        self.color_swap_2 = QtWidgets.QPushButton(parent=self.gridLayoutWidget)
        self.gridLayout.addWidget(self.color_swap_2, 1, 0, 1, 1)
        self.color_swap_2.pressed.connect(lambda: setattr(self, 'key', 2))
        self.color_swap_2.setStyleSheet("background-color: blue;")

        self.color_swap_3 = QtWidgets.QPushButton(parent=self.gridLayoutWidget)
        self.gridLayout.addWidget(self.color_swap_3, 2, 0, 1, 1)
        self.color_swap_3.pressed.connect(lambda: setattr(self, 'key', 3))
        self.color_swap_3.setStyleSheet("background-color: red;")

        self.color_swap_4 = QtWidgets.QPushButton(parent=self.gridLayoutWidget)
        self.gridLayout.addWidget(self.color_swap_4, 3, 0, 1, 1)
        self.color_swap_4.pressed.connect(lambda: setattr(self, 'key', 4))
        self.color_swap_4.setStyleSheet("background-color: green;")

        self.color_swap_5 = QtWidgets.QPushButton(parent=self.gridLayoutWidget)
        self.gridLayout.addWidget(self.color_swap_5, 4, 0, 1, 1)
        self.color_swap_5.pressed.connect(lambda: setattr(self, 'key', 5))
        self.color_swap_5.setStyleSheet("background-color: yellow;")

        self.color_swap_6 = QtWidgets.QPushButton(parent=self.gridLayoutWidget)
        self.gridLayout.addWidget(self.color_swap_6, 5, 0, 1, 1)
        self.color_swap_6.pressed.connect(lambda: setattr(self, 'key', 6))
        self.color_swap_6.setStyleSheet("background-color: orange;")

        self.color_swap_7 = QtWidgets.QPushButton(parent=self.gridLayoutWidget)
        self.gridLayout.addWidget(self.color_swap_7, 6, 0, 1, 1)
        self.color_swap_7.pressed.connect(lambda: setattr(self, 'key', 7))
        self.color_swap_7.setStyleSheet("background-color: pink;")

        self.color_swap_8 = QtWidgets.QPushButton(parent=self.gridLayoutWidget)
        self.gridLayout.addWidget(self.color_swap_8, 7, 0, 1, 1)
        self.color_swap_8.pressed.connect(lambda: setattr(self, 'key', 8))
        self.color_swap_8.setStyleSheet("background-color: purple;")

        self.color_swap_9 = QtWidgets.QPushButton(parent=self.gridLayoutWidget_4)
        self.gridLayout_6.addWidget(self.color_swap_9, 0, 0, 1, 1)
        self.color_swap_9.pressed.connect(lambda: setattr(self, 'key', 9))
        self.color_swap_9.setStyleSheet("background-color: cyan;")

        self.color_swap_10 = QtWidgets.QPushButton(parent=self.gridLayoutWidget_4)
        self.gridLayout_6.addWidget(self.color_swap_10, 1, 0, 1, 1)
        self.color_swap_10.pressed.connect(lambda: setattr(self, 'key', 10))
        self.color_swap_10.setStyleSheet("background-color: DarkBlue;")

        self.color_swap_11 = QtWidgets.QPushButton(parent=self.gridLayoutWidget_4)
        self.gridLayout_6.addWidget(self.color_swap_11, 2, 0, 1, 1)
        self.color_swap_11.pressed.connect(lambda: setattr(self, 'key', 11))
        self.color_swap_11.setStyleSheet("background-color: brown;")

        self.color_swap_12 = QtWidgets.QPushButton(parent=self.gridLayoutWidget_4)
        self.gridLayout_6.addWidget(self.color_swap_12, 3, 0, 1, 1)
        self.color_swap_12.pressed.connect(lambda: setattr(self, 'key', 12))
        self.color_swap_12.setStyleSheet("background-color: DarkGoldenRod;")

        self.color_swap_13 = QtWidgets.QPushButton(parent=self.gridLayoutWidget_4)
        self.gridLayout_6.addWidget(self.color_swap_13, 4, 0, 1, 1)
        self.color_swap_13.pressed.connect(lambda: setattr(self, 'key', 13))
        self.color_swap_13.setStyleSheet("background-color: DeepPink;")

        self.color_swap_14 = QtWidgets.QPushButton(parent=self.gridLayoutWidget_4)
        self.gridLayout_6.addWidget(self.color_swap_14, 5, 0, 1, 1)
        self.color_swap_14.pressed.connect(lambda: setattr(self, 'key', 14))
        self.color_swap_14.setStyleSheet("background-color: grey;")

        self.color_swap_15 = QtWidgets.QPushButton(parent=self.gridLayoutWidget_4)
        self.gridLayout_6.addWidget(self.color_swap_15, 6, 0, 1, 1)
        self.color_swap_15.pressed.connect(lambda: setattr(self, 'key', 15))
        self.color_swap_15.setStyleSheet("background-color: Coral;")

        self.color_swap_16 = QtWidgets.QPushButton(parent=self.gridLayoutWidget_4)
        self.gridLayout_6.addWidget(self.color_swap_16, 7, 0, 1, 1)
        self.color_swap_16.pressed.connect(lambda: setattr(self, 'key', 16))
        self.color_swap_16.setStyleSheet("background-color: DarkOrange;")

        self.canvas = CanvasWidget(parent=self.centralwidget)
        self.canvas.setGeometry(QtCore.QRect(0, 230, 1920, 1000))
        self.canvas.setText("")

        self.verticalLayoutWidget = QtWidgets.QWidget(parent=self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(240, 0, 331, 201))

        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)

        self.width = QtWidgets.QLabel(parent=self.verticalLayoutWidget)
        self.width.setText("Width")
        self.verticalLayout.addWidget(self.width)

        self.widthSlide = QtWidgets.QSlider(parent=self.verticalLayoutWidget)
        self.widthSlide.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.widthSlide.setMinimum(1)
        self.widthSlide.setMaximum(100)
        self.verticalLayout.addWidget(self.widthSlide)

        self.opacity = QtWidgets.QLabel(parent=self.verticalLayoutWidget)
        self.opacity.setText("Opacity")
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
        self.timer.timeout.connect(self.PenUpdate)
        self.timer.start(10)

    def PenUpdate(self):
        self.canvas.pen = QPen(QColor(options_dict[self.key]), self.widthSlide.value())


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
