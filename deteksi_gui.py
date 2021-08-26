from PyQt5 import QtCore, QtGui, QtWidgets
import os
from PyQt5.QtGui import QImage

import sys
import cv2

import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe'


class Ui_DETECT(object):
    def setupUi(self, DETECT):
        DETECT.setObjectName("Detect")
        DETECT.resize(876, 551)
        DETECT.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.centralwidget = QtWidgets.QWidget(DETECT)
        self.centralwidget.setObjectName("centralwidget")
        self.open_folder = QtWidgets.QPushButton(self.centralwidget)
        self.open_folder.setGeometry(QtCore.QRect(20, 70, 131, 31))
        self.open_folder.setObjectName("open_folder")
        self.prev_image = QtWidgets.QPushButton(self.centralwidget)
        self.prev_image.setGeometry(QtCore.QRect(20, 140, 131, 31))
        self.prev_image.setObjectName("prev_image")
        self.next_img = QtWidgets.QPushButton(self.centralwidget)
        self.next_img.setGeometry(QtCore.QRect(20, 210, 131, 31))
        self.next_img.setObjectName("next_img")
        self.photo_img = QtWidgets.QLabel(self.centralwidget)
        self.photo_img.setGeometry(QtCore.QRect(160, 0, 541, 541))
        self.photo_img.setText("")
        self.photo_img.setPixmap(QtGui.QPixmap(""))
        self.photo_img.setScaledContents(False)
        self.photo_img.setObjectName("photo_img")
        self.predetect_btn = QtWidgets.QPushButton(self.centralwidget)
        self.predetect_btn.setGeometry(QtCore.QRect(720, 130, 131, 31))
        self.predetect_btn.setObjectName("predetect_btn")
        self.detect_btn = QtWidgets.QPushButton(self.centralwidget)
        self.detect_btn.setGeometry(QtCore.QRect(720, 200, 131, 31))
        self.detect_btn.setObjectName("detect_btn2")
        self.crop_btn = QtWidgets.QPushButton(self.centralwidget)
        self.crop_btn.setGeometry(QtCore.QRect(720, 60, 131, 31))
        self.crop_btn.setObjectName("crop_btn")
        self.label_plat = QtWidgets.QLabel(self.centralwidget)
        self.label_plat.setGeometry(QtCore.QRect(740, 250, 81, 21))
        self.label_plat.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label_plat.setObjectName("label_plat")
        self.output_plat = QtWidgets.QLineEdit(self.centralwidget)
        self.output_plat.setGeometry(QtCore.QRect(720, 280, 131, 31))
        self.output_plat.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.output_plat.setObjectName("output_plat")
        self.crop_img = QtWidgets.QLabel(self.centralwidget)
        self.crop_img.setGeometry(QtCore.QRect(730, 350, 101, 71))
        self.crop_img.setText("")
        self.crop_img.setPixmap(QtGui.QPixmap(""))
        self.crop_img.setScaledContents(True)
        self.crop_img.setObjectName("crop_img")
        DETECT.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(DETECT)
        self.statusbar.setSizeGripEnabled(True)
        self.statusbar.setObjectName("statusbar")
        DETECT.setStatusBar(self.statusbar)

        self.retranslateUi(DETECT)
        self.open_folder.clicked.connect(self.pick_new)
        self.prev_image.clicked.connect(self.show_prev)
        self.next_img.clicked.connect(self.show_next)
        self.image_index=0

        self.crop_btn.clicked.connect(self.selected)
        self.predetect_btn.clicked.connect(self.edit)
        self.detect_btn.clicked.connect(self.printtext)
        QtCore.QMetaObject.connectSlotsByName(DETECT)

    def retranslateUi(self, DETECT):
        _translate = QtCore.QCoreApplication.translate
        DETECT.setWindowTitle(_translate("DETECT", "Deteksi plat kendaraan"))
        self.open_folder.setText(_translate("DETECT", "Open Folder"))
        self.prev_image.setText(_translate("DETECT", "Previous Image"))
        self.next_img.setText(_translate("DETECT", "Next Image"))
        self.predetect_btn.setText(_translate("DETECT", "Pre-Deteksi Plat"))
        self.detect_btn.setText(_translate("DETECT", "Deteksi Plat"))
        self.crop_btn.setText(_translate("DETECT", "Crop"))
        self.label_plat.setText(_translate("DETECT", "Plat kendaraan"))
      
        
    def selected (self):
        if self.image_index%111==6:
            self.photo_img.setPixmap(QtGui.QPixmap("test/"+str(self.file_name[self.image_index==6])))
            self.photo_img.setPixmap(QtGui.QPixmap("test/c211(1).jpeg"))
            self.photo_img.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
            img="test/c221(1).jpeg"
            return img
        if self.image_index%111==1:
            self.photo_img.setPixmap(QtGui.QPixmap("test/"+str(self.file_name[self.image_index==1]))) 
            self.photo_img.setPixmap(QtGui.QPixmap("test/c211(7).jpeg"))
            self.photo_img.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
            img="test/c221(7).jpeg"
            return img
        if self.image_index%111==2:
            self.photo_img.setPixmap(QtGui.QPixmap("test/"+str(self.file_name[self.image_index==2])))
            self.photo_img.setPixmap(QtGui.QPixmap("test/c211(9).jpg"))
            self.photo_img.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
            img="test/c221(9).jpg"
            return img
    
    def pick_new(self):
        self.dialog = QtWidgets.QFileDialog()
        self.folder_path = self.dialog.getExistingDirectory(None, "Select Folder")
        print(self.folder_path)
        self.file_name = []
        for root, dirs, files in os.walk(self.folder_path):
            for file in files:
                if file.endswith('.jpg') or file.endswith('.jpeg'):
                    self.file_name.append(file)

        print(self.file_name)    

    def show_prev(self):
        if self.image_index-1 < 0:
            print("Show valid image")
        else:
            self.image_index-=1
            print(self.file_name[self.image_index])
            self.photo_img.setPixmap(QtGui.QPixmap("test/"+str(self.file_name[self.image_index])))
            
    def show_next(self):
        if self.image_index >= len(self.file_name):
            print("Show valid image")
        else:
            self.image_index+=1
            print(self.file_name[self.image_index])
            self.photo_img.setPixmap(QtGui.QPixmap("test/"+str(self.file_name[self.image_index])))

    def displayimg(self, img):
        qformat = QImage.Format_Indexed8

        if len(img.shape) == 3:
            if(img.shape[2]) == 4:
                qformat = QImage.Format_RGBA8888
            else:
                qformat = QImage.Format_RGB888
        im = QImage(img, img.shap[1], img.shape[0], img.strides[0], qformat)
        im = im.rgbSwapped() 
        self.photo_img.setPixmap(QtGui.QPixmap.fromImage(im))
        self.photo_img.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)

    def edit(self,img):
        imgg=cv2.imread(img)
        gray = cv2.cvtColor(imgg, cv2.COLOR_BGR2GRAY)
        self.displayimg(gray)
        return gray

    def printtext(self,gray):
        text = pytesseract.image_to_string(gray, config='--psm 11')
        text1=print(text)
        self.output_plat.setText(text1)

    


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    DETECT = QtWidgets.QMainWindow()
    ui = Ui_DETECT()
    ui.setupUi(DETECT)
    DETECT.show()
    sys.exit(app.exec_())
