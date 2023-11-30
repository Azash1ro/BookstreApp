from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon

class Ui_Info(object):
    def setupUi(self, Form):
        Form.setWindowIcon(QIcon('img/icon.png'))
        Form.setObjectName("Form")
        Form.resize(500, 330)
        Form.setMinimumSize(QtCore.QSize(500, 330))
        Form.setMaximumSize(QtCore.QSize(500, 330))
        Form.setStyleSheet("background-color: #745146;")
        self.horizontalLayout = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout.setContentsMargins(20, 20, 20, 20)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(Form)
        self.label.setStyleSheet("font: 15px \"Calibri\";color: rgb(255, 255, 255);font-weight: 800;")
        self.label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Bookstore"))
        self.label.setText(_translate("Form", 
        "<h3 style=\"line-height: 1.2; color: #FFCD50;\"><strong>Про Програму</strong></h3>\n"
        "<p>Ласкаво просимо до вашого надійного помічника у книготоргівлі! Наша програма - це компактний інструмент для управління продажами книг в вашій книгарні.</p>\n"
        "\n"
        "<h3 style=\"line-height: 1.2;color: #FFCD50;\"><strong>Основні функції:</strong></h3>\n"
        "<ul>\n"
        "    <li style=\"margin-bottom: 10px;\">\n"
        "        <strong>Каталог книг:</strong><br> Додавання та редагування книг з нескладністю.\n"
        "    </li>\n"
        "    <li style=\"margin-bottom: 10px;\">\n"
        "        <strong>Замовлення:</strong><br> Відстеження замовлень в режимі реального часу.\n"
        "    </li>\n"
        "    <li>\n"
        "        <strong>Клієнтська база:</strong><br> Зберігайте дані про клієнтів та їхні покупки.\n"
        "    </li>\n"
        "</ul>"))
    
    # Відкриття діалогу
    def open(self, center_x, center_y):
        self.Form = QtWidgets.QWidget()
        center_x = round(center_x)
        center_y = round(center_y)
        self.Form.move(center_x - 250, center_y - 175)
        self.setupUi(self.Form)
        self.Form.show()
