import os, sys, youtube_dl
from PyQt5 import QtCore, QtGui, QtWidgets
from design_downloader1 import *

class downloader(QtCore.QThread):
    mysignal = QtCore.pyqtSignal(str)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.url = None

    def run(self):
        self.mysignal.emit('The download process has started!')

        with youtube_dl.YoutubeDL({}) as ydl:
            ydl.download([self.url])

        self.mysignal.emit('The download process is complete!')
        self.mysignal.emit('finish')

    def init_args(self, url):
        self.url = url
    

class Download(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.download_folder = None
        self.ui.btn_select.clicked.connect(self.get_folder)
        self.ui.btn_download.clicked.connect(self.start)
        self.mythread = downloader()
        self.mythread.mysignal.connect(self.handler)
        

    
    def start(self):
        if len(self.ui.lineEdit.text()) > 10:
            if self.download_folder != None:
                link = self.ui.lineEdit.text()
                self.mythread.init_args(link)
                self.mythread.start()
                self.locker(True)
            else:
               QtWidgets.QMessageBox.warning(self, "Error", "You have not selected a folder!") 
        else:
            QtWidgets.QMessageBox.warning(self, "Error", "Video link has not included!")


    def get_folder(self):
        try:
            self.download_folder = QtWidgets.QFileDialog.getExistingDirectory(self, 'Select a folder to save video')
            os.chdir(self.download_folder)
        except:
            return
        

    def handler(self, value):
        if value == 'finish':
            self.locker(False)

        else:
            self.ui.plainTextEdit.appendPlainText(value)


    def locker(self, lock_value):
        base = [self.ui.btn_select, self.ui.btn_download]

        for item in base:
            item.setDisabled(lock_value)        
        
        
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    win = Download()
    win.show()
    sys.exit(app.exec_())