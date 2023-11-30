from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Delete(object):
    def __init__(self, id_value):
        self.id_value = id_value

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(258, 163)
        Dialog.setMinimumSize(QtCore.QSize(250, 163))
        Dialog.setMaximumSize(QtCore.QSize(250, 163))
        Dialog.setStyleSheet("background-color: rgb(57, 37, 33);")
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setContentsMargins(15, 15, 15, 15)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_Id = QtWidgets.QLabel(Dialog)
        self.label_Id.setStyleSheet("background: transparent;color: #FFCD50;font-family: \"Calibri\";font-size: 16px;font-style: normal;font-weight: 700;")
        self.label_Id.setAlignment(QtCore.Qt.AlignCenter)
        self.label_Id.setWordWrap(True)
        self.label_Id.setObjectName("label_Id")
        self.verticalLayout.addWidget(self.label_Id)
        self.labelText = QtWidgets.QLabel(Dialog)
        self.labelText.setStyleSheet("background: transparent;color: white;font-family: \"Calibri\";font-size: 16px;font-style: normal;font-weight: 700;")
        self.labelText.setAlignment(QtCore.Qt.AlignCenter)
        self.labelText.setWordWrap(True)
        self.labelText.setObjectName("labelText")
        self.verticalLayout.addWidget(self.labelText)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(-1, 15, -1, -1)
        self.horizontalLayout.setSpacing(16)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.buttonYes = QtWidgets.QPushButton(Dialog)
        self.buttonYes.setMinimumSize(QtCore.QSize(92, 40))
        self.buttonYes.setMaximumSize(QtCore.QSize(92, 40))
        self.buttonYes.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.buttonYes.setStyleSheet("QPushButton {border-radius: 5px;background: #FFCD50;color: #693D3B;text-align: center;font-family: \"Calibri\";font-size: 16px;font-style: normal;font-weight: 800;}QPushButton:hover {background-color: #FFD56C;}QPushButton:pressed {background-color: #FFCD50;}")
        self.buttonYes.setObjectName("buttonYes")
        self.horizontalLayout.addWidget(self.buttonYes)
        self.buttonNo = QtWidgets.QPushButton(Dialog)
        self.buttonNo.setMinimumSize(QtCore.QSize(92, 40))
        self.buttonNo.setMaximumSize(QtCore.QSize(92, 40))
        self.buttonNo.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.buttonNo.setStyleSheet("QPushButton {border-radius: 5px;background: #FFCD50;color: #693D3B;text-align: center;font-family: \"Calibri\";font-size: 16px;font-style: normal;font-weight: 800;}QPushButton:hover {background-color: #FFD56C;}QPushButton:pressed {background-color: #FFCD50;}")
        self.buttonNo.setObjectName("buttonNo")
        self.horizontalLayout.addWidget(self.buttonNo)
        self.verticalLayout.addLayout(self.horizontalLayout)

        Dialog.setWindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.Dialog)
        Dialog.setModal(True)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        self.buttonNo.clicked.connect(self.closeDialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Bookstore"))
        self.label_Id.setText(_translate("Dialog", "ID " + self.id_value))
        self.labelText.setText(_translate("Dialog", "Ви дійсно бажаєте видалити цей запис?"))
        self.buttonYes.setText(_translate("Dialog", "Так"))
        self.buttonNo.setText(_translate("Dialog", "Ні"))

    # Відкриття діалогу та відстеження натискання кнопки Так
    def openDialog(self, center_x, center_y):
        self.dialog = QtWidgets.QDialog()
        center_x = round(center_x)
        center_y = round(center_y)
        self.dialog.move(center_x - 129, center_y - 81)
        self.setupUi(self.dialog)
        
        result = 0 

        def accept_dialog():
            nonlocal result 
            result = 1 
            self.dialog.accept()
        
        self.buttonYes.clicked.connect(accept_dialog)
        
        self.dialog.show()
        self.dialog.exec_()

        return result

    # Закриття діалогу
    def closeDialog(self):
        self.dialog.close()