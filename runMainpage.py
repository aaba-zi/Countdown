from PyQt5 import QtWidgets
from mainpage import Ui_MainWindow
#from Answers_page import Ui_Form

class mywindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(mywindow,self).__init__()
       # MainWindow=QtWidgets.QMainWindow()
        self.new=Ui_MainWindow()
        self.new.setupUi(self)

if __name__=="__main__":
    import sys
    app=QtWidgets.QApplication(sys.argv)
  #  MainWindow=QtWidgets.QMainWindow()
    myshow=mywindow()
  #  myshow.setupUi(MainWindow)
    myshow.show()
    sys.exit(app.exec_())
