from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import QIcon

class Ui_Error(object):
    def setupUi(self, Dialog):
        Dialog.setWindowIcon(QIcon('img/icon.png'))
        Dialog.setObjectName("Dialog")
        Dialog.resize(460, 210)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        Dialog.setMinimumSize(QtCore.QSize(460, 216))
        Dialog.setMaximumSize(QtCore.QSize(460, 216))
        Dialog.setStyleSheet("background-color: rgb(57, 37, 33);")
        Dialog.setModal(False)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout.setContentsMargins(18, 18, 18, 18)
        self.verticalLayout.setSpacing(18)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(5)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.Title = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(99)
        self.Title.setFont(font)
        self.Title.setStyleSheet("color: #FFFFFF;text-align: center;font-family: \"Calibri\";font-size: 22px;font-style: normal;font-weight: 800;")
        self.Title.setText("")
        self.Title.setObjectName("Title")
        self.horizontalLayout_2.addWidget(self.Title)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.Icon = QtWidgets.QLabel(Dialog)
        self.Icon.setMinimumSize(QtCore.QSize(30, 30))
        self.Icon.setMaximumSize(QtCore.QSize(30, 30))
        self.Icon.setStyleSheet("background-image: url(:/icon/img/error.svg);background-repeat: no-repeat;")
        self.Icon.setText("")
        self.Icon.setObjectName("Icon")
        self.horizontalLayout_2.addWidget(self.Icon)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.Subtitle = QtWidgets.QLabel(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Subtitle.sizePolicy().hasHeightForWidth())
        self.Subtitle.setSizePolicy(sizePolicy)
        self.Subtitle.setMinimumSize(QtCore.QSize(0, 0))
        self.Subtitle.setMaximumSize(QtCore.QSize(460, 16777215))
        self.Subtitle.setStyleSheet("color: #FFFFFF;text-align: center;font-family: \"Calibri\";font-size: 15px;font-style: normal;font-weight: 400;")
        self.Subtitle.setText("")
        self.Subtitle.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.Subtitle.setWordWrap(True)
        self.Subtitle.setObjectName("Subtitle")
        self.horizontalLayout_3.addWidget(self.Subtitle)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.ButtonCopy = QtWidgets.QPushButton(Dialog)
        self.ButtonCopy.setMaximumSize(QtCore.QSize(16777215, 225))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(-1)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(True)
        font.setWeight(99)
        self.ButtonCopy.setFont(font)
        self.ButtonCopy.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.ButtonCopy.setStyleSheet("background: transparent; color: #FFCD50; text-align: center;font-family: \"Calibri\";font-size: 16px;font-style: normal;font-weight: 800;")
        self.ButtonCopy.setObjectName("ButtonCopy")
        self.horizontalLayout.addWidget(self.ButtonCopy)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.ButtonContinue = QtWidgets.QPushButton(Dialog)
        self.ButtonContinue.setMinimumSize(QtCore.QSize(110, 40))
        self.ButtonContinue.setMaximumSize(QtCore.QSize(110, 40))
        self.ButtonContinue.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.ButtonContinue.setStyleSheet("QPushButton {border-radius: 5px;background: #FFCD50;color: #693D3B;text-align: center;font-family: \"Calibri\";font-size: 16px;font-style: normal;font-weight: 800;}QPushButton:hover {background-color: #FFD56C;}QPushButton:pressed {background-color: #FFCD50;}")
        self.ButtonContinue.setObjectName("ButtonContinue")
        self.horizontalLayout.addWidget(self.ButtonContinue)
        self.verticalLayout.addLayout(self.horizontalLayout)

        Dialog.setModal(True)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Error"))
        self.ButtonCopy.setText(_translate("Dialog", "Скопіювати"))
        self.ButtonContinue.setText(_translate("Dialog", "Продовжити"))

    # Відкриття діалогу
    def openDialog(self, center_x, center_y, title, err):
        self.dialog = QtWidgets.QDialog()
        center_x = round(center_x)
        center_y = round(center_y)
        self.dialog.move(center_x - 210, center_y - 108)

        self.setupUi(self.dialog)

        self.Title.setText(title)
        self.Subtitle.setText(err)

        # Прийняття діалогу
        def accept_dialog():
            self.dialog.accept()
        
        self.ButtonCopy.clicked.connect(self.copyToClipboard)
        self.ButtonContinue.clicked.connect(accept_dialog)
        
        self.dialog.show()
        self.dialog.exec_()

    # Скопіювати помилку
    def copyToClipboard(self):
        textToCopy = self.Subtitle.text()

        clipboard = QApplication.clipboard()
        clipboard.setText(textToCopy)
        
        self.ButtonCopy.setText("Скопійовано")

import resources