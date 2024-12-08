import io
import os
import sys


from PyQt6 import uic  # Импортируем uic
from PyQt6.QtWidgets import QDialog
from PyQt6.QtGui import QIcon

class Dialog(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi('consts/Dialog.ui', self)
        self.setWindowTitle("Cryptography")
        self.setWindowIcon(QIcon('images/ico.png'))
        self.comboBox.addItem('C')
        self.comboBox.addItem('F')
        self.comboBox.addItem('G')
        self.comboBox.addItem('D')
        self.comboBox.addItem('M')
        self.comboBox.setCurrentIndex(-1)
        self.comboBox.currentTextChanged.connect(self.activated)

    def activated(self, index):
        # print(index)
        self.index = index



