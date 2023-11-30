from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
from Ui_Edit import Ui_Edit
from Ui_Delete import Ui_Delete
from Ui_Error import Ui_Error

import mysql.connector


class Ui_Table(object):
    def __init__(self, connection, tableName):
        self.connection = connection
        self.tableName = tableName

    def setupUi(self, Form):
        Form.setWindowIcon(QIcon('img/icon.png'))
        Form.setObjectName("Form")
        Form.resize(1145, 650)
        Form.setMinimumSize(QtCore.QSize(1145, 650))
        Form.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(143, 136, 117, 255), stop:0.5 rgba(124, 95, 78, 255), stop:1 rgba(101, 54, 56, 255));")
        self.horizontalLayoutForm = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayoutForm.setContentsMargins(25, 25, 25, 25)
        self.horizontalLayoutForm.setSpacing(40)
        self.horizontalLayoutForm.setObjectName("horizontalLayoutForm")
        self.tableWidget = QtWidgets.QTableWidget(Form)
        self.tableWidget.setMinimumSize(QtCore.QSize(850, 600))
        self.tableWidget.setStyleSheet("QTableWidget {border-radius: 10px;background: rgba(0, 0, 0, 0.19);border: none;font-family: \"Calibri\";font-size: 16px;font-weight: 400;color: white;}QTableWidget QHeaderView {background: transparent;font-family: \"Calibri\";font-size: 16px;font-weight: 600;color: white;}QHeaderView::section { height: 40px;background: rgba(0, 0, 0, 0.37);}QTableWidget::item {height: 80px;background: transparent;border-left: 1px solid rgba(0, 0, 0, 0.0);border-top: 1px solid rgba(0, 0, 0, 0.19);}")
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget.setTabKeyNavigation(True)
        self.tableWidget.setShowGrid(False)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.tableWidget.horizontalHeader().setVisible(True)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setHighlightSections(True)
        self.tableWidget.horizontalHeader().setSortIndicatorShown(True)

        # Міняємо True на False - відповідає за розтягування кінцевого рядка
        self.tableWidget.horizontalHeader().setStretchLastSection(False)
        # Відключаємо індикатор строк
        self.tableWidget.verticalHeader().setVisible(False)
        
        self.tableWidget.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget.verticalHeader().setSortIndicatorShown(True)
        self.tableWidget.verticalHeader().setStretchLastSection(False)
        self.horizontalLayoutForm.addWidget(self.tableWidget)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSpacing(20)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(178, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.buttonBack = QtWidgets.QPushButton(Form)
        self.buttonBack.setMinimumSize(QtCore.QSize(27, 22))
        self.buttonBack.setMaximumSize(QtCore.QSize(27, 22))
        self.buttonBack.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.buttonBack.setStyleSheet("QPushButton {background: transparent;background-image: url(:/button/img/back.svg);background-repeat: no-repeat;background-position: center;background-size: 27px 22px;padding: 0px;margin: 0px;border: none;}")
        self.buttonBack.setText("")
        self.buttonBack.setObjectName("buttonBack")
        self.horizontalLayout.addWidget(self.buttonBack)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.labelTitle = QtWidgets.QLabel(Form)
        self.labelTitle.setMinimumSize(QtCore.QSize(190, 39))
        self.labelTitle.setMaximumSize(QtCore.QSize(190, 39))
        self.labelTitle.setStyleSheet(f"background: transparent;background-image: url(:/title/img/title/{self.tableName}-title.svg);background-repeat: no-repeat;")
        self.labelTitle.setText("")
        self.labelTitle.setObjectName("labelTitle")
        self.verticalLayout.addWidget(self.labelTitle)
        self.verticalLayoutSearchField = QtWidgets.QVBoxLayout()
        self.verticalLayoutSearchField.setContentsMargins(-1, 10, -1, -1)
        self.verticalLayoutSearchField.setSpacing(16)
        self.verticalLayoutSearchField.setObjectName("verticalLayoutSearchField")
        self.SearchField_1 = QtWidgets.QLineEdit(Form)
        self.SearchField_1.setMinimumSize(QtCore.QSize(190, 40))
        self.SearchField_1.setMaximumSize(QtCore.QSize(190, 40))
        self.SearchField_1.setStyleSheet("QLineEdit {color: #F4E0AE;text-align: center;font-family: \"Calibri\";font-size: 16px;font-style: normal;font-weight: 400;padding:  0 12px 0 12px;border-radius: 5px;border: 1px solid #FFCD50;background: transparent;}QLineEdit:hover {border: 1.5px solid #FFCD50;}QLineEdit:focus {border: 1.5px solid #FFCD50;}\n")
        self.SearchField_1.setPlaceholderText("")
        self.SearchField_1.setObjectName("SearchField_1")
        self.verticalLayoutSearchField.addWidget(self.SearchField_1)
        self.SearchField_2 = QtWidgets.QLineEdit(Form)
        self.SearchField_2.setMinimumSize(QtCore.QSize(190, 40))
        self.SearchField_2.setMaximumSize(QtCore.QSize(190, 40))
        self.SearchField_2.setStyleSheet("QLineEdit {color: #F4E0AE;text-align: center;font-family: \"Calibri\";font-size: 16px;font-style: normal;font-weight: 400;padding:  0 12px 0 12px;border-radius: 5px;border: 1px solid #FFCD50;background: transparent;}QLineEdit:hover {border: 1.5px solid #FFCD50;}QLineEdit:focus {border: 1.5px solid #FFCD50;}\n")
        self.SearchField_2.setPlaceholderText("")
        self.SearchField_2.setObjectName("SearchField_2")
        self.verticalLayoutSearchField.addWidget(self.SearchField_2)
        self.SearchField_3 = QtWidgets.QLineEdit(Form)
        self.SearchField_3.setMinimumSize(QtCore.QSize(190, 40))
        self.SearchField_3.setMaximumSize(QtCore.QSize(190, 40))
        self.SearchField_3.setStyleSheet("QLineEdit {color: #F4E0AE;text-align: center;font-family: \"Calibri\";font-size: 16px;font-style: normal;font-weight: 400;padding:  0 12px 0 12px;border-radius: 5px;border: 1px solid #FFCD50;background: transparent;}QLineEdit:hover {border: 1.5px solid #FFCD50;}QLineEdit:focus {border: 1.5px solid #FFCD50;}\n")
        self.SearchField_3.setPlaceholderText("")
        self.SearchField_3.setObjectName("SearchField_3")
        self.verticalLayoutSearchField.addWidget(self.SearchField_3)
        self.buttonSearch = QtWidgets.QPushButton(Form)
        self.buttonSearch.setMinimumSize(QtCore.QSize(190, 40))
        self.buttonSearch.setMaximumSize(QtCore.QSize(190, 40))
        self.buttonSearch.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.buttonSearch.setStyleSheet("QPushButton {border-radius: 5px;border: 1px solid #FFCD50;background-color: transparent;color: #FFCD50;text-align: center;font-size: 16px;font-style: normal;font-weight: 800;line-height: 100%;font-family: \"Calibri\";}QPushButton:hover {background-color: #FFCD50;color: #693C3B;}QPushButton:pressed {background-color: #FFD56C;}\n")
        self.buttonSearch.setObjectName("buttonSearch")
        self.verticalLayoutSearchField.addWidget(self.buttonSearch)
        self.verticalLayout.addLayout(self.verticalLayoutSearchField)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.labelWarning = QtWidgets.QLabel(Form)
        self.labelWarning.setMinimumSize(QtCore.QSize(190, 20))
        self.labelWarning.setMaximumSize(QtCore.QSize(190, 20))
        self.labelWarning.setStyleSheet("background-color: transparent;color: #FFCD50;font-size: 16px;font-style: normal;font-weight: 400;line-height: 100%;font-family: \"Calibri\";")
        self.labelWarning.setAlignment(QtCore.Qt.AlignCenter)
        self.labelWarning.setObjectName("labelWarning")
        self.verticalLayout.addWidget(self.labelWarning)
        self.labelWarning.hide()
        self.verticalLayoutButton = QtWidgets.QVBoxLayout()
        self.verticalLayoutButton.setSpacing(16)
        self.verticalLayoutButton.setObjectName("verticalLayoutButton")
        self.buttonUpdate = QtWidgets.QPushButton(Form)
        self.buttonUpdate.setMinimumSize(QtCore.QSize(190, 40))
        self.buttonUpdate.setMaximumSize(QtCore.QSize(190, 40))
        self.buttonUpdate.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.buttonUpdate.setStyleSheet("QPushButton {border-radius: 5px;background: #FFCD50;color: #693D3B;text-align: center;font-family: \"Calibri\";font-size: 16px;font-style: normal;font-weight: 800;}QPushButton:hover {background-color: #FFD56C;}QPushButton:pressed {background-color: #FFCD50;}")
        self.buttonUpdate.setObjectName("buttonUpdate")
        self.verticalLayoutButton.addWidget(self.buttonUpdate)
        self.buttonAdd = QtWidgets.QPushButton(Form)
        self.buttonAdd.setMinimumSize(QtCore.QSize(190, 40))
        self.buttonAdd.setMaximumSize(QtCore.QSize(190, 40))
        self.buttonAdd.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.buttonAdd.setStyleSheet("QPushButton {border-radius: 5px;background: #FFCD50;color: #693D3B;text-align: center;font-family: \"Calibri\";font-size: 16px;font-style: normal;font-weight: 800;}QPushButton:hover {background-color: #FFD56C;}QPushButton:pressed {background-color: #FFCD50;}")
        self.buttonAdd.setObjectName("buttonAdd")
        self.verticalLayoutButton.addWidget(self.buttonAdd)
        self.buttonDelete = QtWidgets.QPushButton(Form)
        self.buttonDelete.setMinimumSize(QtCore.QSize(190, 40))
        self.buttonDelete.setMaximumSize(QtCore.QSize(190, 40))
        self.buttonDelete.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.buttonDelete.setStyleSheet("QPushButton {border-radius: 5px;background: #FFCD50;color: #693D3B;text-align: center;font-family: \"Calibri\";font-size: 16px;font-style: normal;font-weight: 800;}QPushButton:hover {background-color: #FFD56C;}QPushButton:pressed {background-color: #FFCD50;}")
        self.buttonDelete.setObjectName("buttonDelete")
        self.verticalLayoutButton.addWidget(self.buttonDelete)
        self.verticalLayout.addLayout(self.verticalLayoutButton)
        self.horizontalLayoutForm.addLayout(self.verticalLayout)

        # Додаємо гарячу клавішу Escape для метода "returnToFirstWindow"
        shortcut = QtWidgets.QShortcut(QtGui.QKeySequence("Escape"), self.Form)
        shortcut.activated.connect(self.returnToFirstWindow)
    
        self.selected_row = None
        self.timer = QtCore.QTimer(Form)
        self.timer.timeout.connect(self.toggleLabelWarning)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        self.setupTableColumns()
        self.showDataInTable()

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate

        match self.tableName:
            case "books":
                self.SearchField_1.setPlaceholderText(_translate("Form", "Пошук за назвою"))
                self.SearchField_2.setPlaceholderText(_translate("Form", "Пошук за автором"))
                self.SearchField_3.setPlaceholderText(_translate("Form", "За жанром"))
            case "customers":
                self.SearchField_1.setPlaceholderText(_translate("Form", "Пошук за ім'ям"))
                self.SearchField_2.setPlaceholderText(_translate("Form", "Пошук за прізвищем"))
                self.SearchField_3.setPlaceholderText(_translate("Form", "Пошук за email"))
            case "sales":
                self.SearchField_1.setPlaceholderText(_translate("Form", "Пошук за id"))
                self.SearchField_2.setPlaceholderText(_translate("Form", "Початкова дата"))
                self.SearchField_3.setPlaceholderText(_translate("Form", "Кінцева дата"))

        Form.setWindowTitle(_translate("Form", "Bookstore"))
        self.tableWidget.setSortingEnabled(True)
        self.buttonSearch.setText(_translate("Form", "Пошук"))
        self.labelWarning.setText(_translate("Form", "Немає виділеного рядка"))
        self.buttonUpdate.setText(_translate("Form", "Змінити запис"))
        self.buttonAdd.setText(_translate("Form", "Додати запис"))
        self.buttonDelete.setText(_translate("Form", "Видалити запис"))

    # Видалення вибраного рядка
    def deleteSelectedRow(self):
        selected_items = self.tableWidget.selectedItems()

        if selected_items:
            selected_row = selected_items[0].row()
            item = self.tableWidget.item(selected_row, 0)  # 0 - стовпець "ID"
            
            if item:
                id_value = item.text()
                center_x = self.Form.pos().x() + self.Form.width() / 2
                center_y = self.Form.pos().y() + self.Form.height() / 2
                self.dialog_delete = Ui_Delete(id_value)
                result = self.dialog_delete.openDialog(center_x, center_y)
                
                if result:
                    cursor = self.connection.cursor()
                    query = f"DELETE FROM {self.tableName} WHERE id = {id_value}"
                    try:
                        cursor.execute(query)
                        self.connection.commit()
                        # Рядок успішно видален
                        self.showDataInTable()
                    except mysql.connector.Error as err:
                        center_x = self.Form.pos().x() + self.Form.width() / 2
                        center_y = self.Form.pos().y() + self.Form.height() / 2
                        self.dialogError = Ui_Error()

                        match self.tableName:
                            case "books":
                                title = "Помилка при видаленні книги"
                            case "customers":
                                title = "Помилка при видаленні користувача"
                            case "sales":
                                title = "Помилка при видаленні продажу"
                                
                        self.dialogError.openDialog(center_x, center_y, title, str(err))

                    finally:
                        cursor.close()
        else:
            self.toggleLabelWarning()

    # Пошук в таблиці
    def searchInTable(self):
        SearchField_1 = self.SearchField_1.text()
        SearchField_2 = self.SearchField_2.text()
        SearchField_3 = self.SearchField_3.text()

        search_params = (f"%{SearchField_1}%", f"%{SearchField_2}%", f"%{SearchField_3}%")

        match self.tableName:
            case "books":
                search_query = (f"SELECT * FROM {self.tableName} WHERE "
                "Title LIKE %s AND Author LIKE %s AND Genre LIKE %s")

            case "customers":
                search_query = (f"SELECT * FROM {self.tableName} WHERE "
                "FirstName LIKE %s AND LastName LIKE %s AND Email LIKE %s")

            case "sales":
                if SearchField_1 == "":
                    # Якщо не вказано значення в першому полі, враховуємо тільки діапазон дат
                    if SearchField_2 == "" and SearchField_3 == "":
                        search_query = f"SELECT * FROM sales"
                    elif SearchField_2 == "":
                        search_query = f"SELECT * FROM sales WHERE SaleDate BETWEEN '0000-01-01' AND '%{SearchField_3}%'"
                    elif SearchField_3 == "":
                        search_query = f"SELECT * FROM sales WHERE SaleDate BETWEEN '%{SearchField_2}%' AND '9999-12-30'"
                    else:
                        search_query = f"SELECT * FROM sales WHERE SaleDate BETWEEN '%{SearchField_2}%' AND '%{SearchField_3}%'"
                else:
                    # Якщо вказано значення в першому полі, враховуємо його та діапазон дат
                    if SearchField_2 == "" and SearchField_3 == "":
                        search_query = f"SELECT * FROM sales WHERE ID LIKE '%{SearchField_1}%'"
                    elif SearchField_2 == "":
                        search_query = f"SELECT * FROM sales WHERE ID LIKE '%{SearchField_1}%' AND SaleDate BETWEEN '0000-01-01' AND '%{SearchField_3}%'"
                    elif SearchField_3 == "":
                        search_query = f"SELECT * FROM sales WHERE ID LIKE '%{SearchField_1}%' AND SaleDate BETWEEN '%{SearchField_2}%' AND '9999-12-30'"
                    else:
                        search_query = f"SELECT * FROM sales WHERE ID LIKE '%{SearchField_1}%' AND SaleDate BETWEEN '%{SearchField_2}%' AND '%{SearchField_3}%'"

        cursor = self.connection.cursor()

        try:
            if self.tableName == "sales":
                cursor.execute(search_query)
            else:
                cursor.execute(search_query, search_params)
            
            search_result = cursor.fetchall()

            self.tableWidget.setRowCount(len(search_result))

            # Заповнюємо QTableWidget отриманими даними
            for row_number, row_data in enumerate(search_result):
                for column_number, data in enumerate(row_data):

                    item = QtWidgets.QTableWidgetItem(str(data))

                    item.setTextAlignment(QtCore.Qt.AlignCenter)

                    self.tableWidget.setItem(row_number, column_number, item)

        except mysql.connector.Error as err:
            center_x = self.Form.pos().x() + self.Form.width() / 2
            center_y = self.Form.pos().y() + self.Form.height() / 2
            self.dialogError = Ui_Error()
            title = "Помилка під час виконання запиту"
            self.dialogError.openDialog(center_x, center_y, title, str(err))
        cursor.close()

    # Змінюємо або додаємо рядок
    def rowEdit(self, mode):
        center_x = self.Form.pos().x() + self.Form.width() / 2
        center_y = self.Form.pos().y() + self.Form.height() / 2
        self.dialogEdit = Ui_Edit(self.connection, self.tableName, mode)
        result = 0
        match mode:
            case "Add":
                result = self.dialogEdit.openDialog(center_x, center_y, 0)

            case "Update":
                selected_items = self.tableWidget.selectedItems()
                if selected_items:
                    selected_row = selected_items[0].row()
                    item = self.tableWidget.item(selected_row, 0)  # 0 - стовпець "ID"
                    
                    if item:
                        id_value = item.text()
                        result = self.dialogEdit.openDialog(center_x, center_y, id_value)
                else:
                    self.toggleLabelWarning()
                    
        if result:
            # Оновлення данних у таблиці
            self.showDataInTable()

    # Налаштовує стовпці залежно від таблиці
    def setupTableColumns(self):
        match self.tableName:
            case "books":
                # Налаштовуємо стовпці для таблиці "Книги"
                self.tableWidget.setColumnCount(8)
                self.tableWidget.setHorizontalHeaderLabels(['ID', 'Назва книги', 'Автор', 'Жанр', 'Рік', 'Видавництво', 'Ціна', 'Кількість'])
                self.tableWidget.setColumnWidth(0, 40)  # ID
                self.tableWidget.horizontalHeader().setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
                self.tableWidget.horizontalHeader().setSectionResizeMode(2, QtWidgets.QHeaderView.Stretch)
                self.tableWidget.horizontalHeader().setSectionResizeMode(3, QtWidgets.QHeaderView.Stretch)
                self.tableWidget.horizontalHeader().setSectionResizeMode(4, QtWidgets.QHeaderView.Stretch)
                self.tableWidget.horizontalHeader().setSectionResizeMode(5, QtWidgets.QHeaderView.Stretch)
                self.tableWidget.horizontalHeader().setSectionResizeMode(6, QtWidgets.QHeaderView.Stretch)
                self.tableWidget.horizontalHeader().setSectionResizeMode(7, QtWidgets.QHeaderView.Stretch)

            case "customers":
                # Налаштовуємо стовпці для таблиці "Клієнти"
                self.tableWidget.setColumnCount(6)
                self.tableWidget.setHorizontalHeaderLabels(['ID', "Ім'я", 'Прізвище', 'Email', 'Телефон', 'Адреса'])
                self.tableWidget.setColumnWidth(0, 40)  # ID
                self.tableWidget.horizontalHeader().setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
                self.tableWidget.horizontalHeader().setSectionResizeMode(2, QtWidgets.QHeaderView.Stretch)
                self.tableWidget.horizontalHeader().setSectionResizeMode(3, QtWidgets.QHeaderView.Stretch)
                self.tableWidget.horizontalHeader().setSectionResizeMode(4, QtWidgets.QHeaderView.Stretch)
                self.tableWidget.horizontalHeader().setSectionResizeMode(5, QtWidgets.QHeaderView.Stretch)

            case "sales":
                # Налаштовуємо стовпці для таблиці "Продажі"
                self.tableWidget.setColumnCount(7)
                self.tableWidget.setHorizontalHeaderLabels(['ID', "ID Книги", 'ID Клієнта', 'Кількість', 'Загальна вартість', 'Дата продажу', 'Спосіб оплати'])
                self.tableWidget.setColumnWidth(0, 40)  # ID
                self.tableWidget.horizontalHeader().setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
                self.tableWidget.horizontalHeader().setSectionResizeMode(2, QtWidgets.QHeaderView.Stretch)
                self.tableWidget.horizontalHeader().setSectionResizeMode(3, QtWidgets.QHeaderView.Stretch)
                self.tableWidget.horizontalHeader().setSectionResizeMode(4, QtWidgets.QHeaderView.Stretch)
                self.tableWidget.horizontalHeader().setSectionResizeMode(5, QtWidgets.QHeaderView.Stretch)
                self.tableWidget.horizontalHeader().setSectionResizeMode(6, QtWidgets.QHeaderView.Stretch)

    # Відображення данних у таблиці
    def showDataInTable(self):
        cursor = self.connection.cursor()
        query = f"SELECT * FROM {self.tableName}"
        
        try:
            cursor.execute(query)
            result = cursor.fetchall()

            self.tableWidget.setRowCount(len(result))
            
            # Заповнюємо QTableWidget отриманими даними
            for row_number, row_data in enumerate(result):
                for column_number, data in enumerate(row_data):
                    
                    item = QtWidgets.QTableWidgetItem(str(data))

                    item.setTextAlignment(QtCore.Qt.AlignCenter)

                    self.tableWidget.setItem(row_number, column_number, item)

        except mysql.connector.Error as err:
            # Обробляємо помилки бази даних та виводимо їх у консоль
            center_x = self.Form.pos().x() + self.Form.width() / 2
            center_y = self.Form.pos().y() + self.Form.height() / 2
            self.dialogError = Ui_Error()
            title = "Помилка"
            self.dialogError.openDialog(center_x, center_y, title, str(err))
        finally:
            cursor.close()

    # Показує попередження 
    def toggleLabelWarning(self):
        if self.labelWarning.isHidden():
            self.labelWarning.show()
            self.timer.start(5000)
        else:
            self.labelWarning.hide()
            self.timer.stop()

    # Відкиває вікно
    def open(self, main_form, center_x, center_y):
        self.main_form = main_form
        self.Form = QtWidgets.QWidget()
        center_x = round(center_x)
        center_y = round(center_y)
        self.Form.move(center_x - 573, center_y - 325)
        self.setupUi(self.Form)
        self.Form.show()

    # Повертає до першого вікна
    def returnToFirstWindow(self):
        self.Form.close()  # Закрываємо поточне вікно
        self.main_form.show()  # Показуємо перше вікно

import resources