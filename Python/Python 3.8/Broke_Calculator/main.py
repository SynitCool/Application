import sys
from PyQt5.QtWidgets import QApplication
from calculator_test_lgc import Calculator

app = QApplication(sys.argv)

calculator = Calculator()

sys.exit(app.exec_())