from PyQt4 import QtGui
class FkProductPage(QtGui.QWidget):
	def __init__(self, fsn=None):
		super(FkProductPage,self).__init__()
		if fsn is None:
			self.display = False
		else:
			self.fsn = fsn
			self.display = True
		self.createUI()

	def createUI(self):
		self.image_widget = QtGui.QLabel("Image here!")
		self.specs_stuff = QtGui.QLabel("Text goes here")
		self.layout = QtGui.QHBoxLayout()
		self.layout.addWidget(self.image_widget)
		self.layout.addWidget(self.specs_stuff)
	