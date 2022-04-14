from PyQt5.QtWidgets import QWidget, QPushButton, QLabel, QGridLayout, QSizePolicy, QMainWindow
from PyQt5.QtCore import pyqtSignal, Qt

from Views.Elements import Image
from Config import resources


class MainBar(QMainWindow):

    switch_to_create_client = pyqtSignal()
    switch_to_partners = pyqtSignal()
    switch_to_clients = pyqtSignal()
    switch_to_calendar = pyqtSignal()
    switch_exit = pyqtSignal()

    def __init__(self, parent):
        QWidget.__init__(self, parent=parent)
        self.setMaximumSize(3000, 320)
        self.setObjectName("Darker")
        self.style().unpolish(self)
        self.style().polish(self)
        self.widget = QWidget(self)
        main_layout = QGridLayout()

        self.picture = Image(self.widget, "cotravel.png")
        self.picture.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)

        self.login = QPushButton("Выйти", self.widget)
        self.login.clicked.connect(self.emit_exit)
        self.login.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)

        self.create = QPushButton("Создать", self.widget)
        self.create.setObjectName("GreenButton")
        self.create.clicked.connect(self.emit_create_client)
        self.create.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)

        self.clients = QPushButton("Клиенты", self.widget)
        self.clients.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        self.clients.clicked.connect(self.emit_clients)

        self.partners = QPushButton("Партнеры", self.widget)
        self.partners.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        self.partners.clicked.connect(self.emit_partners)

        self.calendar = QPushButton("Календарь", self.widget)
        self.calendar.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        self.calendar.clicked.connect(self.emit_calendar)

        main_layout.addWidget(self.picture, 0, 0, 1, 1, alignment=Qt.AlignBottom)
        main_layout.addWidget(self.login, 0, 3, 1, 1)
        main_layout.addWidget(self.create, 1, 0, 1, 1)
        main_layout.addWidget(self.clients, 1, 1, 1, 1)
        main_layout.addWidget(self.partners, 1, 2, 1, 1)
        main_layout.addWidget(self.calendar, 1, 3, 1, 1)

        self.widget.setLayout(main_layout)
        self.setCentralWidget(self.widget)

    def set_login(self, val):
       # self.login.setText(val)
        pass

    def get_partners_signal(self):
        return self.switch_to_partners

    def get_clients_signal(self):
        return self.switch_to_clients

    def get_calendar_signal(self):
        return self.switch_to_calendar

    def emit_partners(self):
        self.switch_to_partners.emit()

    def emit_clients(self):
        self.switch_to_clients.emit()

    def emit_calendar(self):
        self.switch_to_calendar.emit()

    def emit_create_client(self):
        self.switch_to_create_client.emit()

    def emit_exit(self):
        self.switch_exit.emit()

