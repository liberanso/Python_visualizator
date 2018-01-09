#!/usr/bin/python

import os
import sys

from PyQt4 import QtGui, QtCore 

class Example(QtGui.QWidget):
    
    def __init__(self):
        super(Example, self).__init__()
        
        self.initUI()
        
    def initUI(self):      

        self.setGeometry(300, 300, 620, 320)
        self.setWindowTitle('Graphics')
        self.show()

    def paintEvent(self, e):

        qp = QtGui.QPainter()
        qp.begin(self)
        
        self.drawBox(qp)
        
        self.drawGrid(qp)

        qp.end()
        
    def drawBox(self, qp):
    	pen = QtGui.QPen(QtCore.Qt.darkGray, 2, QtCore.Qt.SolidLine)
    	brush = QtGui.QBrush(QtCore.Qt.darkGray, QtCore.Qt.SolidPattern)
        qp.setPen(pen)
        qp.setBrush(brush)
        qp.drawRect(20,20,580,280)

    def drawGrid(self,qp):
    	pen = QtGui.QPen(QtCore.Qt.white, 2, QtCore.Qt.SolidLine)
    	qp.setPen(pen)
    	for x in range(30,600,10):
    		for y in range(30,300,10):
    			qp.drawPoint(x,y)
    	pen.setColor(QtCore.Qt.gray)
    	pen.setStyle(QtCore.Qt.DashLine)
    	qp.setPen(pen)
    	for x in range(30,600,20):
    		qp.drawLine(x,30,x,280)
    	for y in range(30,300,20):
    		qp.drawLine(30,y,580,y)
    			
             
        
def main():
    
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    pal = ex.palette();
    pal.setColor(ex.backgroundRole(),QtCore.Qt.darkBlue)
    ex.setPalette(pal)
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
