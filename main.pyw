#Fleece main
from fleece.Fleece import Fleece

if __name__  == "__main__":
	import sys
	from PyQt4 import QtGui
	app = QtGui.QApplication([])
	fleece_app = Fleece()
	sys.exit(app.exec_())