from PyQt5 import QtCore, QtGui, QtWidgets, QtSerialPort
import sys
from zhl import Ui_Form
import threading
import binascii
import serial
import serial.tools.list_ports


class myapp(QtWidgets.QMainWindow, Ui_Form):
    ser = serial.Serial()

    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_Form.__init__(self)
        self.setupUi(self)

    def senddata(self):
        if(self.ser.isOpen()):
            if(self.chkSend.isChecked()):
                self.ser.write(binascii.a2b_hex(
                    self.textSend.toPlainText()))
            else:
                self.ser.write(self.textSend.toPlainText().encode('utf-8'))
            self.textShow.setText("发送成功")
            # self.ser.flushOutput()
        else:
            self.textShow.setText("发送失败")

    def cleardata(self):
        self.textReceive.setText("")
        self.textShow.setText("接收清空")

    def findport(self):
        Com_List = []
        port_list = list(serial.tools.list_ports.comports())
        self.comboBoxSerialport.clear()
        for port in port_list:
            Com_List.append(port[0])
            self.comboBoxSerialport.addItem(port[0])
        if(len(Com_List) == 0):
            self.textShow.setText("没串口")

    def openport(self):
        self.ser.port = self.comboBoxSerialport.currentText()
        self.ser.baudrate = int(self.comboBoxBoud.currentText())
        self.ser.bytesize = int(self.comboBoxData.currentText())
        self.ser.stopbits = int(self.comboBoxStop.currentText())
        self.ser.parity = self.comboBoxCheck.currentText()
        self.ser.open()
        if(self.ser.isOpen()):
            self.btnOpen.setEnabled(False)
            self.textShow.setText("打开成功")
            self.t1 = threading.Thread(target=self.receive_data)
            self.t1.setDaemon(True)
            self.t1.start()
        else:
            self.textShow.setText("打开失败")

    def closeport(self):
        self.ser.close()
        if(self.ser.isOpen()):
            self.textShow.setText("关闭失败")
        else:
            self.btnOpen.setEnabled(True)
            self.textShow.setText("关闭成功")

    def Hexshow(self):
        pass

    def Hexsend(self):
        pass

    def receive_data(self):
        print("The receive_data threading is start")
        res_data = ''
        num = 0
        while (self.ser.isOpen()):
            size = self.ser.inWaiting()
            if size:
                res_data = self.ser.read_all()
                if(self.chkShow.isChecked()):
                    self.textReceive.append(
                        binascii.b2a_hex(res_data).decode())
                else:
                    self.textReceive.append(res_data.decode())
                self.textReceive.moveCursor(QtGui.QTextCursor.End)
                self.ser.flushInput()
                num += 1
                # self.textShow.setText("接收：" + str(num))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ui = myapp()
    ui.show()
    sys.exit(app.exec_())
