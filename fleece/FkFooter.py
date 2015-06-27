from PyQt4 import QtGui

class FkFooter(QtGui.QWidget):
	def __init__(self):
		super(FkFooter,self).__init__()
		self.createUI()

	def createUI(self):
		self.share_now_button = QtGui.QWidget()
		self.add_to_cart_button = QtGui.QWidget()
		self.buy_now_button = QtGui.QWidget()
		self.layout = QtGui.QHBoxLayout()
		self.layout.addWidget(self.share_now_button,1)
		self.layout.addWidget(self.add_to_cart_button,1)
		self.layout.addWidget(self.buy_now_button,2)
		self.setLayout(self.layout)
