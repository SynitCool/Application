from kivy.uix.screenmanager import Screen
from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.properties import ObjectProperty

class MainLayout(Screen):
    input_number = ObjectProperty(None)
    snumb = None
    fnumb = None
    def subtraction(self):
        try:
            self.fnumb = float(self.input_number.text)
        except ValueError:
            pass

        self.operation = "subtraction"
        self.input_number.text = ""

    def multiplication(self):
        try:
            self.fnumb = float(self.input_number.text)
        except ValueError:
            pass

        self.operation = "multiplication"
        self.input_number.text = ""

    def division(self):
        try:
            self.fnumb = float(self.input_number.text)
        except ValueError:
            pass

        self.operation = "division"
        self.input_number.text = ""

    def addition(self):
        try:
            self.fnumb = float(self.input_number.text)
        except ValueError:
            pass

        self.operation = "addition"
        self.input_number.text = ""

    def equal(self):
        try:
            self.snumb = int(self.input_number.text)
            if self.operation == "addition":
                self.input_number.text = str(self.fnumb + self.snumb)
            elif self.operation == "subtraction":
                self.input_number.text = str(self.fnumb - self.snumb)
            elif self.operation == "multiplication":
                self.input_number.text = str(self.fnumb * self.snumb)
            elif self.operation == "division":
                self.input_number.text = str(self.fnumb / self.snumb)
        except:
            pass

    def clear(self):
        self.input_number.text = ""
        self.fnumb = None
        self.snumb = None

class CalculatorApp(App):
    def build(self):
        Window.size = (300, 450)
        return Builder.load_file("design.kv")