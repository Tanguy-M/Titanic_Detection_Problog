import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import * 
from PyQt5.QtCore import * 
from PyQt5.QtWidgets import * 
from Pre_processing import *
from Evaluation import *

class Ui_Dialog(object):
    def setupUi(self, Dialog):

        #Main frame with the fields and buttons
        Dialog.setObjectName("Dialog")
        Dialog.resize(1202, 704)
        Dialog.setMinimumSize(QtCore.QSize(8, 6))
        Dialog.setSizeIncrement(QtCore.QSize(2, 2))
        Dialog.setStyleSheet("background-color: rgb(247, 251, 255);")

        # Course information label
        label = QLabel("Hellenic Mediterranean University", self) 
        label.setGeometry(350, 50, 600, 40) 
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        label.setFont(font)
        label = QLabel("Advanced Topics In Artificial Intelligence 2022", self) 
        label.setGeometry(460, 675, 300, 25) 

        #Submit button
        #self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton = QPushButton('Submit', self)
        self.pushButton.setGeometry(QtCore.QRect(500, 610, 161, 51))

        # Submit button style
        self.pushButton.setStyleSheet("color: white;\n"
                                      "background-color: rgb(255, 110, 58);\n"
                                      "border-style: outset;\n"
                                      "border-width: 2px;\n"
                                      "border-radius: 10px;\n"
                                      "border-color: black;\n"
                                      "font: bold 14px;\n"
                                      "padding : 6px;\n"
                                      "min-width: 10px;")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setGeometry(700, 350, 300, 50) 

        # Test_button
        self.pushButton_3 = QPushButton('Test Training', self)
        self.pushButton_3.setGeometry(QtCore.QRect(15, 650, 141, 41))

        # Exit button style
        self.pushButton_3.setStyleSheet("background-color: rgb(20, 50, 250);\n"
                                        "color: white;\n"
                                        "border-style: outset;\n"
                                        "border-width: 2px;\n"
                                        "border-radius: 10px;\n"
                                        "border-color: black;\n"
                                        "font: bold 14px;\n"
                                        "padding : 6px;\n"
                                        "min-width: 10px;")
        self.pushButton_3.setObjectName("pushButton_3")

        # Exit button
        #self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2 = QPushButton('Exit', self)
        self.pushButton_2.setGeometry(QtCore.QRect(1050, 650, 141, 41))

        # Exit button style
        self.pushButton_2.setStyleSheet("background-color: rgb(255, 0, 0);\n"
                                        "color: white;\n"
                                        "border-style: outset;\n"
                                        "border-width: 2px;\n"
                                        "border-radius: 10px;\n"
                                        "border-color: black;\n"
                                        "font: bold 14px;\n"
                                        "padding : 6px;\n"
                                        "min-width: 10px;")
        self.pushButton_2.setObjectName("pushButton_2")

        

        #Sex textarea input
        self.combo_box_sex = QComboBox(self) 
        self.combo_box_sex.setGeometry(200, 200, 300, 50) 
        sex_list = ["Male", "Female"] 
        self.combo_box_sex.setEditable(False) 
        self.combo_box_sex.addItems(sex_list)  
        label = QLabel("Sex : ", self) 
        label.setGeometry(200, 175, 300, 25) 

        #Class textarea input
        self.combo_box_class = QComboBox(self) 
        self.combo_box_class.setGeometry(200, 275, 300, 50) 
        pclass_list = ["1st", "2nd", "3rd"] 
        self.combo_box_class.setEditable(False) 
        self.combo_box_class.addItems(pclass_list)  
        label = QLabel("Class : ", self) 
        label.setGeometry(200, 250, 300, 25) 

        #Parch textarea input
        self.combo_box_parch = QComboBox(self) 
        self.combo_box_parch.setGeometry(200, 350, 300, 50) 
        pclass_list = ["0", "1", "2","3+"] 
        self.combo_box_parch.setEditable(False) 
        self.combo_box_parch.addItems(pclass_list)  
        label = QLabel("Parents / Childrens : ", self) 
        label.setGeometry(200, 325, 300, 25) 

        #Age textarea input
        self.textbox_age = QLineEdit(self)
        self.textbox_age.setGeometry(700, 200, 300, 50) 
        label = QLabel("Age (0-90) : ", self) 
        label.setGeometry(700, 175, 300, 25) 

        #Fare textarea input
        self.textbox_fare = QLineEdit(self)
        self.textbox_fare.setGeometry(700, 275, 300, 50) 
        label = QLabel("Fare (0-600$) : ", self) 
        label.setGeometry(700, 250, 300, 25) 

        # Result output label
        label = QLabel("Result :", self) 
        label.setGeometry(450, 560, 300, 50) 
        self.label_output = QtWidgets.QLabel(Dialog)
        self.label_output.setGeometry(QtCore.QRect(450, 600, 300, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_output.setFont(font)
        self.label_output.setStyleSheet("color: white;\n"
                                      "background-color: rgb(0, 255, 0);\n"
                                      "border-style: outset;\n"
                                      "border-width: 2px;\n"
                                      "border-radius: 10px;\n"
                                      "border-color: black;\n"
                                      "font: bold 14px;\n"
                                      "padding : 6px;\n"
                                      "min-width: 10px;")
        self.label_output.setObjectName("label_output")

        # Close button for the frame
        # Once the button is clicked then the frame will close
        self.pushButton_2.clicked.connect(self.close)

        # Once the button is clicked then clickMethod is called
        self.pushButton.clicked.connect(self.clickMethod)

        self.pushButton_3.clicked.connect(self.clickMethod_2)

    def clickMethod(self): #create the evidences and run the evaluation
        person_info = ""

        #check if the input is valid
        if not self.textbox_age.text().isnumeric() or not self.textbox_fare.text().isnumeric():
            return

        if float(self.textbox_fare.text()) > 600 or float(self.textbox_fare.text()) < 0 or int(self.textbox_age.text()) > 90 or int(self.textbox_age.text()) < 0:
            return

        #add Sex
        if (self.combo_box_sex.currentText() == "Male"):
            person_info += "evidence(sex,true)."#male
        else:
            person_info += "evidence(sex,false)."#female

        #add Class
        if (self.combo_box_class.currentText() == "1st"):
            person_info += "\nevidence(classs,true)."#1 class
        else:
            person_info += "\nevidence(classs,false)."#2 or 3 class

        #add Parch
        if (self.combo_box_parch.currentText() <= str(TRESH_PARCH)):
            person_info += "\nevidence(parch,true)."
        else:
            person_info += "\nevidence(parch,false)."
            
        #add Age
        if ( int(self.textbox_age.text()) <= TRESH_ADULT):
            person_info += "\nevidence(young,true)."
        elif(int(self.textbox_age.text()) <= TRESH_OLD and TRESH_ADULT < int(self.textbox_age.text())):
            person_info += "\nevidence(adult,true)."
        else:
            person_info += "\nevidence(old,true)."

        #add Fare
        nfare = np.log(float(self.textbox_fare.text())+1)
        if (nfare <= TRESH_AVERAGE):
            person_info += "\nevidence(low,true)."
        elif(nfare > TRESH_AVERAGE and nfare <= TRESH_HIGH):
            person_info += "\nevidence(average,true)."
        else:
            person_info += "\nevidence(high,true)."

        person_info += "\n\nquery(survived)."

        [r, g] = get_evaluation(person_info)
        
        self.label_output.setText("Survivability  ratio : " + format(r, ".4f"))
        

    def clickMethod_2(self): #call evaluation.py to get the ratio of the survivors
        test_evaluation()
        
        
class MainWindow(QtWidgets.QMainWindow, Ui_Dialog):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent=parent)
        self.setupUi(self)
        self.setWindowTitle("Survivor detection by Tanguy MERLE")

def main():
   app = QtWidgets.QApplication(sys.argv)
   ex = MainWindow()
   ex.show()
   sys.exit(app.exec_())
if __name__ == '__main__':
   main()



