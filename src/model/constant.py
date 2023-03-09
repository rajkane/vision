from src import *


class Parameter:
    SCALE = 2
    WIDTH = 800
    HEIGHT = 600
    SIZE = qtc.QSize(int(WIDTH*SCALE), int(HEIGHT*SCALE))
    KEEPRATIO = qtc.Qt.AspectRatioMode.KeepAspectRatio
    SMOOTH_TRANSFORMATION = qtc.Qt.TransformationMode.SmoothTransformation
    RECT_COLOR = (0, 0, 255)
    THICKNEES = 2
