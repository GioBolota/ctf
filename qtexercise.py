import random
from PyQt5 import QtCore, QtGui, QtWidgets
from pymongo import MongoClient
from bson.objectid import ObjectId

client = MongoClient("mongodb://localhost:27017/")
db = client['student_database']
collection = db['students']

LNames = ['Abashidze', 'Gigauri', 'Archvadze', 'Akhalaya', 'Berishvili', 'Dalakishvili']
FNames = ['Anna', 'Nino', 'Mariam', 'Lasha', 'Nika', 'David']
Subjects = ['Algorithms I', 'Calculus II', 'Intro to Physics', 'Data Structures']
Points = [str(i) for i in range(101)]


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(780, 512)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.ID_lable = QtWidgets.QLabel(self.centralwidget)
        self.ID_lable.setGeometry(QtCore.QRect(30, 30, 101, 41))
        self.ID_lable.setObjectName("ID_lable")
        self.ID = QtWidgets.QLineEdit(self.centralwidget)
        self.ID.setGeometry(QtCore.QRect(140, 40, 113, 22))
        self.ID.setObjectName("ID")

        self.lastName_lable = QtWidgets.QLabel(self.centralwidget)
        self.lastName_lable.setGeometry(QtCore.QRect(30, 70, 101, 41))
        self.lastName_lable.setObjectName("lastName_lable")
        self.lastName = QtWidgets.QLineEdit(self.centralwidget)
        self.lastName.setGeometry(QtCore.QRect(140, 80, 113, 22))
        self.lastName.setObjectName("lastName")

        self.name_lable = QtWidgets.QLabel(self.centralwidget)
        self.name_lable.setGeometry(QtCore.QRect(30, 110, 101, 41))
        self.name_lable.setObjectName("name_lable")
        self.name_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.name_2.setGeometry(QtCore.QRect(140, 120, 113, 22))
        self.name_2.setObjectName("name_2")

        self.subject_lable = QtWidgets.QLabel(self.centralwidget)
        self.subject_lable.setGeometry(QtCore.QRect(30, 150, 101, 41))
        self.subject_lable.setObjectName("subject_lable")
        self.subject = QtWidgets.QLineEdit(self.centralwidget)
        self.subject.setGeometry(QtCore.QRect(140, 160, 113, 22))
        self.subject.setObjectName("subject")

        self.grade_label = QtWidgets.QLabel(self.centralwidget)
        self.grade_label.setGeometry(QtCore.QRect(30, 190, 101, 41))
        self.grade_label.setObjectName("grade_label")
        self.grade = QtWidgets.QLineEdit(self.centralwidget)
        self.grade.setGeometry(QtCore.QRect(140, 200, 113, 22))
        self.grade.setObjectName("grade")

        self.addAllRecords_button = QtWidgets.QPushButton(self.centralwidget)
        self.addAllRecords_button.setGeometry(QtCore.QRect(300, 40, 200, 30))
        self.addAllRecords_button.setObjectName("addAllRecords_button")

        self.search_button = QtWidgets.QPushButton(self.centralwidget)
        self.search_button.setGeometry(QtCore.QRect(300, 80, 200, 30))
        self.search_button.setObjectName("search_button")

        self.update_button = QtWidgets.QPushButton(self.centralwidget)
        self.update_button.setGeometry(QtCore.QRect(300, 120, 200, 30))
        self.update_button.setObjectName("update_button")

        self.remove_button = QtWidgets.QPushButton(self.centralwidget)
        self.remove_button.setGeometry(QtCore.QRect(300, 160, 200, 30))
        self.remove_button.setObjectName("remove_button")

        self.close_button = QtWidgets.QPushButton(self.centralwidget)
        self.close_button.setGeometry(QtCore.QRect(300, 200, 200, 30))
        self.close_button.setObjectName("close_button")

        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.addAllRecords_button.clicked.connect(self.add_all_records)
        self.search_button.clicked.connect(self.search_record)
        self.update_button.clicked.connect(self.update_record)
        self.remove_button.clicked.connect(self.remove_record)
        self.close_button.clicked.connect(self.close_app)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Student Manager"))
        self.ID_lable.setText(_translate("MainWindow", "ID"))
        self.lastName_lable.setText(_translate("MainWindow", "Last Name"))
        self.name_lable.setText(_translate("MainWindow", "Name"))
        self.subject_lable.setText(_translate("MainWindow", "Subject"))
        self.grade_label.setText(_translate("MainWindow", "Grade"))
        self.addAllRecords_button.setText(_translate("MainWindow", "Add all records"))
        self.search_button.setText(_translate("MainWindow", "Search"))
        self.update_button.setText(_translate("MainWindow", "Update"))
        self.remove_button.setText(_translate("MainWindow", "Remove"))
        self.close_button.setText(_translate("MainWindow", "Close"))

    def add_all_records(self):
        collection.delete_many({})
        for _ in range(10):
            record = {
                "LastName": random.choice(LNames),
                "FirstName": random.choice(FNames),
                "Subject": random.choice(Subjects),
                "Grade": random.choice(Points)
            }
            collection.insert_one(record)
        QtWidgets.QMessageBox.information(None, "Success", "10 records added to MongoDB.")

    def search_record(self):
        query = {}
        if self.ID.text():
            try:
                query["_id"] = ObjectId(self.ID.text())
            except:
                QtWidgets.QMessageBox.warning(None, "Invalid ID", "ID must be a valid MongoDB ObjectId.")
                return
        if self.lastName.text():
            query["LastName"] = self.lastName.text()
        if self.name_2.text():
            query["FirstName"] = self.name_2.text()
        if self.subject.text():
            query["Subject"] = self.subject.text()
        if self.grade.text():
            query["Grade"] = self.grade.text()

        results = list(collection.find(query))
        if results:
            message = "\n".join(
                f"{r['_id']} | {r['FirstName']} {r['LastName']} | {r['Subject']} | {r['Grade']}"
                for r in results
            )
        else:
            message = "No matching records found."

        QtWidgets.QMessageBox.information(None, "Search Results", message)

    def update_record(self):
        if not self.ID.text():
            QtWidgets.QMessageBox.warning(None, "Missing ID", "Please enter an ID to update.")
            return
        try:
            _id = ObjectId(self.ID.text())
        except:
            QtWidgets.QMessageBox.warning(None, "Invalid ID", "ID must be a valid MongoDB ObjectId.")
            return

        update_fields = {}
        if self.lastName.text():
            update_fields["LastName"] = self.lastName.text()
        if self.name_2.text():
            update_fields["FirstName"] = self.name_2.text()
        if self.subject.text():
            update_fields["Subject"] = self.subject.text()
        if self.grade.text():
            update_fields["Grade"] = self.grade.text()

        if not update_fields:
            QtWidgets.QMessageBox.information(None, "No Update", "No fields to update.")
            return

        result = collection.update_one({"_id": _id}, {"$set": update_fields})
        if result.matched_count:
            QtWidgets.QMessageBox.information(None, "Updated", "Record updated successfully.")
        else:
            QtWidgets.QMessageBox.warning(None, "Not Found", "No record found with that ID.")

    def remove_record(self):
        if not self.ID.text():
            QtWidgets.QMessageBox.warning(None, "Missing ID", "Please enter an ID to delete.")
            return
        try:
            _id = ObjectId(self.ID.text())
        except:
            QtWidgets.QMessageBox.warning(None, "Invalid ID", "ID must be a valid MongoDB ObjectId.")
            return

        result = collection.delete_one({"_id": _id})
        if result.deleted_count:
            QtWidgets.QMessageBox.information(None, "Deleted", "Record deleted successfully.")
        else:
            QtWidgets.QMessageBox.warning(None, "Not Found", "No record found with that ID.")

    def close_app(self):
        QtWidgets.QApplication.quit()



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
