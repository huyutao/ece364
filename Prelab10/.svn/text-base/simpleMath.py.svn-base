from PySide.QtCore import *
from PySide.QtGui import *

from calculator import *

class simpleMath(QMainWindow, Ui_Calculator):
    def __init__(self, parent = None):
        super(simpleMath,self).__init__(parent)
        self.setupUi(self)
        self.data_str = ""
        self.num_btns = [self.btn0,self.btn1,self.btn2,self.btn3,self.btn4,self.btn5,self.btn6,self.btn7,self.btn8,self.btn9,self.btnDot]

        self.btnMultiply.clicked.connect(self.multiply)
        self.btnDivide.clicked.connect(self.devide)
        self.btnPlus.clicked.connect(self.plus)
        self.btnMinus.clicked.connect(self.minus)
        self.btnClear.clicked.connect(self.clearNum)
        self.btnEqual.clicked.connect(self.euqalRun)
        self.cboDecimal.currentIndexChanged.connect(self.change_dec)
        self.chkSeparator.stateChanged.connect(self.change_sep)

        for button in self.num_btns:
            button.clicked.connect(self.num_changed)

        self.prev_data = 0
        self.operator = ""
        self.num_changed_flag = False
        self.decimal = 2
        self.thous = True

    def plus(self):
        self.euqalRun()
        self.operator = "+"

    def minus(self):
        self.euqalRun()
        self.operator = "-"

    def multiply(self):
        self.euqalRun()
        self.operator = "*"

    def devide(self):
        self.euqalRun()
        self.operator = "/"

    def clearNum(self):
        self.prev_data = 0
        self.data_str = "0."
        self.display()
        self.data_str = ""

    def euqalRun(self):
        if self.num_changed_flag:
            current_data = float(self.data_str)
            if self.operator == "+":
                self.data_str = str(self.prev_data + current_data)
            elif self.operator == "-":
                self.data_str = str(self.prev_data - current_data)
            elif self.operator == "*":
                self.data_str = str(self.prev_data * current_data)
            elif self.operator == "/":
                self.data_str = str(self.prev_data / current_data)
            self.prev_data = float(self.data_str)
            self.rich_display()
            self.data_str = ""
            self.operator = ""
            self.num_changed_flag = False


    def num_changed(self):
        self.num_changed_flag = True
        button = self.sender()
        if len(self.data_str) < 12:
            self.data_str += button.text()
        self.display()

    def rich_display(self):
        num = float(self.prev_data)
        int_part,dec_part = str(num).split(".")
        if self.thous:
            if dec_part == "0":
                result = "{:,}".format(int(num))
            elif len(str(dec_part)) > self.decimal:
                pattern = "{:12,." + str(self.decimal) + "f}"
                result = pattern.format(num)
            else:
                result = "{:,}".format(num)
        else:
            if dec_part == "0":
                result = str(int(num))
            elif len(str(dec_part)) > self.decimal:
                pattern = "{:12." + str(self.decimal) + "f}"
                result = pattern.format(num)
            else:
                result = str(num)
        self.txtDisplay.setText(result)

    def display(self):
        self.txtDisplay.setText(self.data_str)

    def change_dec(self):
        combobox = self.sender()
        self.decimal = int(combobox.currentText())
        self.rich_display()

    def change_sep(self):
        self.thous = not self.thous
        self.rich_display()


currentApp = QApplication([])
currentForm = simpleMath()
currentForm.show()
currentApp.exec_()
