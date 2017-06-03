'''
WeightsPanel class
'''

import pymel.core as pm

weightFieldWidth = 100
weightNameWidth = 200


#-------------------------------------------------------------------------------



class WeightsPanel:

	def __init__(self, onNormWeightsChangedCallback = None,
		showTotals = True):
		self.weightFieldWidth = 100
		self.entries = []
		self.onNormWeightsChangedCallback = onNormWeightsChangedCallback
		self.showTotals = showTotals
		
	
	def addWeight(self, label, weight, color=None):
		if not label:
			label = attrName
			
		entry = [weight, (label, color)]
		self.entries.append(entry)
	
	
	def updateNormWeights(self):
		layout = self.layout
		rows = layout.getChildren()
		firstWeightRow = 2

		# Update all normalised weights
		totalWeight = 0
		for weight, weightAttr in self.entries:
			totalWeight += weight

		if totalWeight == 0:
			self.normFactor = 0
		else:
			self.normFactor = self.totalNormWeight/totalWeight

		for entryIdx, entry in enumerate(self.entries):
			weight, weightAttr = entry
			if totalWeight == 0:
				normWeight = 0.0
			else:
				normWeight = weight*self.normFactor
				
			row = rows[entryIdx + firstWeightRow]
			pm.text(row.getChildren()[2], edit=True, label="%0.3f"%normWeight)	
		
		if self.showTotals:	
			row = rows[len(self.entries) + firstWeightRow + 1]
			pm.floatField(row.getChildren()[1], edit=True, value=totalWeight)
			pm.floatField(row.getChildren()[2], edit=True, \
				value=self.totalNormWeight)	
		
		if self.onNormWeightsChangedCallback:
			self.onNormWeightsChangedCallback(self)
		
	
	def onNormWeightTotalChanged(self):
		layout = self.layout
		rows = layout.getChildren()
		firstWeightRow = 2
		row = rows[len(self.entries) + firstWeightRow + 1]
		self.totalNormWeight = row.getChildren()[2].getValue()
		self.updateNormWeights()
	
	
	def onWeightChanged(self, entryIdx):
		
		# A weight has changed.
		# Retrieve it from the control
		firstWeightRow = 2
		
		layout = self.layout
		rows = layout.getChildren()
		row = rows[entryIdx + firstWeightRow]
		valField = row.getChildren()[1]
		val = valField.getValue()
		self.entries[entryIdx][0] = val;
		
		self.updateNormWeights()
		
	
	def create(self):
		minWeight = 0.0
		layout = pm.columnLayout(co=("both", 20))
		
		row = pm.rowLayout(nc = 3)
		pm.text(label="name", align="left", width=weightNameWidth)
		pm.text(label="weight", align="left", width=weightFieldWidth)
		pm.text(label="normalised", align="left", width=weightFieldWidth)
		pm.setParent("..")
		
		pm.text(label="")
		
		totalNormWeight = 0
		for entryIdx, entry in enumerate(self.entries):
			weight, (label, color) = entry
			totalNormWeight += weight
			row = pm.rowLayout(nc = 4, parent=layout)
			textCtrl = pm.text(align="left", label=label, width=weightNameWidth, parent=row)
			if color:
				pm.text(textCtrl, e=True, backgroundColor=color)
			pm.floatField(minValue = minWeight, value=weight, width=weightFieldWidth, changeCommand=pm.Callback(self.onWeightChanged, entryIdx))
			pm.text(align="left", label="0", width=weightFieldWidth)
			pm.setParent("..")

		if self.showTotals:
			pm.text(label="") #row = pm.rowLayout(height = 10, parent=layout)

			row = pm.rowLayout(nc = 3, parent=layout)
			pm.text("Total:  ", align="right", parent=row, width=weightNameWidth)
			pm.floatField(value=0, parent=row, width=weightFieldWidth, enable=False)
			pm.floatField(value=totalNormWeight, parent=row, width=weightFieldWidth, changeCommand=pm.Callback(self.onNormWeightTotalChanged))
			pm.setParent("..") #totalsRow

		pm.text(label="") #row = pm.rowLayout(height = 10, parent=layout)

		pm.setParent("..") #layout

		self.layout = layout
		self.totalNormWeight = 100.0	 #totalNormWeight
		
		if len(self.entries) > 0:
			self.onWeightChanged(0)

		#win.show()



def _testCallback(wnd):
	print("callback")

def main():

	parentWnd = pm.window("PARENT WINDOW", width=400, height=400)
	parentWnd.show()

	wnd = WeightsPanel(onNormWeightsChangedCallback=_testCallback)
	wnd.addWeight("weight A", 1.0, color=[1, 0, 0])
	wnd.addWeight("weight B", 2.0, color=[0, 1, 0])
	wnd.addWeight("weight C", 3.0, color=[0, 0, 1])
	wnd.create()


if __name__=="__main__":
	main()



	
