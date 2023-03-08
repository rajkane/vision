try:
	from PyQt5 import QtWidgets as qtw
	from PyQt5 import QtCore as qtc
	from PyQt5 import QtGui as qtg
except ImportWarning as iw:
	print(str(iw))
except ImportError as ie:
	print(str(ie))

