from PyQt5.QtWidgets import QWidget, QMainWindow, QSizePolicy

from Config import view_config


class View(QMainWindow):

    def __init__(self, name="", geometry=None):
        QWidget.__init__(self)
        self.name = name
        self.setObjectName(name)

        self.setGeometry(geometry) if geometry else self.setGeometry(view_config.WINDOW_GEOMETRY)
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        #print(f"{self.name} geometry on init {self.geometry()}")

    def get_geometry(self):
        #print(f"{self.name} geometry {self.geometry()}")
        return self.geometry()

