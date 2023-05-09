import sys
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton


# Subclass QMainwindow to customize my application's main window
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Qt Main Window")
        button = QPushButton("Press Me")

        # size of main window
        self.setFixedSize(QSize(900, 500))
        # self.setWindowIcon(images\\logoHCi3N.ico)

        # set the central widget of the main window
        self.setCentralWidget(button)

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
