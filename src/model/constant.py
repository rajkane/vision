from src import *


class Parameter:
    SCALE = 1
    WIDTH = 1400
    HEIGHT = 800
    SIZE = qtc.QSize(int(WIDTH*SCALE), int(HEIGHT*SCALE))
    KEEPRATIO = qtc.Qt.AspectRatioMode.KeepAspectRatio
    SMOOTH_TRANSFORMATION = qtc.Qt.TransformationMode.SmoothTransformation
    RECT_COLOR = (0, 0, 255)
    THICKNEES = 2
