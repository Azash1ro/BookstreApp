from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
from datetime import datetime
from Ui_Error import Ui_Error
import mysql.connector

class Ui_Edit(object):
    def __init__(self, connection, tableName, mode):
        self.connection = connection
        self.tableName = tableName
        self.mode = mode

    def setupUi(self, Dialog):
        color_error = "#FF0000"
        self.defaultStyleField = "QLineEdit {color: #F4E0AE;text-align: center;font-family: \"Calibri\";font-size: 16px;font-style: normal;font-weight: 400;padding:  0 12px 0 12px;border-radius: 5px;border: 1px solid #FFCD50;background: transparent;}QLineEdit:hover {border: 1.5px solid #FFCD50;}QLineEdit:focus {border: 1.5px solid #FFCD50;}\n"
        self.errorStyleField = "QLineEdit {color: #F4E0AE;text-align: center;font-family: \"Calibri\";font-size: 16px;font-style: normal;font-weight: 400;padding:  0 12px 0 12px;border-radius: 5px;border: 1.2px solid " + color_error + ";background: transparent;}QLineEdit:hover {border: 1.5px solid " + color_error + ";}QLineEdit:focus {border: 1.5px solid " + color_error + ";}\n"
        Dialog.setWindowIcon(QIcon('img/icon.png'))
        Dialog.setObjectName("Dialog")

        self.dialogHeight = 492
        match self.tableName:
            case "customers":
                self.dialogHeight = 380
            case "sales":
                self.dialogHeight = 436

        Dialog.resize(250, self.dialogHeight)
        Dialog.setMinimumSize(QtCore.QSize(250, self.dialogHeight))
        Dialog.setMaximumSize(QtCore.QSize(250, self.dialogHeight))
        Dialog.setStyleSheet("background-color: rgb(116, 81, 70);")
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setContentsMargins(30, 30, 30, 30)
        self.verticalLayout.setSpacing(16)
        self.verticalLayout.setObjectName("verticalLayout")

        self.Field1 = QtWidgets.QLineEdit(Dialog)
        self.Field1.setMinimumSize(QtCore.QSize(190, 40))
        self.Field1.setMaximumSize(QtCore.QSize(190, 40))
        self.Field1.setStyleSheet("QLineEdit {color: #F4E0AE;text-align: center;font-family: \"Calibri\";font-size: 16px;font-style: normal;font-weight: 400;padding:  0 12px 0 12px;border-radius: 5px;border: 1px solid #FFCD50;background: transparent;}QLineEdit:hover {border: 1.5px solid #FFCD50;}QLineEdit:focus {border: 1.5px solid #FFCD50;}")
        self.Field1.setObjectName("Field1")
        self.verticalLayout.addWidget(self.Field1)

        self.Field2 = QtWidgets.QLineEdit(Dialog)
        self.Field2.setMinimumSize(QtCore.QSize(190, 40))
        self.Field2.setMaximumSize(QtCore.QSize(190, 40))
        self.Field2.setStyleSheet("QLineEdit {color: #F4E0AE;text-align: center;font-family: \"Calibri\";font-size: 16px;font-style: normal;font-weight: 400;padding:  0 12px 0 12px;border-radius: 5px;border: 1px solid #FFCD50;background: transparent;}QLineEdit:hover {border: 1.5px solid #FFCD50;}QLineEdit:focus {border: 1.5px solid #FFCD50;}")
        self.Field2.setObjectName("Field2")
        self.verticalLayout.addWidget(self.Field2)

        self.Field3 = QtWidgets.QLineEdit(Dialog)
        self.Field3.setMinimumSize(QtCore.QSize(190, 40))
        self.Field3.setMaximumSize(QtCore.QSize(190, 40))
        self.Field3.setStyleSheet("QLineEdit {color: #F4E0AE;text-align: center;font-family: \"Calibri\";font-size: 16px;font-style: normal;font-weight: 400;padding:  0 12px 0 12px;border-radius: 5px;border: 1px solid #FFCD50;background: transparent;}QLineEdit:hover {border: 1.5px solid #FFCD50;}QLineEdit:focus {border: 1.5px solid #FFCD50;}")
        self.Field3.setObjectName("Field3")
        self.verticalLayout.addWidget(self.Field3)

        self.Field4 = QtWidgets.QLineEdit(Dialog)
        self.Field4.setMinimumSize(QtCore.QSize(190, 40))
        self.Field4.setMaximumSize(QtCore.QSize(190, 40))
        self.Field4.setStyleSheet("QLineEdit {color: #F4E0AE;text-align: center;font-family: \"Calibri\";font-size: 16px;font-style: normal;font-weight: 400;padding:  0 12px 0 12px;border-radius: 5px;border: 1px solid #FFCD50;background: transparent;}QLineEdit:hover {border: 1.5px solid #FFCD50;}QLineEdit:focus {border: 1.5px solid #FFCD50;}")
        self.Field4.setObjectName("Field4")
        self.verticalLayout.addWidget(self.Field4)

        self.Field5 = QtWidgets.QLineEdit(Dialog)
        self.Field5.setMinimumSize(QtCore.QSize(190, 40))
        self.Field5.setMaximumSize(QtCore.QSize(190, 40))
        self.Field5.setStyleSheet("QLineEdit {color: #F4E0AE;text-align: center;font-family: \"Calibri\";font-size: 16px;font-style: normal;font-weight: 400;padding:  0 12px 0 12px;border-radius: 5px;border: 1px solid #FFCD50;background: transparent;}QLineEdit:hover {border: 1.5px solid #FFCD50;}QLineEdit:focus {border: 1.5px solid #FFCD50;}")
        self.Field5.setObjectName("Field5")
        self.verticalLayout.addWidget(self.Field5)

        self.Field6 = QtWidgets.QLineEdit(Dialog)
        self.Field6.setMinimumSize(QtCore.QSize(190, 40))
        self.Field6.setMaximumSize(QtCore.QSize(190, 40))
        self.Field6.setStyleSheet("QLineEdit {color: #F4E0AE;text-align: center;font-family: \"Calibri\";font-size: 16px;font-style: normal;font-weight: 400;padding:  0 12px 0 12px;border-radius: 5px;border: 1px solid #FFCD50;background: transparent;}QLineEdit:hover {border: 1.5px solid #FFCD50;}QLineEdit:focus {border: 1.5px solid #FFCD50;}")
        self.Field6.setObjectName("Field6")
        self.verticalLayout.addWidget(self.Field6)

        self.Field7 = QtWidgets.QLineEdit(Dialog)
        self.Field7.setMinimumSize(QtCore.QSize(190, 40))
        self.Field7.setMaximumSize(QtCore.QSize(190, 40))
        self.Field7.setStyleSheet("QLineEdit {color: #F4E0AE;text-align: center;font-family: \"Calibri\";font-size: 16px;font-style: normal;font-weight: 400;padding:  0 12px 0 12px;border-radius: 5px;border: 1px solid #FFCD50;background: transparent;}QLineEdit:hover {border: 1.5px solid #FFCD50;}QLineEdit:focus {border: 1.5px solid #FFCD50;}")
        self.Field7.setObjectName("Field7")
        self.verticalLayout.addWidget(self.Field7)

        self.buttonAdd = QtWidgets.QPushButton(Dialog)
        self.buttonAdd.setMinimumSize(QtCore.QSize(190, 40))
        self.buttonAdd.setMaximumSize(QtCore.QSize(190, 40))
        self.buttonAdd.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.buttonAdd.setStyleSheet("QPushButton {border-radius: 5px;background: #FFCD50;color: #693D3B;text-align: center;font-family: \"Calibri\";font-size: 16px;font-style: normal;font-weight: 800;}QPushButton:hover {background-color: #FFD56C;}QPushButton:pressed {background-color: #FFCD50;}")
        self.buttonAdd.setObjectName("buttonAdd")
        self.verticalLayout.addWidget(self.buttonAdd)

        self.buttonUpdate = QtWidgets.QPushButton(Dialog)
        self.buttonUpdate.setMinimumSize(QtCore.QSize(190, 40))
        self.buttonUpdate.setMaximumSize(QtCore.QSize(190, 40))
        self.buttonUpdate.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.buttonUpdate.setStyleSheet("QPushButton {border-radius: 5px;background: #FFCD50;color: #693D3B;text-align: center;font-family: \"Calibri\";font-size: 16px;font-style: normal;font-weight: 800;}QPushButton:hover {background-color: #FFD56C;}QPushButton:pressed {background-color: #FFCD50;}")
        self.buttonUpdate.setObjectName("buttonUpdate")
        self.verticalLayout.addWidget(self.buttonUpdate)

        match self.tableName:
            case "customers":
                self.Field6.setVisible(False)
                self.Field7.setVisible(False)
            case "sales":
                self.Field7.setVisible(False)

        match self.mode:
            case "Add":
                self.buttonUpdate.setVisible(False)
            case "Update":
                self.buttonAdd.setVisible(False)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        match self.tableName:
            case "customers":
                self.Field1.setPlaceholderText(_translate("Dialog", "Ім'я"))
                self.Field2.setPlaceholderText(_translate("Dialog", "Прізвище"))
                self.Field3.setPlaceholderText(_translate("Dialog", "Email"))
                self.Field4.setPlaceholderText(_translate("Dialog", "Телефон"))
                self.Field5.setPlaceholderText(_translate("Dialog", "Адреса"))
            case "sales":
                self.Field1.setPlaceholderText(_translate("Dialog", "ID книги"))
                self.Field2.setPlaceholderText(_translate("Dialog", "ID клієнта"))
                self.Field3.setPlaceholderText(_translate("Dialog", "Кількість куплених книг"))
                self.Field4.setPlaceholderText(_translate("Dialog", "Загальна вартість"))
                self.Field5.setPlaceholderText(_translate("Dialog", "Дата продажу (YYYY-MM-DD)"))
                self.Field6.setPlaceholderText(_translate("Dialog", "Спосіб оплати"))
            case "books":
                self.Field1.setPlaceholderText(_translate("Dialog", "Назва"))
                self.Field2.setPlaceholderText(_translate("Dialog", "Автор"))
                self.Field3.setPlaceholderText(_translate("Dialog", "Жанр"))
                self.Field4.setPlaceholderText(_translate("Dialog", "Рік видання"))
                self.Field5.setPlaceholderText(_translate("Dialog", "Видатник"))
                self.Field6.setPlaceholderText(_translate("Dialog", "Ціна за одиницю"))
                self.Field7.setPlaceholderText(_translate("Dialog", "Кількість"))
        
        Dialog.setWindowTitle(_translate("Dialog", "Bookstore"))
        self.buttonAdd.setText(_translate("Dialog", "Додати запис"))
        self.buttonUpdate.setText(_translate("Dialog", "Змінити запис"))

    # Відкриваємо диалогове вікно
    def openDialog(self, center_x, center_y, id_value):
        self.dialog = QtWidgets.QDialog()
        center_x = round(center_x)
        center_y = round(center_y)

        self.dialog.move(center_x - 125, center_y - 252)
        self.setupUi(self.dialog)

        # Усі QLineEdit
        fields_mapping = {
            "books": [self.Field1, self.Field2, self.Field3, self.Field4, self.Field5, self.Field6, self.Field7],
            "customers": [self.Field1, self.Field2, self.Field3, self.Field4, self.Field5],
            "sales": [self.Field1, self.Field2, self.Field3, self.Field4, self.Field5, self.Field6]
        }

        self.fields_to_check = fields_mapping.get(self.tableName, [])

        if self.mode == "Update":
            # Отримаємо потрібний рядок за id
            query = f"SELECT * FROM {self.tableName} WHERE id = {id_value}"
            cursor = self.connection.cursor()
            cursor.execute(query)
            result = cursor.fetchone()

            if result:
                # Встановлюємо значення у відповідні поля
                for field, value in zip(self.fields_to_check, result[1:]):
                    field.setText(str(value))

            cursor.close()

        self.result = 0 

        self.buttonAdd.clicked.connect(self.AddNewRow)
        self.buttonUpdate.clicked.connect(lambda: self.EditRow(id_value))

        self.dialog.show()
        self.dialog.exec_() 
        return self.result

    # Додаємо новий запис
    def AddNewRow(self):
        if self.validateAndCheckFields():
            # Усі поля заповнені та пройшли перевірки

            # Створюємо SQL-запит для додавання даних
            match self.tableName:
                case "books":
                    insert_query = "INSERT INTO books (Title, Author, Genre, Year, Publisher, Price, InStock) VALUES (%s, %s, %s, %s, %s, %s, %s)"
                    values = (self.Field1.text(), self.Field2.text(), self.Field3.text(), int(self.Field4.text()), self.Field5.text(), float(self.Field6.text()), int(self.Field7.text()))
                case "customers":
                    insert_query = "INSERT INTO customers (FirstName, LastName, Email, Phone, Address) VALUES (%s, %s, %s, %s, %s)"
                    values = (self.Field1.text(), self.Field2.text(), self.Field3.text(), self.Field4.text(), self.Field5.text())
                case "sales":
                    insert_query = "INSERT INTO sales (BookID, CustomerID, QuantitySold, TotalPrice, SaleDate, PaymentMethod) VALUES (%s, %s, %s, %s, %s, %s)"
                    values = (int(self.Field1.text()), int(self.Field2.text()), int(self.Field3.text()), float(self.Field4.text()), self.Field5.text(), self.Field6.text())

            cursor = self.connection.cursor()
            
            try:
                cursor.execute(insert_query, values)
                self.connection.commit()
                cursor.close()
                # Дані успішно додано до бази даних
                self.result = 1
                self.dialog.accept()

            except mysql.connector.Error as err:
                center_x = self.Form.pos().x() + self.Form.width() / 2
                center_y = self.Form.pos().y() + self.Form.height() / 2
                self.dialogError = Ui_Error()
                title = "Помилка при додаванні даних"
                self.dialogError.openDialog(center_x, center_y, title, str(err))

    # Змінюємо існуючий запис
    def EditRow(self, id_value):
        if self.validateAndCheckFields():
            # Усі поля заповнені та пройшли перевірки

            # Створюємо SQL-запит для оновлення даних
            match self.tableName:
                case "books":
                    update_query = "UPDATE books SET Title = %s, Author = %s, Genre = %s, Year = %s, Publisher = %s, Price = %s, InStock = %s WHERE id = %s"
                    values = (self.Field1.text(), self.Field2.text(), self.Field3.text(), int(self.Field4.text()), self.Field5.text(), float(self.Field6.text()), int(self.Field7.text()), id_value)
                case "customers":
                    update_query = "UPDATE customers SET FirstName = %s, LastName = %s, Email = %s, Phone = %s, Address = %s WHERE id = %s"
                    values = (self.Field1.text(), self.Field2.text(), self.Field3.text(), self.Field4.text(), self.Field5.text(), id_value)
                case "sales":
                    update_query = "UPDATE sales SET BookID = %s, CustomerID = %s, QuantitySold = %s, TotalPrice = %s, SaleDate = %s, PaymentMethod = %s WHERE id = %s"
                    values = (int(self.Field1.text()), int(self.Field2.text()), int(self.Field3.text()), float(self.Field4.text()), self.Field5.text(), self.Field6.text(), id_value)

            cursor = self.connection.cursor()
            
            try:
                cursor.execute(update_query, values)
                self.connection.commit()
                cursor.close()
                # Дані успішно змінено
                self.result = 1
                self.dialog.accept()

            except mysql.connector.Error as err:
                center_x = self.Form.pos().x() + self.Form.width() / 2
                center_y = self.Form.pos().y() + self.Form.height() / 2
                self.dialogError = Ui_Error()
                title = "Помилка під час зміни даних"
                self.dialogError.openDialog(center_x, center_y, title, str(err))

    # Перевіряємо перед відправкою чи всі поля заповнені правильно
    def validateAndCheckFields(self):
        # Перевірка числових значеннь у полі
        def validateNumericField(field, min_value, max_value):
            try:
                value = float(field.text())
                if min_value <= value <= max_value:
                    field.setStyleSheet(self.defaultStyleField)
                    return True
                else: # Некоректне значення в полі
                    pass
            except ValueError: # Невірні дані в полі
                pass

            field.setStyleSheet(self.errorStyleField)
            return False
        # Перевірка значеннь у полі Id
        def validateIdField(field, table):
            try:
                value = int(field.text())
                
                cursor = self.connection.cursor()
                cursor.execute(f"SELECT ID FROM {table}")
                
                id_list = [int(row[0]) for row in cursor.fetchall()]
                if value in id_list:
                    field.setStyleSheet(self.defaultStyleField)
                    return True
                else:
                    field.setStyleSheet(self.errorStyleField)
                    return False
            except ValueError:
                pass

            field.setStyleSheet(self.errorStyleField)
            return False

        # Перевірка запису дати у полі
        def validateDateField(field):
            try:
                datetime.strptime(field.text(), '%Y-%m-%d')
                field.setStyleSheet(self.defaultStyleField)
                return True
            except ValueError: # Невірні дані в полі
                pass
            field.setStyleSheet(self.errorStyleField)
            return False

        all_fields_filled = True  # Спочатку вважаємо, що всі поля заповнені
        all_fields_True = False # Спочатку вважаємо, що всі поля не пройшли перевірку
        
        # Перевіряємо заповнені поля чи ні
        for field in self.fields_to_check:
            if field.text() == "":
                # Зміна кольорів для відображення що введені не вірні дані
                field.setStyleSheet(self.errorStyleField)
                all_fields_filled = False
            else:
                field.setStyleSheet(self.defaultStyleField)  # Скидання стилю, якщо поле заповнене

        if self.tableName == "books":
            valid_year = validateNumericField(self.Field4, 1000, 9999)
            valid_price = validateNumericField(self.Field6, 0, 999999999.99)
            valid_quantity = validateNumericField(self.Field7, 0, float('inf'))        

            if all_fields_filled and valid_year and valid_price and valid_quantity:
                all_fields_True = True

        elif self.tableName == "customers" and all_fields_filled:    
            all_fields_True = True

        elif self.tableName == "sales":

            valid_idBook = validateIdField(self.Field1, "books")
            valid_idCustomers = validateIdField(self.Field2, "customers")
            valid_quantitySold = validateNumericField(self.Field3, 0, float('inf'))
            valid_totalPrice = validateNumericField(self.Field4, 0, 999999999.99)
            valid_date = validateDateField(self.Field5)
            
            if all_fields_filled and valid_idBook and valid_idCustomers and valid_quantitySold and valid_totalPrice and valid_date:
                all_fields_True = True

        return all_fields_filled and all_fields_True
    