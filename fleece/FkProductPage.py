from PyQt4 import QtGui

class FkProductPage():

	def __init__(self, fsn=None):
		super(FkProductPage,self).__init__()
		if fsn is None:
			self.display = False
		else:
			self.fsn = fsn
			self.display = True
		self.createUI()

	def createUI(self):
		self.