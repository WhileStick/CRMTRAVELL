from PyQt5.QtWidgets import QWidget, QScrollArea, QGridLayout, QPushButton, QSizePolicy, QMainWindow
from PyQt5.Qt import Qt
from PyQt5.QtCore import pyqtSignal

from Views.Elements import DBTablePartners
from loader import db


class PartnerWorkplace(QMainWindow):

    switch_to_create = pyqtSignal()
    switch_to_delete = pyqtSignal()

    def __init__(self, parent):
        QWidget.__init__(self, parent=parent)

        self.main_layout = QGridLayout()
        self.widget = QWidget(self)
        self.setObjectName("Lighter")
        self.widget.setLayout(self.main_layout)

        self.b = QPushButton(text="Добавить нового партнера", parent=self.widget)
        self.b.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        self.b.clicked.connect(self.create_partner)

        self.b2 = QPushButton(text="Удалить партнера", parent=self.widget)
        self.b2.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        self.b2.clicked.connect(self.delete_partner)

        self.main_layout.addWidget(self.b, 1, 0, 1, 1)
        self.main_layout.addWidget(self.b2, 1, 1, 1, 1)

        self.table = DBTablePartners(self.widget)
        self.main_layout.addWidget(self.table, 2, 0, 6, 2)
        self.table.set_source(db)

        self.setCentralWidget(self.widget)

    def create_partner(self):
        self.switch_to_create.emit()

    def delete_partner(self):
        self.switch_to_delete.emit()


