# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(450, 265)
        MainWindow.setMinimumSize(QtCore.QSize(450, 265))
        MainWindow.setMaximumSize(QtCore.QSize(450, 265))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("C:\\Users\\vikto\\.vscode\\MyWork\\Downloader\\downloader\\icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("background-color: rgb(70, 70, 70);")
        MainWindow.setIconSize(QtCore.QSize(30, 30))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(15, 15, 420, 150))
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(12)
        font.setItalic(False)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color: rgb(110, 110, 110);\n"
"border-radius: 6px;\n"
"border-color: rgb(196, 48, 43);\n"
"border-style: solid; border-width: 2px;\n"
"color: rgb(255, 255, 255);")
        self.label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(15, 175, 420, 32))
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(12)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("border-radius: 5px;\n"
"border-color: rgb(196, 48, 43);\n"
"border-style: solid; border-width: 2px;\n"
"background-color: rgb(240, 240, 240);")
        self.lineEdit.setText("")
        self.lineEdit.setMaxLength(1000)
        self.lineEdit.setFrame(True)
        self.lineEdit.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lineEdit.setObjectName("lineEdit")
        self.btn_select = QtWidgets.QPushButton(self.centralwidget)
        self.btn_select.setGeometry(QtCore.QRect(15, 220, 205, 30))
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.btn_select.setFont(font)
        self.btn_select.setStyleSheet("QPushButton{\n""border: 2px solid #c4302b;\n""border-radius: 5px;"
"background-color: #e6e61e;\n""color: black;\n""}\n"
"\n""QPushButton:hover{\n""border: 2px solid #c4302b;\n"
"background-color: #444444;\n""color: white;\n""}\n"
"\n""QPushButton:pressed{\n""border: 2px solid white;\n"
"background-color: #444444;\n""color: white;\n""}")
        self.btn_select.setObjectName("btn_select")
        self.btn_download = QtWidgets.QPushButton(self.centralwidget)
        self.btn_download.setGeometry(QtCore.QRect(230, 220, 205, 30))
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(12)
        self.btn_download.setFont(font)
        self.btn_download.setStyleSheet("QPushButton{\n""border: 2px solid #c4302b;\n""border-radius: 5px;"
"background-color: #c4302b;\n""color: white;\n""}\n"
"\n""QPushButton:hover{\n""border: 2px solid #c4302b;\n"
"background-color: #444444;\n""color: white;\n""}\n"
"\n""QPushButton:pressed{\n""border: 2px solid white;\n"
"background-color: #444444;\n""color: white;\n""}")
        self.btn_select.setObjectName("btn_select")
        self.btn_download.setObjectName("btn_download")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("Mainwindow", "Youtube downloader"))
        self.label.setText(_translate("MainWindow", "execution process . . ."))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "Paste URL https://www.youtube.com/watch?v="))
        self.btn_select.setText(_translate("MainWindow", "&Select folder"))
        self.btn_download.setText(_translate("MainWindow", "&Download"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
