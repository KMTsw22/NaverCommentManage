# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'LoginUi.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(636, 287)
        self.StartBtn = QtWidgets.QPushButton(Dialog)
        self.StartBtn.setGeometry(QtCore.QRect(70, 70, 191, 51))
        self.StartBtn.setObjectName("StartBtn")
        self.FinishBtn = QtWidgets.QPushButton(Dialog)
        self.FinishBtn.setGeometry(QtCore.QRect(340, 190, 181, 51))
        self.FinishBtn.setObjectName("FinishBtn")
        self.MacroBtn = QtWidgets.QPushButton(Dialog)
        self.MacroBtn.setGeometry(QtCore.QRect(70, 190, 191, 51))
        self.MacroBtn.setObjectName("MacroBtn")
        self.Rest = QtWidgets.QLineEdit(Dialog)
        self.Rest.setGeometry(QtCore.QRect(470, 120, 51, 41))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(14)
        self.Rest.setFont(font)
        self.Rest.setText("")
        self.Rest.setObjectName("Rest")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(340, 130, 111, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(340, 30, 101, 16))
        self.label_2.setObjectName("label_2")
        self.Want = QtWidgets.QLineEdit(Dialog)
        self.Want.setGeometry(QtCore.QRect(470, 20, 51, 41))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(14)
        self.Want.setFont(font)
        self.Want.setText("")
        self.Want.setObjectName("Want")
        self.Now = QtWidgets.QLineEdit(Dialog)
        self.Now.setGeometry(QtCore.QRect(470, 70, 51, 41))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(14)
        self.Now.setFont(font)
        self.Now.setText("")
        self.Now.setObjectName("Now")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(340, 80, 101, 16))
        self.label_3.setObjectName("label_3")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.StartBtn.setText(_translate("Dialog", "네이버 로그인"))
        self.FinishBtn.setText(_translate("Dialog", "중지"))
        self.MacroBtn.setText(_translate("Dialog", "댓글 지우기 시작"))
        self.label.setText(_translate("Dialog", "남은 페이지 수"))
        self.label_2.setText(_translate("Dialog", "원하는 채택률"))
        self.label_3.setText(_translate("Dialog", "현재 채택률"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
