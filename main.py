from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
import sys
import peewee
import sqlite3
import json
from PyQt5 import QtWidgets
ui,_ = loadUiType('bigg.ui')
class MainApp(QMainWindow , ui):
        def __init__(self , parent=None):
            super(MainApp , self).__init__(parent)
            QMainWindow.__init__(self)
            self.setupUi(self)
            self.db_conncet()
            self.Categor()
            self.Dashbord()
            self.Exit()
            self.Add_user()
            self.Add_Category()
            self.Add_Items()
            self.Browse()
            self.savebtn()
            self.UICHANGES()


        def db_conncet(self):
            conn = sqlite3.connect('pos.db')
            c = conn.cursor()
            print('Sucssifly Connected!')
#################################
        ### تعديلات علي الواجهة
        def UICHANGES(self):
            self.tab_main.tabBar().setVisible(False)
            self.tabWidget_2.tabBar().setVisible(False)

#################################
############## الازرار الجانبية
        def Categor(self):
            self.btn_cashier.clicked.connect(self.taps)
        def Dashbord(self):
            self.btn_category_2.clicked.connect(self.taps2)

        def Exit(self):
            self.btn_exit.clicked.connect(self.tabs3)


##############################
#    زرار الدخول

        def Login(self):
            pass


#############################
#            ازرار الادمن

        def Add_user(self):
            self.pushButton_5.clicked.connect(self.tap_edit_user)

        def Add_Category(self):
            self.pushButton_7.clicked.connect(self.tap_edit_category)
        def Add_Items(self):
            self.pushButton_8.clicked.connect(self.tap_edit_items)

        def save_add_category(self):
            pass
        def save_add_user(self):
            pass
        def save_add_items(self):
            pass
        def Delete_for_admin(self):
            pass
#################################
#              ازرار الاوردرات

        def btn_0(self):
            pass

        def btn_1(self):
            pass

        def btn_2(self):
            pass

        def btn_3(self):
            pass

        def btn_4(self):
            pass

        def btn_5(self):
            pass

        def btn_6(self):
            pass

        def btn_7(self):
            pass

        def btn_8(self):
            pass

        def btn_9(self):
            pass

        def btn_sum(self):
            pass

        def btn_qs(self):
            pass

        def btn_drb(self):
            pass

        def btn_tr7(self):
            pass
        def btn_ys(self):
            pass

        def savebtn(self):
            self.saveBtn.clicked.connect(self.writeSettings)

        def Browse(self):
            self.browseBtn.clicked.connect(self.setLogo)
        def taps(self):
            self.tab_main.setCurrentIndex(3)
            self.tab_main.tabBar().setVisible(False)
            self.btn_cashier.setVisible(False)
            self.btn_category.setVisible(False)
            self.btn_category_2.setVisible(False)
            #self.btn_exit.setVisible(False)




        def taps2(self):
           self.tab_main.setCurrentIndex(1)
        def tabs3(self):
            self.tab_main.setCurrentIndex(0)
        def import_logo(self):
            self.browseBtn.clicked.connect(self.setLogo)
        def tap_edit_user(self):
            self.tab_main.setCurrentIndex(2)
            self.tabWidget_2.setCurrentIndex(0)
        def tap_edit_category(self):
            self.tab_main.setCurrentIndex(2)
            self.tabWidget_2.setCurrentIndex(2)
        def tap_edit_items(self):
            self.tab_main.setCurrentIndex(2)
            self.tabWidget_2.setCurrentIndex(3)

        def setLogo(self):
            self.logoPath = QFileDialog.getOpenFileName(self, ("Open Image"), "",
                                                        ("Image Files (*.png *.jpg *.bmp *.svg *.jpeg)"))
            self.logoPath = self.logoPath[0]
            if self.logoPath != '':
                pixmap = QPixmap(self.logoPath)
                self.businessLogo.setPixmap(pixmap)

        def writeSettings(self):
            settings = {
                'logoPath': self.logoPath
            }
            try:
                with open('settings.json', 'w') as configsfile:
                    json.dump(settings, configsfile)
            except:
                QtWidgets.QMessageBox.warning(self, "Error",
                                              "Couldn't write the new settings.")
            else:
                QtWidgets.QMessageBox.information(self, "Successfully",
                                                  "successfully Upload Logo Item.")
            finally:
                self.taps()



def main():
            app = QApplication(sys.argv)
            window = MainApp()
            window.show()
            app.exec_()

if __name__ == '__main__':
            main()