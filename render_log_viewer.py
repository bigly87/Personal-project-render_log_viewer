'''
Create a render-log analysis UI.

A Qt UI that allows you to browse for a log file and display the following information:
1. a summary of render time and memory usage
2. all errors and warnings should be clearly displayed in the UI
3. the UI should have a separate sub-widgets tab for displaying separate sections of the log file
4. follow python pep8 standard
5. if you upload the result to GitHub, do not attach the sample render logs

We use https://pypi.org/project/PySide2/ for creating python UIs.

'''

import sys
import os
import utils



from PySide2 import QtCore, QtWidgets, QtGui
from PySide2.QtWidgets import QApplication, QPushButton,  QWidget, QFileDialog, QMainWindow, QLineEdit


from render_log_viewer_ui import Ui_mainwindow


class MainWindow(QtWidgets.QMainWindow, Ui_mainwindow):
    """
    Args:
       QMainWindow: The name of our main widget class in render_log_viewer.ui
       Ui_mainwindow: The class object in render_log_viewer_ui.py file 
    """
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)

        self.browsebutton.clicked.connect(self.browsefiles)
    
        
    def browsefiles(self):
         """

         """
         fname = QFileDialog.getOpenFileName(self, "Browse log files", "D:\Pipeline\Resumes\Cinesite\Test Project\Log Files", "(*.log)")
         self.filepath.setText(fname[0])
         self.path = self.filepath.text()

         paragraphs_contain_warning = utils.get_warnings(logfile_path=self.path)
         self.warningbox.clear()
         self.warningbox.setPlainText("\n".join(paragraphs_contain_warning))

        
         paragraphs_contain_errors = utils.get_errors(logfile_path=self.path)
         self.errorbox.clear()
         self.errorbox.setPlainText("\n".join(paragraphs_contain_errors))

         paragraphs_contain_info = utils.get_infos(logfile_path=self.path)
         self.infobox.clear()
         self.infobox.setPlainText("\n".join(paragraphs_contain_info))
        
        

app = QtWidgets.QApplication(sys.argv)

window = MainWindow()
window.show()
app.exec_()