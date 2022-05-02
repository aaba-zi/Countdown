# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainpage3.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

import inputLetter
import findWordFromDic
import time
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from workthread import WorkThread

global sec
sec=0
global wordlen
wordlen=0
global generatedWord

class Ui_MainWindow(object):
## global varibales
    vowelButton_Times=0
    timer=QTimer()
    workThread=WorkThread()
    c=[]
    generatedWord=[]
    number_answers=0

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(624, 680)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(134, 20, 361, 51))
        self.label.setMinimumSize(QtCore.QSize(361, 0))
        font = QtGui.QFont()
        font.setFamily("Monotype Corsiva")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(9)
        self.label.setFont(font)
        self.label.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.label.setAutoFillBackground(False)
        self.label.setStyleSheet("font: 75 italic 20pt \"Monotype Corsiva\";")
        self.label.setScaledContents(False)
        self.label.setObjectName("label")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(30, 90, 551, 141))
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.groupBox)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 60, 551, 89))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.textBrowser_4 = QtWidgets.QTextBrowser(self.horizontalLayoutWidget)
        self.textBrowser_4.setObjectName("textBrowser_4")
        self.horizontalLayout.addWidget(self.textBrowser_4)
        self.textBrowser_8 = QtWidgets.QTextBrowser(self.horizontalLayoutWidget)
        self.textBrowser_8.setObjectName("textBrowser_8")
        self.horizontalLayout.addWidget(self.textBrowser_8)
        self.textBrowser_9 = QtWidgets.QTextBrowser(self.horizontalLayoutWidget)
        self.textBrowser_9.setObjectName("textBrowser_9")
        self.horizontalLayout.addWidget(self.textBrowser_9)
        self.textBrowser_6 = QtWidgets.QTextBrowser(self.horizontalLayoutWidget)
        self.textBrowser_6.setObjectName("textBrowser_6")
        self.horizontalLayout.addWidget(self.textBrowser_6)
        self.textBrowser_7 = QtWidgets.QTextBrowser(self.horizontalLayoutWidget)
        self.textBrowser_7.setObjectName("textBrowser_7")
        self.horizontalLayout.addWidget(self.textBrowser_7)
        self.textBrowser_5 = QtWidgets.QTextBrowser(self.horizontalLayoutWidget)
        self.textBrowser_5.setObjectName("textBrowser_5")
        self.horizontalLayout.addWidget(self.textBrowser_5)
        self.textBrowser_3 = QtWidgets.QTextBrowser(self.horizontalLayoutWidget)
        self.textBrowser_3.setObjectName("textBrowser_3")
        self.horizontalLayout.addWidget(self.textBrowser_3)
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.horizontalLayoutWidget)
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.horizontalLayout.addWidget(self.textBrowser_2)
        self.textBrowser = QtWidgets.QTextBrowser(self.horizontalLayoutWidget)
        self.textBrowser.setObjectName("textBrowser")
        self.horizontalLayout.addWidget(self.textBrowser)
        self.label_2 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.label_11 = QtWidgets.QLabel(self.groupBox)
        self.label_11.setGeometry(QtCore.QRect(10, 9, 491, 51))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setStyleSheet("")
        self.label_11.setObjectName("label_11")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(20, 80, 581, 541))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")

        ## click button to input vowels
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(10, 170, 161, 28))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.input)

        ##
        ## click button to input consonants
        self.pushButton_2 = QtWidgets.QPushButton(self.frame)
        self.pushButton_2.setGeometry(QtCore.QRect(200, 170, 161, 28))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.input1)

        ##Countdown function
        ## click start
        self.lcdNumber = QtWidgets.QLCDNumber(self.frame)
        self.lcdNumber.setGeometry(QtCore.QRect(400, 160, 101, 51))
        self.lcdNumber.setSmallDecimalPoint(True)
        self.lcdNumber.setDigitCount(5)
        self.lcdNumber.setMode(QtWidgets.QLCDNumber.Dec)
        self.lcdNumber.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.lcdNumber.setObjectName("lcdNumber")
        self.timer.timeout.connect(self.countTime)


        ## groupBox _2
        self.groupBox_2 = QtWidgets.QGroupBox(self.frame)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 210, 561, 321))
        self.groupBox_2.setObjectName("groupBox_2")
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.groupBox_2)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(0, 60, 551, 171))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_12 = QtWidgets.QLabel(self.groupBox_2)
        self.label_12.setGeometry(QtCore.QRect(4, 10, 541, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")

        ##Submit button in the bottle of frame

        self.pushButton_3 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_3.setGeometry(QtCore.QRect(170, 260, 171, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.Answer_Game)

        ## show answers
        self.textBrowser_10 = QtWidgets.QTextBrowser(self.groupBox_2)
        self.textBrowser_10.setGeometry(QtCore.QRect(0, 60, 561, 171))
        self.textBrowser_10.setObjectName("textBrowser_10")

        self.textEdit = QtWidgets.QTextEdit(self.groupBox_2)
        self.textEdit.setGeometry(QtCore.QRect(493, 20, 61, 31))
        self.textEdit.setObjectName("textEdit")
        self.label_4 = QtWidgets.QLabel(self.groupBox_2)
        self.label_4.setGeometry(QtCore.QRect(380, 20, 111, 31))
        self.label_4.setObjectName("label_4")
        self.textEdit_2 = QtWidgets.QTextEdit(self.groupBox_2)
        self.textEdit_2.setGeometry(QtCore.QRect(240, 20, 111, 31))
        self.textEdit_2.setObjectName("textEdit_2")
        self.label_3 = QtWidgets.QLabel(self.groupBox_2)
        self.label_3.setGeometry(QtCore.QRect(140, 25, 91, 21))
        self.label_3.setObjectName("label_3")

        ## pushbutton_4 is a button to control countdown function
        self.pushButton_4 = QtWidgets.QPushButton(self.frame)
        self.pushButton_4.setGeometry(QtCore.QRect(520, 160, 51, 51))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.clicked.connect(self.work)

        ## reset
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(490, 20, 93, 51))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_5.clicked.connect(self.reset)
        self.frame.raise_()
        self.label.raise_()
        self.groupBox.raise_()
        self.pushButton_5.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 624, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Countdown Word Game"))
        self.groupBox.setTitle(_translate("MainWindow", "GroupBox"))
        self.label_11.setText(_translate("MainWindow", "Please press Button to input letter :"))
        self.pushButton.setText(_translate("MainWindow", "Vowels"))
        self.pushButton_2.setText(_translate("MainWindow", "Consonants"))
        self.groupBox_2.setTitle(_translate("MainWindow", "-------------------------------------------------------------------------------------------------------------"))
        self.label_12.setText(_translate("MainWindow", "Answers"))
        self.pushButton_3.setText(_translate("MainWindow", "Submit"))
        self.label_3.setText(_translate("MainWindow", "input answer : "))
        self.label_4.setText(_translate("MainWindow", "length of answer :"))
        self.pushButton_4.setText(_translate("MainWindow", "Start"))
        self.pushButton_5.setText(_translate("MainWindow", "Reset"))


##Function to Generate Vowels
    def input(self):
        if self.vowelButton_Times==0 :

            number=inputLetter.vowel()
            self.generatedWord.append(number)
            self.textBrowser_4.setText(number)
       #     print(self.generatedWord)
        elif self.vowelButton_Times==1 :
            number=inputLetter.vowel()
            self.generatedWord.append(number)
            self.textBrowser_8.setText(number)
        #    print(self.generatedWord)
        elif self.vowelButton_Times==2 :
            number=inputLetter.vowel()
            self.generatedWord.append(number)
            self.textBrowser_9.setText(number)
        elif self.vowelButton_Times==3 :
            number=inputLetter.vowel()
            self.generatedWord.append(number)
            self.textBrowser_6.setText(number)
        elif self.vowelButton_Times==4 :
            number=inputLetter.vowel()
            self.generatedWord.append(number)
            self.textBrowser_7.setText(number)
        elif self.vowelButton_Times==5 :
            number=inputLetter.vowel()
            self.generatedWord.append(number)
            self.textBrowser_5.setText(number)
        elif self.vowelButton_Times==6 :
            number=inputLetter.vowel()
            self.generatedWord.append(number)
            self.textBrowser_3.setText(number)
        elif self.vowelButton_Times==7 :
            number=inputLetter.vowel()
            self.generatedWord.append(number)
            self.textBrowser_2.setText(number)
        elif self.vowelButton_Times==8 :
            number=inputLetter.vowel()
            self.generatedWord.append(number)
            self.textBrowser.setText(number)
            self.work()
        else :
            self.pushButton.clicked.connect(self.msg)
        self.vowelButton_Times=self.vowelButton_Times+1
      #  print(self.vowelButton_Times)


## Function to Generate  Consonants
    def input1(self):
       # print(self.vowelButton_Times)
       # print("-----------")
        if self.vowelButton_Times==0 :
          #  self.work()
            number=inputLetter.con()
            print(number)
            self.generatedWord.append(number)
            self.textBrowser_4.setText(number)
        elif self.vowelButton_Times==1 :
            number=inputLetter.con()
            self.generatedWord.append(number)
            self.textBrowser_8.setText(number)
        elif self.vowelButton_Times==2 :
            number=inputLetter.con()
            self.generatedWord.append(number)
            self.textBrowser_9.setText(number)
        elif self.vowelButton_Times==3 :
            number=inputLetter.con()
            self.generatedWord.append(number)
            self.textBrowser_6.setText(number)
        elif self.vowelButton_Times==4 :
            number=inputLetter.con()
            self.generatedWord.append(number)
            self.textBrowser_7.setText(number)
        elif self.vowelButton_Times==5 :
            number=inputLetter.con()
            self.generatedWord.append(number)
            self.textBrowser_5.setText(number)
        elif self.vowelButton_Times==6 :
            number=inputLetter.con()
            self.generatedWord.append(number)
            self.textBrowser_3.setText(number)
        elif self.vowelButton_Times==7 :
            number=inputLetter.con()
            self.generatedWord.append(number)
            self.textBrowser_2.setText(number)
        elif self.vowelButton_Times==8 :
            number=inputLetter.con()
            self.generatedWord.append(number)
            self.textBrowser.setText(number)
            self.work()
        else :
            self.pushButton_2.clicked.connect(self.msg)
        self.vowelButton_Times=self.vowelButton_Times+1
      #  print(self.vowelButton_Times)

    def msg(self):
        reply = QMessageBox.information(QtWidgets.QWidget(),"Warning","out of range", QMessageBox.Yes | QMessageBox.No)

##Generate Answer in a other window
    def getGeneratedWord(self):
        self.generatedWord=self.generatedWord
        print(self.generatedWord)

    def Answer_Game(self):
        print(self.generatedWord)
        print("!!!!!!!")
        findWordFromDic.set_input_word(self.generatedWord)
        print(self.generatedWord)
        print('------')

        ## get content(wordlength  and input word ) from textEdit and textEdit_2
        wordlen= self.textEdit.toPlainText()
        input=self.textEdit_2.toPlainText()

        ##get infor[] from findWordFromDic
        c=findWordFromDic.infor
        number_answers=0

        ##set cc
        cc=[]

        if wordlen=='':
            wordlen=5
        if input=='' :
            self.input=''

        for i in c:
            if len(i)>=int(wordlen) :
                cc.append(i)
                self.textBrowser_10.append(i)
                number_answers=number_answers+1
        if number_answers==0 :
            self.textBrowser_10.append('No answer')

        if str(input) in cc :
            reply = QMessageBox.information(QtWidgets.QWidget(),"Congraulation","Time : spend "+ str(sec) +"seconds to get answer", QMessageBox.Yes | QMessageBox.No)
        else  :
            reply = QMessageBox.information(QtWidgets.QWidget(),"Sorry","Time : spend "+ str(sec) +"seconds ", QMessageBox.Yes | QMessageBox.No)

  ## Function of Countdown
    def countTime(self):
        global  sec
        sec += 1
        if sec <= 30:
            self.lcdNumber.display(sec)          # sec + 1

    def work(self):
        self.timer.start(1000)               #start counting
        self.workThread.start()        
        if sec > 30:
            self.timeStop
            self.workThread.trigger.connect(self.timeStop)  

    def timeStop(self):
        self.timer.stop()
        print("END",self.lcdNumber.value())
        global sec
        # sec=0

    def reset(self):
        global generatedWord
        self.generatedWord=None
        self.generatedWord=[]
        global sec
        sec=0
        self.vowelButton_Times=0
        global c
        self.c=[]
        self.timeStop()
        self.number_answers=0
        self.textBrowser.clear()
        self.textBrowser_2.clear()
        self.textBrowser_3.clear()
        self.textBrowser_4.clear()
        self.textBrowser_5.clear()
        self.textBrowser_6.clear()
        self.textBrowser_7.clear()
        self.textBrowser_8.clear()
        self.textBrowser_9.clear()
        self.textBrowser_10.clear()


