from src import *
from src.controller.main_window import MainWindow
import sys


def main():
	app = qtw.QApplication(sys.argv)
	mw = MainWindow()
	mw.show()
	sys.exit(app.exec_())


if __name__ == "__main__":
	main()
