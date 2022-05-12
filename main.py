from form import *
import sys


class FormControl(QWidget, Ui_Widget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.released.connect(self.pr)

    def pr(self):
        print("ok")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = FormControl()
    window.show()
    sys.exit(app.exec_())

"""
pyinstaller main.py -F --noconsole --name "test_ui"
pyside2-uic form.ui -o form.py
"""
