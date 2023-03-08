from src import *
from src.view.ui_vision import Ui_MainWindow


class MainWindow(qtw.QMainWindow, Ui_MainWindow):
	def __init__(self):
		super(MainWindow, self).__init__()
		self.setupUi(self)
		self.show()
