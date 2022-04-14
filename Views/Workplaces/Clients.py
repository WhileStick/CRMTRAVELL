from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QWidget, QScrollArea, QVBoxLayout, QPushButton, QSizePolicy, QGridLayout, QLabel, \
    QMainWindow
from PyQt5.Qt import Qt

from Views.Elements import DBTableClients
from loader import db


class ClientsWorkplace(QMainWindow):

    switch_to_delete = pyqtSignal()

    def __init__(self, parent):
        QWidget.__init__(self, parent=parent)

        self.setObjectName("Lighter")

        self.widget = QWidget(self)
        self.main_layout = QGridLayout()
        self.widget.setLayout(self.main_layout)
        self.setLayout(self.main_layout)

        self.b = QPushButton(text="Удалить клиента", parent=self.widget)
        self.b.clicked.connect(self.delete_one)
        self.b.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        self.main_layout.addWidget(self.b, 1, 2, 1, 1)

        self.table = DBTableClients(self.widget)
        self.main_layout.addWidget(self.table, 2, 1, 6, 3)
        self.table.set_source(db)

        self.setCentralWidget(self.widget)

    def delete_one(self):
        self.switch_to_delete.emit()


