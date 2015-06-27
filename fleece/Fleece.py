from PyQt4 import QtGui
from FkBanner import FkBanner
from FkProductPage import FkProductPage
from FkFooter import FkFooter

class Fleece(QtGui.QMainWindow):
	def __init__(self):
		super(Fleece, self).__init__()
		self.createUI()

	def createUI(self):
		self.banner = FkBanner()
		self.productArea = FkProductPage()		
		self.footer = FkFooter()
		self.layout = QtGui.QVBoxLayout()
		self.layout.addWidget(self.banner,1)
		self.layout.addWidget(self.productArea,4)
		self.layout.addWidget(self.footer,1)
		
		self.main_widget = QtGui.QWidget()
		self.main_widget.setLayout(self.layout)
		self.setCentralWidget(self.main_widget)
		self.show()
