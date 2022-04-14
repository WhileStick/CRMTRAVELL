from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QWidget, QGridLayout, QSizePolicy

from Views import View
from Views.Bars import MainBar
from Views.Workplaces import PartnerWorkplace, ClientsWorkplace, CreatePartner, CalendarSpace, DeletePartner
from Views.Workplaces.DeleteClient import DeleteClient


class MainMenu(View):

    switch_to_create_client = pyqtSignal()
    switch_exit = pyqtSignal()

    def __init__(self, geometry=None, login="user"):
        View.__init__(self, "MainMenu", geometry)
        self.setWindowTitle('Main Window')

        self.global_widget = QWidget(self)
        self.layout = QGridLayout()
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setVerticalSpacing(0)
        self.global_widget.setLayout(self.layout)
        self.workplace = None

        self.bar = MainBar(self)
        self.bar.set_login(login)
        self.bar.switch_exit.connect(self.emit_exit)
        self.layout.addWidget(self.bar, 0, 0, 1, 1)
        self.bar.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        #layout.addWidget(self.widget, 1, 0, 1, 1)
        #layout.addWidget(self.button, 1, 0, 2, 1)

        self.setLayout(self.layout)
        self.connect_menu_signals()
        self.open_partners()

        self.setCentralWidget(self.global_widget)

    def switch(self):
        self.switch_window.emit()

    def connect_menu_signals(self):
        self.bar.get_partners_signal().connect(self.open_partners)
        self.bar.get_clients_signal().connect(self.open_clients)
        self.bar.switch_to_create_client.connect(self.switch_to_client)
        self.bar.switch_to_calendar.connect(self.open_calendar)

    def open_clients(self):
        if self.workplace:
            self.workplace.close()
        self.workplace = ClientsWorkplace(self)
        self.workplace.switch_to_delete.connect(self.delete_client_menu)
        self.layout.addWidget(self.workplace, 1, 0, 10, 1)
        self.workplace.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)

    def open_partners(self):
        if self.workplace:
            self.workplace.close()
        self.workplace = PartnerWorkplace(self)
        self.workplace.switch_to_create.connect(self.create_partner_menu)
        self.workplace.switch_to_delete.connect(self.delete_partner_menu)
        self.layout.addWidget(self.workplace, 1, 0, 10, 1)
        self.workplace.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)

    def open_calendar(self):
        if self.workplace:
            self.workplace.close()
        self.workplace = CalendarSpace(self)
        self.layout.addWidget(self.workplace, 1, 0, 10, 1)
        self.workplace.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)

    def delete_client_menu(self):
        self.workplace.close()
        try:
            self.workplace = DeleteClient(self)
        except Exception as e:
            print(e)
        self.layout.addWidget(self.workplace, 1, 0, 10, 1)
        self.workplace.return_to_clients.connect(self.open_clients)
        self.workplace.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)

    def create_partner_menu(self):
        self.workplace.close()
        try:
            self.workplace = CreatePartner(self)
            self.workplace.on_added_partner.connect(self.open_partners)
        except Exception as e:
            print(e)
        self.layout.addWidget(self.workplace, 1, 0, 10, 1)
        self.workplace.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)

    def delete_partner_menu(self):
        self.workplace.close()
        try:
            self.workplace = DeletePartner(self)
            self.workplace.return_to_partners.connect(self.open_partners)
        except Exception as e:
            print(e)
        self.layout.addWidget(self.workplace, 1, 0, 10, 1)
        self.workplace.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)

    def switch_to_client(self):
        self.switch_to_create_client.emit()

    def emit_exit(self):
        self.switch_exit.emit()

