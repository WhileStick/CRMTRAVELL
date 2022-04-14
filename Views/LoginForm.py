from PyQt5.QtCore import pyqtSignal
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QWidget, QGridLayout, QPushButton, QVBoxLayout, QLineEdit, QSizePolicy, QLabel
from PyQt5.Qt import Qt

from Views import View
from Views.Elements import Image


class LoginForm(View):

    # Сигнал для запуска авторизации пользователя
    auth = pyqtSignal(str, str)

    def __init__(self, geometry=None):
        View.__init__(self, "LoginForm", geometry)
        self.setWindowTitle('Login')

        global_layout = QGridLayout()
        widget_layout = QGridLayout()

        self.global_widget = QWidget(self)
        self.global_widget.setLayout(global_layout)

        self.widget = QWidget(self.global_widget)
        self.widget.setObjectName("LoginBullet")
        self.widget.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        self.widget.setLayout(widget_layout)

        print(self.geometry())
        print(self.widget.geometry())

        self.login_line = QLineEdit(parent=self.widget, placeholderText='Логин')
        self.login_line.setMinimumSize(300, 50)
        self.login_line.setMaximumSize(600, 50)
        self.password_line = QLineEdit(parent=self.widget, placeholderText='Пароль')
        self.password_line.setEchoMode(2)
        self.password_line.setMinimumSize(300, 50)
        self.password_line.setMaximumSize(600, 50)
        self.button = QPushButton(parent=self.widget, text='Войти')
        self.button.setObjectName("GreenButton")
        self.button.setMinimumSize(70, 40)
        self.button.setMaximumSize(140, 60)
        self.button.clicked.connect(self.login)

        self.image = Image(self, "cotravel.png")

        widget_layout.addWidget(self.login_line, 2, 1, 2, 4)
        widget_layout.setVerticalSpacing(20)
        widget_layout.addWidget(self.password_line, 4, 1, 2, 4)
        widget_layout.addWidget(self.button, 6, 1, 2, 2)
        widget_layout.addWidget(self.image, 1, 1, 1, 1)

        global_layout.addWidget(self.widget, 2, 2, 1, 1, alignment=Qt.AlignCenter)

        self.setLayout(global_layout)

        self.setCentralWidget(self.global_widget)
        self.show()

    def login(self):
        text = self.login_line.text() if self.login_line.text() != '' else None
        passw = self.password_line.text() if self.password_line.text() != '' else None
        #print(f"Emmiting signal auth in LoginForm with value '{text}'")
        self.auth.emit(text, passw)
