from PyQt5 import QtWidgets
from calculator_test import Ui_MainWindow

class Calculator(QtWidgets.QMainWindow, Ui_MainWindow):

    first_numb = None

    def __init__(self):
        super(Calculator, self).__init__()
        self.setupUi(self)
        self.show()

        self.button_0.clicked.connect(self.digit)
        self.button_1.clicked.connect(self.digit)
        self.pushButton_10.clicked.connect(self.digit)
        self.button_3.clicked.connect(self.digit)
        self.button_4.clicked.connect(self.digit)
        self.button_5.clicked.connect(self.digit)
        self.button_6.clicked.connect(self.digit)
        self.button_7.clicked.connect(self.digit)
        self.button_8.clicked.connect(self.digit)
        self.button_9.clicked.connect(self.digit)
        self.button_c.clicked.connect(self.clear)
        self.button_equ.clicked.connect(self.equal)

        self.button_add.clicked.connect(self.operator)
        self.button_sub.clicked.connect(self.operator)
        self.button_multi.clicked.connect(self.operator)
        self.button_divi.clicked.connect(self.operator)

        self.button_add.setCheckable(True)
        self.button_sub.setCheckable(True)
        self.button_multi.setCheckable(True)
        self.button_divi.setCheckable(True)


    def digit(self):
        button = self.sender()

        if (self.button_add.isChecked() or self.button_sub.isChecked() or self.button_multi.isChecked() or
            self.button_divi.isChecked()):
            self.label.clear()
         
        new_label = format(float(self.label.text() + button.text()),".15g")

        if len(new_label) == 15:
            self.label.setText("KEBANYAKAN")
            button.setC
        else:
            self.label.setText(new_label)

    def clear(self):
        self.label.clear()

    def operator(self):
        button = self.sender()

        self.first_numb = float(self.label.text())

        button.setChecked(True)

    def equal(self):
        second_numb = float(self.label.text())

        if self.button_add.isChecked():
            label_number = self.first_numb + second_numb
            new_label = format(label_number,".15g")
            self.label.setText(new_label)
            self.button_add.setChecked(False)
        if self.button_sub.isChecked():
            label_number = self.first_numb - second_numb
            new_label = format(label_number,".15g")
            self.label.setText(new_label)
            self.button_sub.setChecked(False)
        if self.button_multi.isChecked():
            label_number = self.first_numb * second_numb
            new_label = format(label_number,".15g")
            self.label.setText(new_label)
            self.button_multi.setChecked(False)
        if self.button_divi.isChecked():
            label_number = self.first_numb / second_numb
            new_label = format(label_number,".15g")
            self.label.setText(new_label)
            self.button_divi.setChecked(False)