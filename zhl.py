# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1151, 618)
        self.chkShow = QtWidgets.QCheckBox(Form)
        self.chkShow.setGeometry(QtCore.QRect(800, 330, 105, 22))
        self.chkShow.setObjectName("chkShow")
        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setGeometry(QtCore.QRect(20, 20, 261, 391))
        self.groupBox.setObjectName("groupBox")
        self.comboBoxSerialport = QtWidgets.QComboBox(self.groupBox)
        self.comboBoxSerialport.setGeometry(QtCore.QRect(80, 40, 99, 24))
        self.comboBoxSerialport.setObjectName("comboBoxSerialport")
        self.comboBoxData = QtWidgets.QComboBox(self.groupBox)
        self.comboBoxData.setGeometry(QtCore.QRect(80, 130, 99, 24))
        self.comboBoxData.setObjectName("comboBoxData")
        self.comboBoxData.addItem("")
        self.comboBoxData.addItem("")
        self.comboBoxData.addItem("")
        self.comboBoxData.addItem("")
        self.btnDetect = QtWidgets.QPushButton(self.groupBox)
        self.btnDetect.setGeometry(QtCore.QRect(80, 290, 112, 34))
        self.btnDetect.setObjectName("btnDetect")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(10, 40, 41, 18))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(10, 130, 81, 18))
        self.label_2.setObjectName("label_2")
        self.btnOpen = QtWidgets.QPushButton(self.groupBox)
        self.btnOpen.setGeometry(QtCore.QRect(30, 340, 81, 34))
        self.btnOpen.setObjectName("btnOpen")
        self.btnClose = QtWidgets.QPushButton(self.groupBox)
        self.btnClose.setGeometry(QtCore.QRect(150, 340, 81, 34))
        self.btnClose.setObjectName("btnClose")
        self.comboBoxCheck = QtWidgets.QComboBox(self.groupBox)
        self.comboBoxCheck.setGeometry(QtCore.QRect(80, 180, 99, 24))
        self.comboBoxCheck.setObjectName("comboBoxCheck")
        self.comboBoxCheck.addItem("")
        self.comboBoxCheck.addItem("")
        self.comboBoxCheck.addItem("")
        self.comboBoxStop = QtWidgets.QComboBox(self.groupBox)
        self.comboBoxStop.setGeometry(QtCore.QRect(80, 230, 99, 24))
        self.comboBoxStop.setObjectName("comboBoxStop")
        self.comboBoxStop.addItem("")
        self.comboBoxStop.addItem("")
        self.comboBoxStop.addItem("")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(10, 80, 61, 18))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(10, 180, 61, 18))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setGeometry(QtCore.QRect(10, 230, 61, 18))
        self.label_5.setObjectName("label_5")
        self.comboBoxBoud = QtWidgets.QComboBox(self.groupBox)
        self.comboBoxBoud.setGeometry(QtCore.QRect(80, 80, 99, 24))
        self.comboBoxBoud.setObjectName("comboBoxBoud")
        self.comboBoxBoud.addItem("")
        self.comboBoxBoud.addItem("")
        self.comboBoxBoud.addItem("")
        self.comboBoxBoud.addItem("")
        self.comboBoxBoud.addItem("")
        self.comboBoxBoud.addItem("")
        self.comboBoxBoud.addItem("")
        self.comboBoxBoud.addItem("")
        self.comboBoxBoud.addItem("")
        self.groupBoxReceive = QtWidgets.QGroupBox(Form)
        self.groupBoxReceive.setGeometry(QtCore.QRect(350, 20, 401, 251))
        self.groupBoxReceive.setObjectName("groupBoxReceive")
        self.textReceive = QtWidgets.QTextEdit(self.groupBoxReceive)
        self.textReceive.setGeometry(QtCore.QRect(20, 30, 251, 211))
        self.textReceive.setObjectName("textReceive")
        self.textShow = QtWidgets.QTextEdit(self.groupBoxReceive)
        self.textShow.setGeometry(QtCore.QRect(280, 30, 104, 211))
        self.textShow.setObjectName("textShow")
        self.groupBoxSend = QtWidgets.QGroupBox(Form)
        self.groupBoxSend.setGeometry(QtCore.QRect(350, 280, 401, 191))
        self.groupBoxSend.setObjectName("groupBoxSend")
        self.textSend = QtWidgets.QTextEdit(self.groupBoxSend)
        self.textSend.setGeometry(QtCore.QRect(20, 20, 361, 151))
        self.textSend.setObjectName("textSend")
        self.chkSend = QtWidgets.QCheckBox(Form)
        self.chkSend.setGeometry(QtCore.QRect(950, 330, 105, 22))
        self.chkSend.setObjectName("chkSend")
        self.btnClear = QtWidgets.QPushButton(Form)
        self.btnClear.setGeometry(QtCore.QRect(800, 380, 112, 34))
        self.btnClear.setObjectName("btnClear")
        self.btnSend = QtWidgets.QPushButton(Form)
        self.btnSend.setGeometry(QtCore.QRect(800, 430, 112, 34))
        self.btnSend.setObjectName("btnSend")

        self.retranslateUi(Form)
        self.btnSend.clicked.connect(Form.senddata)
        self.btnClear.clicked.connect(Form.cleardata)
        self.btnClose.clicked.connect(Form.closeport)
        self.btnDetect.clicked.connect(Form.findport)
        self.btnOpen.clicked.connect(Form.openport)
        self.chkShow.toggled['bool'].connect(Form.Hexshow)
        self.chkSend.toggled['bool'].connect(Form.Hexsend)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.chkShow.setText(_translate("Form", "Hex显示"))
        self.groupBox.setTitle(_translate("Form", "串口设置"))
        self.comboBoxData.setItemText(0, _translate("Form", "8"))
        self.comboBoxData.setItemText(1, _translate("Form", "7"))
        self.comboBoxData.setItemText(2, _translate("Form", "6"))
        self.comboBoxData.setItemText(3, _translate("Form", "5"))
        self.btnDetect.setText(_translate("Form", "检测串口"))
        self.label.setText(_translate("Form", "串口"))
        self.label_2.setText(_translate("Form", "数据位"))
        self.btnOpen.setText(_translate("Form", "打开"))
        self.btnClose.setText(_translate("Form", "关闭"))
        self.comboBoxCheck.setItemText(0, _translate("Form", "N"))
        self.comboBoxCheck.setItemText(1, _translate("Form", "E"))
        self.comboBoxCheck.setItemText(2, _translate("Form", "O"))
        self.comboBoxStop.setItemText(0, _translate("Form", "1"))
        self.comboBoxStop.setItemText(1, _translate("Form", "1.5"))
        self.comboBoxStop.setItemText(2, _translate("Form", "2"))
        self.label_3.setText(_translate("Form", "波特率"))
        self.label_4.setText(_translate("Form", "校验位"))
        self.label_5.setText(_translate("Form", "停止位"))
        self.comboBoxBoud.setItemText(0, _translate("Form", "115200"))
        self.comboBoxBoud.setItemText(1, _translate("Form", "76800"))
        self.comboBoxBoud.setItemText(2, _translate("Form", "57600"))
        self.comboBoxBoud.setItemText(3, _translate("Form", "19200"))
        self.comboBoxBoud.setItemText(4, _translate("Form", "14400"))
        self.comboBoxBoud.setItemText(5, _translate("Form", "9600"))
        self.comboBoxBoud.setItemText(6, _translate("Form", "4800"))
        self.comboBoxBoud.setItemText(7, _translate("Form", "2400"))
        self.comboBoxBoud.setItemText(8, _translate("Form", "1200"))
        self.groupBoxReceive.setTitle(_translate("Form", "接收区"))
        self.groupBoxSend.setTitle(_translate("Form", "发送区"))
        self.chkSend.setText(_translate("Form", "Hex发送"))
        self.btnClear.setText(_translate("Form", "清除"))
        self.btnSend.setText(_translate("Form", "发送"))

