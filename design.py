# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(640, 480)
        MainWindow.setMinimumSize(QtCore.QSize(640, 480))
        MainWindow.setMaximumSize(QtCore.QSize(640, 480))
        MainWindow.setBaseSize(QtCore.QSize(640, 480))
        MainWindow.setTabletTracking(False)
        MainWindow.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        MainWindow.setAcceptDrops(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(10, 10, 621, 451))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setAccessibleName("")
        self.tab.setObjectName("tab")
        self.spinBox = QtWidgets.QSpinBox(self.tab)
        self.spinBox.setGeometry(QtCore.QRect(390, 57, 42, 22))
        self.spinBox.setStatusTip("")
        self.spinBox.setWhatsThis("")
        self.spinBox.setAutoFillBackground(False)
        self.spinBox.setWrapping(True)
        self.spinBox.setReadOnly(False)
        self.spinBox.setMinimum(4)
        self.spinBox.setMaximum(10)
        self.spinBox.setObjectName("spinBox")
        self.pushButton_GenPass = QtWidgets.QPushButton(self.tab)
        self.pushButton_GenPass.setGeometry(QtCore.QRect(190, 110, 241, 23))
        self.pushButton_GenPass.setObjectName("pushButton_GenPass")
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(190, 60, 191, 16))
        self.label.setObjectName("label")
        self.pushButton_SaveFile_Pass = QtWidgets.QPushButton(self.tab)
        self.pushButton_SaveFile_Pass.setGeometry(QtCore.QRect(190, 320, 241, 23))
        self.pushButton_SaveFile_Pass.setObjectName("pushButton_SaveFile_Pass")
        self.textEdit_PassList = QtWidgets.QTextEdit(self.tab)
        self.textEdit_PassList.setGeometry(QtCore.QRect(190, 140, 241, 171))
        self.textEdit_PassList.setReadOnly(True)
        self.textEdit_PassList.setObjectName("textEdit_PassList")
        self.label_4 = QtWidgets.QLabel(self.tab)
        self.label_4.setGeometry(QtCore.QRect(190, 85, 91, 16))
        self.label_4.setObjectName("label_4")
        self.comboBox_PassType = QtWidgets.QComboBox(self.tab)
        self.comboBox_PassType.setGeometry(QtCore.QRect(286, 80, 69, 22))
        self.comboBox_PassType.setObjectName("comboBox_PassType")
        self.comboBox_PassType.addItem("")
        self.comboBox_PassType.addItem("")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.label_2 = QtWidgets.QLabel(self.tab_2)
        self.label_2.setGeometry(QtCore.QRect(180, 60, 47, 13))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.tab_2)
        self.label_3.setGeometry(QtCore.QRect(182, 178, 47, 13))
        self.label_3.setObjectName("label_3")
        self.lineEdit_Key = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_Key.setGeometry(QtCore.QRect(220, 174, 131, 20))
        self.lineEdit_Key.setObjectName("lineEdit_Key")
        self.pushButton_Shifr = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_Shifr.setGeometry(QtCore.QRect(180, 200, 111, 23))
        self.pushButton_Shifr.setObjectName("pushButton_Shifr")
        self.pushButton_DeShifr = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_DeShifr.setGeometry(QtCore.QRect(310, 200, 111, 23))
        self.pushButton_DeShifr.setObjectName("pushButton_DeShifr")
        self.pushButton_SaveFile_Shifr = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_SaveFile_Shifr.setGeometry(QtCore.QRect(180, 320, 241, 23))
        self.pushButton_SaveFile_Shifr.setObjectName("pushButton_SaveFile_Shifr")
        self.textEdit_Text = QtWidgets.QTextEdit(self.tab_2)
        self.textEdit_Text.setGeometry(QtCore.QRect(180, 80, 241, 81))
        self.textEdit_Text.setObjectName("textEdit_Text")
        self.textEdit_Shifr = QtWidgets.QTextEdit(self.tab_2)
        self.textEdit_Shifr.setGeometry(QtCore.QRect(180, 230, 241, 81))
        self.textEdit_Shifr.setReadOnly(True)
        self.textEdit_Shifr.setObjectName("textEdit_Shifr")
        self.comboBox_shifrLang = QtWidgets.QComboBox(self.tab_2)
        self.comboBox_shifrLang.setGeometry(QtCore.QRect(352, 173, 69, 22))
        self.comboBox_shifrLang.setObjectName("comboBox_shifrLang")
        self.comboBox_shifrLang.addItem("")
        self.comboBox_shifrLang.addItem("")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.groupBox_UserInf = QtWidgets.QGroupBox(self.tab_3)
        self.groupBox_UserInf.setGeometry(QtCore.QRect(70, 60, 221, 121))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.groupBox_UserInf.setFont(font)
        self.groupBox_UserInf.setObjectName("groupBox_UserInf")
        self.checkBox_UserInf_EditStatus = QtWidgets.QCheckBox(self.groupBox_UserInf)
        self.checkBox_UserInf_EditStatus.setGeometry(QtCore.QRect(10, 60, 201, 20))
        self.checkBox_UserInf_EditStatus.setObjectName("checkBox_UserInf_EditStatus")
        self.label_47 = QtWidgets.QLabel(self.groupBox_UserInf)
        self.label_47.setGeometry(QtCore.QRect(20, 34, 60, 16))
        self.label_47.setObjectName("label_47")
        self.comboBox_UserInf_User = QtWidgets.QComboBox(self.groupBox_UserInf)
        self.comboBox_UserInf_User.setGeometry(QtCore.QRect(60, 30, 141, 26))
        self.comboBox_UserInf_User.setObjectName("comboBox_UserInf_User")
        self.comboBox_UserInf_User.addItem("")
        self.comboBox_UserInf_User.addItem("")
        self.comboBox_UserInf_User.addItem("")
        self.comboBox_UserInf_User.addItem("")
        self.comboBox_UserInf_User.addItem("")
        self.pushButton_UserInf_Cheak = QtWidgets.QPushButton(self.groupBox_UserInf)
        self.pushButton_UserInf_Cheak.setGeometry(QtCore.QRect(55, 84, 113, 32))
        self.pushButton_UserInf_Cheak.setObjectName("pushButton_UserInf_Cheak")
        self.groupBox_FileLook = QtWidgets.QGroupBox(self.tab_3)
        self.groupBox_FileLook.setGeometry(QtCore.QRect(320, 60, 221, 201))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_FileLook.sizePolicy().hasHeightForWidth())
        self.groupBox_FileLook.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.groupBox_FileLook.setFont(font)
        self.groupBox_FileLook.setFlat(False)
        self.groupBox_FileLook.setObjectName("groupBox_FileLook")
        self.checkBox_FileLook_Ban = QtWidgets.QCheckBox(self.groupBox_FileLook)
        self.checkBox_FileLook_Ban.setGeometry(QtCore.QRect(40, 70, 151, 20))
        self.checkBox_FileLook_Ban.setCheckable(False)
        self.checkBox_FileLook_Ban.setObjectName("checkBox_FileLook_Ban")
        self.checkBox_FileLook_Write = QtWidgets.QCheckBox(self.groupBox_FileLook)
        self.checkBox_FileLook_Write.setGeometry(QtCore.QRect(40, 90, 151, 20))
        self.checkBox_FileLook_Write.setCheckable(False)
        self.checkBox_FileLook_Write.setObjectName("checkBox_FileLook_Write")
        self.checkBox_FileLook_Read = QtWidgets.QCheckBox(self.groupBox_FileLook)
        self.checkBox_FileLook_Read.setGeometry(QtCore.QRect(40, 110, 151, 20))
        self.checkBox_FileLook_Read.setCheckable(False)
        self.checkBox_FileLook_Read.setObjectName("checkBox_FileLook_Read")
        self.checkBox_FileLook_Full = QtWidgets.QCheckBox(self.groupBox_FileLook)
        self.checkBox_FileLook_Full.setGeometry(QtCore.QRect(40, 130, 151, 20))
        self.checkBox_FileLook_Full.setCheckable(False)
        self.checkBox_FileLook_Full.setObjectName("checkBox_FileLook_Full")
        self.checkBox_FileLook_SendPrav = QtWidgets.QCheckBox(self.groupBox_FileLook)
        self.checkBox_FileLook_SendPrav.setGeometry(QtCore.QRect(40, 150, 151, 20))
        self.checkBox_FileLook_SendPrav.setCheckable(False)
        self.checkBox_FileLook_SendPrav.setTristate(False)
        self.checkBox_FileLook_SendPrav.setObjectName("checkBox_FileLook_SendPrav")
        self.label_42 = QtWidgets.QLabel(self.groupBox_FileLook)
        self.label_42.setGeometry(QtCore.QRect(41, 44, 60, 16))
        self.label_42.setObjectName("label_42")
        self.comboBox_FileLook_File = QtWidgets.QComboBox(self.groupBox_FileLook)
        self.comboBox_FileLook_File.setGeometry(QtCore.QRect(80, 40, 111, 26))
        self.comboBox_FileLook_File.setObjectName("comboBox_FileLook_File")
        self.comboBox_FileLook_File.addItem("")
        self.comboBox_FileLook_File.addItem("")
        self.comboBox_FileLook_File.addItem("")
        self.comboBox_FileLook_File.addItem("")
        self.groupBox_FilePravEdit = QtWidgets.QGroupBox(self.tab_3)
        self.groupBox_FilePravEdit.setGeometry(QtCore.QRect(70, 180, 221, 191))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(False)
        font.setWeight(50)
        self.groupBox_FilePravEdit.setFont(font)
        self.groupBox_FilePravEdit.setFlat(False)
        self.groupBox_FilePravEdit.setCheckable(False)
        self.groupBox_FilePravEdit.setObjectName("groupBox_FilePravEdit")
        self.comboBox_FilePravEdit_User = QtWidgets.QComboBox(self.groupBox_FilePravEdit)
        self.comboBox_FilePravEdit_User.setGeometry(QtCore.QRect(57, 20, 141, 26))
        self.comboBox_FilePravEdit_User.setObjectName("comboBox_FilePravEdit_User")
        self.comboBox_FilePravEdit_User.addItem("")
        self.comboBox_FilePravEdit_User.addItem("")
        self.comboBox_FilePravEdit_User.addItem("")
        self.comboBox_FilePravEdit_User.addItem("")
        self.comboBox_FilePravEdit_User.addItem("")
        self.label_43 = QtWidgets.QLabel(self.groupBox_FilePravEdit)
        self.label_43.setGeometry(QtCore.QRect(17, 24, 60, 16))
        self.label_43.setObjectName("label_43")
        self.label_44 = QtWidgets.QLabel(self.groupBox_FilePravEdit)
        self.label_44.setGeometry(QtCore.QRect(17, 54, 60, 16))
        self.label_44.setObjectName("label_44")
        self.comboBox_FilePravEdit_File = QtWidgets.QComboBox(self.groupBox_FilePravEdit)
        self.comboBox_FilePravEdit_File.setGeometry(QtCore.QRect(57, 50, 141, 26))
        self.comboBox_FilePravEdit_File.setObjectName("comboBox_FilePravEdit_File")
        self.comboBox_FilePravEdit_File.addItem("")
        self.comboBox_FilePravEdit_File.addItem("")
        self.comboBox_FilePravEdit_File.addItem("")
        self.comboBox_FilePravEdit_File.addItem("")
        self.checkBox_FilePravEdit_SendPrav = QtWidgets.QCheckBox(self.groupBox_FilePravEdit)
        self.checkBox_FilePravEdit_SendPrav.setGeometry(QtCore.QRect(40, 160, 151, 20))
        self.checkBox_FilePravEdit_SendPrav.setObjectName("checkBox_FilePravEdit_SendPrav")
        self.checkBox_FilePravEdit_Write = QtWidgets.QCheckBox(self.groupBox_FilePravEdit)
        self.checkBox_FilePravEdit_Write.setGeometry(QtCore.QRect(40, 100, 151, 20))
        self.checkBox_FilePravEdit_Write.setObjectName("checkBox_FilePravEdit_Write")
        self.checkBox_FilePravEdit_Read = QtWidgets.QCheckBox(self.groupBox_FilePravEdit)
        self.checkBox_FilePravEdit_Read.setGeometry(QtCore.QRect(40, 120, 151, 20))
        self.checkBox_FilePravEdit_Read.setObjectName("checkBox_FilePravEdit_Read")
        self.checkBox_FilePravEdit_Ban = QtWidgets.QCheckBox(self.groupBox_FilePravEdit)
        self.checkBox_FilePravEdit_Ban.setGeometry(QtCore.QRect(40, 80, 151, 20))
        self.checkBox_FilePravEdit_Ban.setObjectName("checkBox_FilePravEdit_Ban")
        self.checkBox_FilePravEdit_Full = QtWidgets.QCheckBox(self.groupBox_FilePravEdit)
        self.checkBox_FilePravEdit_Full.setGeometry(QtCore.QRect(40, 140, 151, 20))
        self.checkBox_FilePravEdit_Full.setObjectName("checkBox_FilePravEdit_Full")
        self.groupBox_ChangePrav = QtWidgets.QGroupBox(self.tab_3)
        self.groupBox_ChangePrav.setGeometry(QtCore.QRect(320, 260, 221, 111))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.groupBox_ChangePrav.setFont(font)
        self.groupBox_ChangePrav.setObjectName("groupBox_ChangePrav")
        self.label_45 = QtWidgets.QLabel(self.groupBox_ChangePrav)
        self.label_45.setGeometry(QtCore.QRect(20, 64, 121, 16))
        self.label_45.setObjectName("label_45")
        self.label_46 = QtWidgets.QLabel(self.groupBox_ChangePrav)
        self.label_46.setGeometry(QtCore.QRect(20, 34, 60, 16))
        self.label_46.setObjectName("label_46")
        self.comboBox_ChangePrav_User = QtWidgets.QComboBox(self.groupBox_ChangePrav)
        self.comboBox_ChangePrav_User.setGeometry(QtCore.QRect(60, 30, 141, 26))
        self.comboBox_ChangePrav_User.setObjectName("comboBox_ChangePrav_User")
        self.comboBox_ChangePrav_User.addItem("")
        self.comboBox_ChangePrav_User.addItem("")
        self.comboBox_ChangePrav_User.addItem("")
        self.comboBox_ChangePrav_User.addItem("")
        self.comboBox_ChangePrav_User.addItem("")
        self.comboBox_ChangePrav_Type = QtWidgets.QComboBox(self.groupBox_ChangePrav)
        self.comboBox_ChangePrav_Type.setGeometry(QtCore.QRect(130, 60, 71, 26))
        self.comboBox_ChangePrav_Type.setObjectName("comboBox_ChangePrav_Type")
        self.comboBox_ChangePrav_Type.addItem("")
        self.comboBox_ChangePrav_Type.addItem("")
        self.tabWidget.addTab(self.tab_3, "")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Гильфанов 612 3в."))
        self.pushButton_GenPass.setText(_translate("MainWindow", "Сгенерировать пароли"))
        self.label.setText(_translate("MainWindow", "Введите число символов в пароле:"))
        self.pushButton_SaveFile_Pass.setText(_translate("MainWindow", "Сохранить в файл"))
        self.label_4.setText(_translate("MainWindow", "Спец. символы:"))
        self.comboBox_PassType.setItemText(0, _translate("MainWindow", "Да"))
        self.comboBox_PassType.setItemText(1, _translate("MainWindow", "Нет"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Генератор паролей"))
        self.label_2.setText(_translate("MainWindow", "Фраза:"))
        self.label_3.setText(_translate("MainWindow", "Ключ:"))
        self.pushButton_Shifr.setText(_translate("MainWindow", "Шифровать"))
        self.pushButton_DeShifr.setText(_translate("MainWindow", "Дешифровать"))
        self.pushButton_SaveFile_Shifr.setText(_translate("MainWindow", "Сохранить в файл"))
        self.comboBox_shifrLang.setItemText(0, _translate("MainWindow", "rus"))
        self.comboBox_shifrLang.setItemText(1, _translate("MainWindow", "en"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Шифр Виженера"))
        self.groupBox_UserInf.setTitle(_translate("MainWindow", "Пользователь"))
        self.checkBox_UserInf_EditStatus.setText(_translate("MainWindow", "Редактирования прав"))
        self.label_47.setText(_translate("MainWindow", "Юзер:"))
        self.comboBox_UserInf_User.setItemText(0, _translate("MainWindow", "Admin"))
        self.comboBox_UserInf_User.setItemText(1, _translate("MainWindow", "User1"))
        self.comboBox_UserInf_User.setItemText(2, _translate("MainWindow", "User2"))
        self.comboBox_UserInf_User.setItemText(3, _translate("MainWindow", "User3"))
        self.comboBox_UserInf_User.setItemText(4, _translate("MainWindow", "User4"))
        self.pushButton_UserInf_Cheak.setText(_translate("MainWindow", "Выбрать"))
        self.groupBox_FileLook.setTitle(_translate("MainWindow", "Просмотр прав доступа"))
        self.checkBox_FileLook_Ban.setText(_translate("MainWindow", "Полный запрет"))
        self.checkBox_FileLook_Write.setText(_translate("MainWindow", "Запись"))
        self.checkBox_FileLook_Read.setText(_translate("MainWindow", "Чтение"))
        self.checkBox_FileLook_Full.setText(_translate("MainWindow", "Полный доступ"))
        self.checkBox_FileLook_SendPrav.setText(_translate("MainWindow", "Передача прав"))
        self.label_42.setText(_translate("MainWindow", "Файл:"))
        self.comboBox_FileLook_File.setItemText(0, _translate("MainWindow", "File1"))
        self.comboBox_FileLook_File.setItemText(1, _translate("MainWindow", "File2"))
        self.comboBox_FileLook_File.setItemText(2, _translate("MainWindow", "File3"))
        self.comboBox_FileLook_File.setItemText(3, _translate("MainWindow", "File4"))
        self.groupBox_FilePravEdit.setTitle(_translate("MainWindow", "Управление доступом к файлам"))
        self.comboBox_FilePravEdit_User.setItemText(0, _translate("MainWindow", "Admin"))
        self.comboBox_FilePravEdit_User.setItemText(1, _translate("MainWindow", "User1"))
        self.comboBox_FilePravEdit_User.setItemText(2, _translate("MainWindow", "User2"))
        self.comboBox_FilePravEdit_User.setItemText(3, _translate("MainWindow", "User3"))
        self.comboBox_FilePravEdit_User.setItemText(4, _translate("MainWindow", "User4"))
        self.label_43.setText(_translate("MainWindow", "Юзер:"))
        self.label_44.setText(_translate("MainWindow", "Файл:"))
        self.comboBox_FilePravEdit_File.setItemText(0, _translate("MainWindow", "File1"))
        self.comboBox_FilePravEdit_File.setItemText(1, _translate("MainWindow", "File2"))
        self.comboBox_FilePravEdit_File.setItemText(2, _translate("MainWindow", "File3"))
        self.comboBox_FilePravEdit_File.setItemText(3, _translate("MainWindow", "File4"))
        self.checkBox_FilePravEdit_SendPrav.setText(_translate("MainWindow", "Передача прав"))
        self.checkBox_FilePravEdit_Write.setText(_translate("MainWindow", "Запись"))
        self.checkBox_FilePravEdit_Read.setText(_translate("MainWindow", "Чтение"))
        self.checkBox_FilePravEdit_Ban.setText(_translate("MainWindow", "Полный запрет"))
        self.checkBox_FilePravEdit_Full.setText(_translate("MainWindow", "Полный доступ"))
        self.groupBox_ChangePrav.setTitle(_translate("MainWindow", "Права пользователей"))
        self.label_45.setText(_translate("MainWindow", "Ред. прав польз.:"))
        self.label_46.setText(_translate("MainWindow", "Юзер:"))
        self.comboBox_ChangePrav_User.setItemText(0, _translate("MainWindow", "Admin"))
        self.comboBox_ChangePrav_User.setItemText(1, _translate("MainWindow", "User1"))
        self.comboBox_ChangePrav_User.setItemText(2, _translate("MainWindow", "User2"))
        self.comboBox_ChangePrav_User.setItemText(3, _translate("MainWindow", "User3"))
        self.comboBox_ChangePrav_User.setItemText(4, _translate("MainWindow", "User4"))
        self.comboBox_ChangePrav_Type.setItemText(0, _translate("MainWindow", "Да"))
        self.comboBox_ChangePrav_Type.setItemText(1, _translate("MainWindow", "Нет"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Права доступа"))
