import sys
from PyQt5 import QtWidgets
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QApplication, QDialog, QMessageBox


class user_login(QDialog):
    def __init__(self):
        super(user_login, self).__init__()
        loadUi("login.ui", self)
        self.submit_button.clicked.connect(self.user_function)
        self.tableWidget.setColumnWidth(0, 200)
        self.tableWidget.setColumnWidth(1, 200)
        self.tableWidget.setColumnWidth(2, 180)
        self.tableWidget.setColumnWidth(3, 220)
        self.tableWidget.setColumnWidth(4, 190)
        self.tableWidget.setRowCount(0)
        for i in range(1, 9):
            self.tableWidget.setItem(
                i - 1, 0, QtWidgets.QTableWidgetItem(str(i)))

    def user_function(self):
        self.tableWidget.clearContents()
        self.tableWidget.setRowCount(0)
        io = self.io.text().split()
        io_per = self.io_per.text().split()
        burst = self.burst_time.text().split()

        if len(io_per) != len(io) or len(io_per) != len(burst) or len(io) != len(burst):
            QtWidgets.QMessageBox.critical(
                self, "Error", "Number of Process ID, I/O Time, and Burst Time must be the same.")
            return

        if not io_per or not io or not burst:
            QtWidgets.QMessageBox.critical(
                self, "Error", "Please fill in all fields.")
            return
        
        if len(burst) > 8:
            QtWidgets.QMessageBox.critical(
                self, "Error", "Number of processes should not exceed 8.")
            return
        for i, ip in zip(io, io_per):
            if (i.lower() not in ['y', 'n'] and i.lower() not in ['Y', 'N']):
                QtWidgets.QMessageBox.critical(
                    self, "Error", "I/O should be 'Y' or 'N'")
                return
            if (i.lower() == 'N' or i.lower() == 'n') and ip != '0':
                QtWidgets.QMessageBox.critical(
                    self, "Error", "I/O is 'NO', so I/O Percentage must be 0.")
                return

        for i, ip, b in zip(io, io_per, burst):
            rowPosition = self.tableWidget.rowCount()
            self.tableWidget.insertRow(rowPosition)
            p = f'p{rowPosition}'
            self.tableWidget.setItem(
                rowPosition, 0, QtWidgets.QTableWidgetItem(p))
            self.tableWidget.setItem(
                rowPosition, 1, QtWidgets.QTableWidgetItem('1'))
            self.tableWidget.setItem(
                rowPosition, 2, QtWidgets.QTableWidgetItem(i))
            self.tableWidget.setItem(
                rowPosition, 3, QtWidgets.QTableWidgetItem(ip))
            self.tableWidget.setItem(
                rowPosition, 4, QtWidgets.QTableWidgetItem(b))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainwindow = user_login()
    widget = QtWidgets.QStackedWidget()
    widget.addWidget(mainwindow)
    widget.show()
    sys.exit(app.exec_())
