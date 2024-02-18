from PyQt5 import QtCore, QtGui, QtWidgets
from a import Library
from PyQt5.QtCore import QTextCodec

QTextCodec.setCodecForLocale(QTextCodec.codecForName("UTF-8"))


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(766, 422)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icon/images.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("background-color: rgb(170, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(30, 120, 701, 191))
        self.groupBox.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.groupBox.setObjectName("groupBox")
        self.pushButton = QtWidgets.QPushButton(self.groupBox)
        self.pushButton.setGeometry(QtCore.QRect(40, 70, 141, 71))
        self.pushButton.setStyleSheet("selection-background-color: rgb(255, 255, 0);")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/listele/book_learning_notebook_reading_study_icon_127253.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon1)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.kitaplari_listele) 
        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_2.setGeometry(QtCore.QRect(190, 70, 141, 71))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/ekle/book_plus_multiple_icon_137862.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon2)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.kitap_ekle)  
        self.pushButton_3 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_3.setGeometry(QtCore.QRect(340, 70, 131, 71))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/çıkar/book_minus_multiple_icon_138858.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_3.setIcon(icon3)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.kitap_sil)  
        self.pushButton_4 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_4.setGeometry(QtCore.QRect(480, 70, 161, 71))
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/sonlandır/crosshd_106070.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_4.setIcon(icon4)
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.clicked.connect(QtWidgets.qApp.quit) 
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        
        self.lib = Library()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox.setTitle(_translate("MainWindow", "Kütüphane Yönetim Sistemi"))
        self.pushButton.setText(_translate("MainWindow", "1) Kitapları Listele"))
        self.pushButton_2.setText(_translate("MainWindow", "2) Kitap Ekle"))
        self.pushButton_3.setText(_translate("MainWindow", "3) Kitap Sil"))
        self.pushButton_4.setText(_translate("MainWindow", "4)Programı sonlandır"))

    def kitaplari_listele(self):
        self.lib.kitaplari_listele()

    def kitap_ekle(self):
        
        kitap_adi, ok = QtWidgets.QInputDialog.getText(None, "Kitap Ekle", "Kitap Adı:")
        if ok and kitap_adi:
            self.lib.kitap_ekle(kitap_adi)

    def kitap_sil(self):
        
        kitap_adi, ok = QtWidgets.QInputDialog.getText(None, "Kitap Sil", "Silinecek Kitap Adı:")
        if ok and kitap_adi:
            self.lib.kitap_sil(kitap_adi)

    def kitap_ekle(self):
    
        kitap_adi, ok1 = QtWidgets.QInputDialog.getText(None, "Kitap Ekle", "Kitap Adı:")
        yazar, ok2 = QtWidgets.QInputDialog.getText(None, "Kitap Ekle", "Yazar:")
        yayin_yili, ok3 = QtWidgets.QInputDialog.getText(None, "Kitap Ekle", "Yayın Yılı:")
        sayfa_sayisi, ok4 = QtWidgets.QInputDialog.getInt(None, "Kitap Ekle", "Sayfa Sayısı:")
    
    
        if (ok1 and ok2 and ok3 and ok4) and kitap_adi:
        
            kitap_bilgisi = f"{kitap_adi.strip()}, {yazar.strip()}, {yayin_yili.strip()}, {sayfa_sayisi}\n"
        
        
        with open("books.txt", "a") as file:
            file.write(kitap_bilgisi)

    def kitap_sil(self):
    
        kitap_adi, ok = QtWidgets.QInputDialog.getText(None, "Kitap Sil", "Silinecek Kitap Adı:")
    
        if ok and kitap_adi:
        
            with open("books.txt", "r") as file:
                lines = file.readlines()
            with open("books.txt", "w") as file:
                for line in lines:
                    if kitap_adi.strip() not in line:
                        file.write(line)
import icon_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
