# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'src/view/ui_vision.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("background-color: rgb(36, 31, 49);\n"
"color: rgb(143, 240, 164);")
        MainWindow.setUnifiedTitleAndToolBarOnMac(True)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.lbl_stream = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_stream.sizePolicy().hasHeightForWidth())
        self.lbl_stream.setSizePolicy(sizePolicy)
        self.lbl_stream.setCursor(QtGui.QCursor(QtCore.Qt.CrossCursor))
        self.lbl_stream.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_stream.setObjectName("lbl_stream")
        self.gridLayout.addWidget(self.lbl_stream, 0, 3, 3, 1)
        self.btn_live = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_live.sizePolicy().hasHeightForWidth())
        self.btn_live.setSizePolicy(sizePolicy)
        self.btn_live.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_live.setObjectName("btn_live")
        self.gridLayout.addWidget(self.btn_live, 0, 0, 1, 1)
        self.btn_settings = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_settings.sizePolicy().hasHeightForWidth())
        self.btn_settings.setSizePolicy(sizePolicy)
        self.btn_settings.setObjectName("btn_settings")
        self.gridLayout.addWidget(self.btn_settings, 2, 0, 1, 1)
        self.btn_freeze = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_freeze.sizePolicy().hasHeightForWidth())
        self.btn_freeze.setSizePolicy(sizePolicy)
        self.btn_freeze.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_freeze.setObjectName("btn_freeze")
        self.gridLayout.addWidget(self.btn_freeze, 1, 0, 1, 1)
        self.btn_gray_rgb = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_gray_rgb.sizePolicy().hasHeightForWidth())
        self.btn_gray_rgb.setSizePolicy(sizePolicy)
        self.btn_gray_rgb.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_gray_rgb.setObjectName("btn_gray_rgb")
        self.gridLayout.addWidget(self.btn_gray_rgb, 0, 4, 1, 1)
        self.btn_measurement = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_measurement.sizePolicy().hasHeightForWidth())
        self.btn_measurement.setSizePolicy(sizePolicy)
        self.btn_measurement.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_measurement.setObjectName("btn_measurement")
        self.gridLayout.addWidget(self.btn_measurement, 1, 4, 1, 1)
        self.btn_machine_vision = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_machine_vision.sizePolicy().hasHeightForWidth())
        self.btn_machine_vision.setSizePolicy(sizePolicy)
        self.btn_machine_vision.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_machine_vision.setObjectName("btn_machine_vision")
        self.gridLayout.addWidget(self.btn_machine_vision, 2, 4, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setAutoFillBackground(False)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Vision"))
        MainWindow.setStatusTip(_translate("MainWindow", "ready ..."))
        self.lbl_stream.setStatusTip(_translate("MainWindow", "streaming ..."))
        self.lbl_stream.setText(_translate("MainWindow", "Stream"))
        self.btn_live.setStatusTip(_translate("MainWindow", "live streaming ..."))
        self.btn_live.setText(_translate("MainWindow", "Live"))
        self.btn_settings.setStatusTip(_translate("MainWindow", "settings ..."))
        self.btn_settings.setText(_translate("MainWindow", "Settings"))
        self.btn_freeze.setStatusTip(_translate("MainWindow", "freeze streaming ..."))
        self.btn_freeze.setText(_translate("MainWindow", "Freeze"))
        self.btn_gray_rgb.setStatusTip(_translate("MainWindow", "gray scale ..."))
        self.btn_gray_rgb.setText(_translate("MainWindow", "Gray"))
        self.btn_measurement.setStatusTip(_translate("MainWindow", "measurement ..."))
        self.btn_measurement.setText(_translate("MainWindow", "Measurement"))
        self.btn_machine_vision.setStatusTip(_translate("MainWindow", "machine vision ..."))
        self.btn_machine_vision.setText(_translate("MainWindow", "Machine\n"
"Vision"))
