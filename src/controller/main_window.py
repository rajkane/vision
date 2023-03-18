from src import *
from src.view.ui_vision import Ui_MainWindow
from src.model.camera_model import CameraWorker


class MainWindow(qtw.QMainWindow, Ui_MainWindow):
	def __init__(self):
		super(MainWindow, self).__init__()
		self.setupUi(self)
		self.worker = None
		
		self.btn_live.clicked.connect(self.live_camera)
		self.btn_freeze.clicked.connect(self.freeze_camera)
		
		self.action_running_process(on=False)
	
	def live_camera(self):
		self.worker = CameraWorker(channel=-1)
		self.worker.img_update.connect(self.update_image)
		self.worker.enabled.connect(self.action_running_process)
		self.worker.status.connect(self.message_status)
		self.worker.start()
	
	def freeze_camera(self):
		self.worker.enabled.connect(self.action_running_process)
		self.worker.stop()
		
	@qtc.pyqtSlot(qtg.QImage)
	def update_image(self, img):
		self.lbl_stream.setPixmap(qtg.QPixmap.fromImage(img))
	
	def action_running_process(self, on):
		if on:
			self.btn_live.setEnabled(False)
			self.btn_freeze.setEnabled(True)
		else:
			self.btn_live.setEnabled(True)
			self.btn_freeze.setEnabled(False)
	
	@qtc.pyqtSlot(str)
	def message_status(self, message):
		self.statusbar.setStyleSheet("color: lightgreen; background-color: darkgreen")
		self.statusbar.showMessage(message)
		
