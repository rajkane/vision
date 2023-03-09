import cv2
from src.model.constant import Parameter
from src import *


def show_camera_stop(frame, on: bool):
	if on:
		cv2.putText(frame, "Freeze", (750, 30), cv2.FONT_HERSHEY_SIMPLEX, .7, (0, 180, 0), 2)

class CameraWorker(qtc.QThread):
	img_update = qtc.pyqtSignal(qtg.QImage)
	status = qtc.pyqtSignal(str)
	enabled = qtc.pyqtSignal(bool)
	
	def __init__(self, channel: int):
		super(CameraWorker, self).__init__()
		self.channel = channel
		self.cap = None
		self.active, self.on = None, None

	def run(self):
		self.active, self.on = True, False
		self.cap = cv2.VideoCapture(self.channel)
		self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, Parameter.WIDTH)
		self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, Parameter.HEIGHT)
		
		while self.active:
			self.enabled.emit(True)
			ret, frame = self.cap.read()
			if ret:
				img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
				img = cv2.flip(img, 1)
				convert_qt_format = qtg.QImage(img.data, img.shape[1], img.shape[0],
											   qtg.QImage.Format_RGB888)
				pic = convert_qt_format.scaled(Parameter.SIZE, Parameter.KEEPRATIO,
											   Parameter.SMOOTH_TRANSFORMATION)
				self.img_update.emit(pic)
				self.status.emit("Live camera in real time ...")
				
				if self.on:
					show_camera_stop(frame=img, on=self.on)
					convert_qt_format = qtg.QImage(img.data, img.shape[1], img.shape[0], qtg.QImage.Format_RGB888)
					pic = convert_qt_format.scaled(Parameter.SIZE, Parameter.KEEPRATIO,
												   Parameter.SMOOTH_TRANSFORMATION)
					self.img_update.emit(pic)
					self.status.emit("Freeze camera")
					self.enabled.emit(False)
					break
			else:
				break
	
	def stop(self):
		self.active, self.on = False, True
		self.wait()
