import sys
from PyQt4 import QtGui

app = QtGui.QApplication(sys.argv)

widget = QtGui.Qwidget()
widget.resize(250,150)
widget.setWindowTitle('simple')
widget.show()


sys.exit(app.exec_())
