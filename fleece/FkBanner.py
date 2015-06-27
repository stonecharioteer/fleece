from PyQt4 import QtGui

class FkBanner(QtGui.QWidget):
	def __init__(self):
		super(FkBanner, self).__init__()
		self.createUI()
		self.createEvents()

	def createUI(self):
		self.fk_icon = QtGui.QLabel()
		self.notification_button = QtGui.QPushButton()
		self.cart_button = QtGui.QPushButton()
		self.search_entry_field = QtGui.QLineEdit()
		self.search_button = QtGui.QPushButton()
		self.menu_button = QtGui.QPushButton()
		self.layout = QtGui.QHBoxLayout()
		self.layout.addWidget(self.fk_icon,1)
		self.layout.addStretch(3)
		self.layout.addWidget(self.search_entry_field,2)
		self.layout.addWidget(self.search_button,1)
		self.layout.addWidget(self.notification_button,1)
		self.layout.addWidget(self.menu_button,1)
		self.setLayout(self.layout)

	def createEvents(self):
		self.search_button.clicked.connect(self.toggleSearch)

	def toggleSearch(self):
		self.search_entry_field.setVisible(not self.search_entry_field.isVisible())



