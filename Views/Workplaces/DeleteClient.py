from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QMainWindow, QWidget, QGridLayout, QPushButton, QSizePolicy, QComboBox, QLabel

from loader import db


class DeleteClient(QMainWindow):

    return_to_clients = pyqtSignal()

    def __init__(self, parent):
        QMainWindow.__init__(self, parent=parent)

        self.setObjectName("Lighter")
        self.widget = QWidget(parent=self)
        self.main_layout = QGridLayout()
        self.widget.setLayout(self.main_layout)

        pos = [[1, 1], [2, 1], [3, 1], [4, 1], [1, 2], [4, 2], [1, 3],
               [2, 3], [3, 3], [4, 3]]
        for i in pos:
            lab = QLabel(parent=self.widget)
            self.main_layout.addWidget(lab, i[0], i[1], 1, 1)

        self.b = QPushButton(text="Удалить", parent=self.widget)
        self.b.clicked.connect(self.delete_one)
        self.b.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        self.main_layout.addWidget(self.b, 3, 2, 1, 1)

        self.clients = QComboBox(parent=self.widget)
        parts = db.get_clients_options()
        for i in parts:
            self.clients.addItem(i[1], userData=i[0])
        self.clients.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        self.main_layout.addWidget(self.clients, 2, 2, 1, 1)

        self.setCentralWidget(self.widget)

    def delete_one(self):
        try:
            db.delete_client(self.clients.currentData())
            self.return_to_clients.emit()
        except Exception as e:
            print(e)
