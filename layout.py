import sys
from PyQt6 import QtCore, QtWidgets
from PyQt6.QtCore import QTimer
from classes import *

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
        self.centralwidget.setStyleSheet("background-color:black")

        self.gridLayoutWidget = QtWidgets.QWidget(parent=self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 0, 120, 200))
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(2, 2, 2, 2)

        self.gridLayoutWidget_4 = QtWidgets.QWidget(parent=self.centralwidget)
        self.gridLayoutWidget_4.setGeometry(QtCore.QRect(120, 0, 120, 200))
        self.gridLayout_6 = QtWidgets.QGridLayout(self.gridLayoutWidget_4)
        self.gridLayout_6.setContentsMargins(2, 2, 2, 2)

        self.key = 1

        self.color_swap_1 = ColorButton(parent=self.gridLayoutWidget, color="black", key=1)
        self.gridLayout.addWidget(self.color_swap_1, 0, 0, 1, 1)

        self.color_swap_2 = ColorButton(parent=self.gridLayoutWidget, color="blue", key=2)
        self.gridLayout.addWidget(self.color_swap_2, 1, 0, 1, 1)

        self.color_swap_3 = ColorButton(parent=self.gridLayoutWidget, color="red", key=3)
        self.gridLayout.addWidget(self.color_swap_3, 2, 0, 1, 1)

        self.color_swap_4 = ColorButton(parent=self.gridLayoutWidget, color="green", key=4)
        self.gridLayout.addWidget(self.color_swap_4, 3, 0, 1, 1)

        self.color_swap_5 = ColorButton(parent=self.gridLayoutWidget, color="yellow", key=5)
        self.gridLayout.addWidget(self.color_swap_5, 4, 0, 1, 1)

        self.color_swap_6 = ColorButton(parent=self.gridLayoutWidget, color="orange", key=6)
        self.gridLayout.addWidget(self.color_swap_6, 5, 0, 1, 1)

        self.color_swap_7 = ColorButton(parent=self.gridLayoutWidget, color="pink", key=7)
        self.gridLayout.addWidget(self.color_swap_7, 6, 0, 1, 1)

        self.color_swap_8 = ColorButton(parent=self.gridLayoutWidget, color="purple", key=8)
        self.gridLayout.addWidget(self.color_swap_8, 7, 0, 1, 1)

        self.color_swap_9 = ColorButton(parent=self.gridLayoutWidget_4, color="cyan", key=9)
        self.gridLayout_6.addWidget(self.color_swap_9, 0, 0, 1, 1)

        self.color_swap_10 = ColorButton(parent=self.gridLayoutWidget_4, color="DarkBlue", key=10)
        self.gridLayout_6.addWidget(self.color_swap_10, 1, 0, 1, 1)

        self.color_swap_11 = ColorButton(parent=self.gridLayoutWidget_4, color="brown", key=11)
        self.gridLayout_6.addWidget(self.color_swap_11, 2, 0, 1, 1)

        self.color_swap_12 = ColorButton(parent=self.gridLayoutWidget_4, color="DarkGoldenRod", key=12)
        self.gridLayout_6.addWidget(self.color_swap_12, 3, 0, 1, 1)

        self.color_swap_13 = ColorButton(parent=self.gridLayoutWidget_4, color="DeepPink", key=13)
        self.gridLayout_6.addWidget(self.color_swap_13, 4, 0, 1, 1)

        self.color_swap_14 = ColorButton(parent=self.gridLayoutWidget_4, color="grey", key=14)
        self.gridLayout_6.addWidget(self.color_swap_14, 5, 0, 1, 1)

        self.color_swap_15 = ColorButton(parent=self.gridLayoutWidget_4, color="Coral", key=15)
        self.gridLayout_6.addWidget(self.color_swap_15, 6, 0, 1, 1)

        self.color_swap_16 = ColorButton(parent=self.gridLayoutWidget_4, color="DarkOrange", key=16)
        self.gridLayout_6.addWidget(self.color_swap_16, 7, 0, 1, 1)

        self.canvas = CanvasWidget(parent=self.centralwidget)
        self.canvas.setGeometry(QtCore.QRect(0, 230, 1920, 1000))


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
        self.canvas.pen = QPen(QColor(options_dict[self.key]), self.widthSlide.value(), Qt.PenStyle.SolidLine, Qt.PenCapStyle.RoundCap, Qt.PenJoinStyle.RoundJoin)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
