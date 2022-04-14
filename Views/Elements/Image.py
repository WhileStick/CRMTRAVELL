from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QLabel

import os
import Config.resources


class Image(QLabel):

    def __init__(self, parent, image_name):
        QLabel.__init__(self, parent=parent)
        pixmap1 = QPixmap(f":/images/{image_name}")
        self.setPixmap(pixmap1)

