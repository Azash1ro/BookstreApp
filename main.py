import sys
import mysql.connector
from PyQt5 import QtWidgets, QtGui
from Ui_Home import Ui_Home
from Ui_Info import Ui_Info
from Ui_Table import Ui_Table

class MyForm(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Home()
        self.ui.setupUi(self)
        
        shortcuts = {
            "L": self.ui.buttonLibrary.click,
            "C": self.ui.buttonCustomers.click,
            "S": self.ui.buttonSales.click,
            "I": self.ui.buttonInfo.click,
        }

        for key, click_handler in shortcuts.items():
            shortcut = QtWidgets.QShortcut(QtGui.QKeySequence(key), self)
            shortcut.activated.connect(click_handler)

        self.ui.buttonInfo.clicked.connect(self.open_Ui_Info)

        self.ui.buttonLibrary.clicked.connect(lambda: self.open_Ui_Table("books"))
        self.ui.buttonCustomers.clicked.connect(lambda: self.open_Ui_Table("customers"))
        self.ui.buttonSales.clicked.connect(lambda: self.open_Ui_Table("sales"))
    
    # Відкриваємо інформаційне вікно
    def open_Ui_Info(self):
        center_x = self.x() + self.width() / 2
        center_y = self.y() + self.height() / 2
        self.info_form = Ui_Info()
        self.info_form.open(center_x, center_y)

    # Відкриваємо вікно з таблицею
    def open_Ui_Table(self, tableName):
        center_x = self.x() + self.width() / 2
        center_y = self.y() + self.height() / 2
        self.table_form = Ui_Table(connection, tableName)
        self.table_form.open(self, center_x, center_y)  # Передаємо посилання на стартове вікно
        
        # Повернення назад до першого вікна
        self.table_form.buttonBack.clicked.connect(self.table_form.returnToFirstWindow)
        # Знайти запис
        self.table_form.buttonSearch.clicked.connect(self.table_form.searchInTable)
        # Додати запис
        self.table_form.buttonAdd.clicked.connect(lambda: self.table_form.rowEdit("Add"))
        # Змінити запис
        self.table_form.buttonUpdate.clicked.connect(lambda: self.table_form.rowEdit("Update"))
        # Видалити запис
        self.table_form.buttonDelete.clicked.connect(self.table_form.deleteSelectedRow)

        self.close()

def connectAndCheckDatabase(login: str, password: str):
    try:
        # Спробуємо встановити з'єднання з існуючою базою даних
        connection = mysql.connector.connect(
            host = "localhost",
            user = login,
            password = password,
            database = "bookstore"
        )
        print("Підключено до існуючої бази даних")

    except mysql.connector.Error as err:
        if err.errno == mysql.connector.errorcode.ER_BAD_DB_ERROR:
            # База даних не існує
            try:
                connection = mysql.connector.connect(
                    host = "localhost",
                    user = "admin",
                    password = "admin"
                )
                cursor = connection.cursor()
                cursor.execute("CREATE DATABASE bookstore")
                print("Створено нову базу даних 'bookstore'")
                connection.database = "bookstore"
                
                # Перевірка наявності та створення таблиць
                cursor.execute("""
                    CREATE TABLE IF NOT EXISTS books (
                        ID INT NOT NULL AUTO_INCREMENT,
                        Title VARCHAR(150) NOT NULL,
                        Author VARCHAR(150) NOT NULL,
                        Genre VARCHAR(150) NOT NULL,
                        Year INT DEFAULT NULL,
                        Publisher VARCHAR(150) DEFAULT NULL,
                        Price DECIMAL(10,2) NOT NULL,
                        InStock INT NOT NULL,
                        PRIMARY KEY (ID)
                    ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;""")
                cursor.execute("""
                    CREATE TABLE IF NOT EXISTS customers (
                        ID INT NOT NULL AUTO_INCREMENT,
                        FirstName VARCHAR(255) NOT NULL,
                        LastName VARCHAR(255) NOT NULL,
                        Email VARCHAR(255) NOT NULL,
                        Phone VARCHAR(45) DEFAULT NULL,
                        Address VARCHAR(500) DEFAULT NULL,
                        PRIMARY KEY (ID)
                    ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;""")
                cursor.execute("""
                    CREATE TABLE IF NOT EXISTS sales (
                        ID INT NOT NULL AUTO_INCREMENT,
                        BookID INT NOT NULL,
                        CustomerID INT NOT NULL,
                        QuantitySold INT NOT NULL,
                        TotalPrice DECIMAL(10,2) NOT NULL,
                        SaleDate DATE NOT NULL,
                        PaymentMethod VARCHAR(100) NOT NULL,
                        PRIMARY KEY (ID),
                        KEY FK_Book_Sale (BookID),
                        KEY FK_Customer_Sale (CustomerID),
                        CONSTRAINT FK_Book_Sale FOREIGN KEY (BookID) REFERENCES books (ID),
                        CONSTRAINT FK_Customer_Sale FOREIGN KEY (CustomerID) REFERENCES customers (ID)
                    ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;""")

                print("Перевірка та створення таблиць завершено")

            except mysql.connector.Error as err:
                exit(1)

        else:
            exit(1)

    return connection

# Пібключаємось до бази даних
connection = connectAndCheckDatabase("admin", "admin")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Form = MyForm()
    Form.show()
    
    try:
        sys.exit(app.exec_())
    finally:
        # Закриваємо підключення до бази даних
        if connection.is_connected():
            connection.close()
