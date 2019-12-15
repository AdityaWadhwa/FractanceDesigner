import sys
import numpy
import math
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from PyQt5.QtCore import Qt, QRegExp
from PyQt5.QtGui import QRegExpValidator
from PyQt5.QtWidgets import (QApplication, QCheckBox, QGridLayout, QGroupBox,
        QMenu, QPushButton, QRadioButton, QVBoxLayout, QWidget, QSlider, QLabel, QHBoxLayout, QLineEdit, QMessageBox,QTabWidget)
from Methodss import calculator
from sympy import pretty_print as pp

class Window(QWidget):
    def __init__(self, parent=None):
        super(Window, self).__init__(parent)
        self.layout = QVBoxLayout(self)
        
        # Initialize tab screen
        self.tabs = QTabWidget()
        self.inputTab = QWidget()
        self.outputTab = QWidget()
        self.tabs.resize(800,400)
        
        # Add tabs
        self.tabs.addTab(self.inputTab,"Parameters")
        self.tabs.addTab(self.outputTab,"Results")
        
#    def initInputUI(self):

        self.inputTab.layout = QGridLayout()

        self.methodBox = QGroupBox("Approximation Method")
        
        self.mb_radio1 = QRadioButton("Adhikari Method")
        self.mb_radio2 = QRadioButton("Valsa Method")
        self.mb_radio3 = QRadioButton("Mastuda Method")
        self.mb_radio4 = QRadioButton("Theile Second Method")
        self.mb_radio5 = QRadioButton("Oustaloup Method")
        self.mb_radio6 = QRadioButton("Modified Oustaloup Method")
        self.mb_radio7 = QRadioButton("Charef Method")
        self.mb_radio8 = QRadioButton("Carlson Method")
        
        self.mb_radio1.setChecked(True)

        self.vbox = QVBoxLayout()
        self.vbox.addWidget(self.mb_radio1)
        self.vbox.addWidget(self.mb_radio2)
        self.vbox.addWidget(self.mb_radio3)
        self.vbox.addWidget(self.mb_radio4)
        self.vbox.addWidget(self.mb_radio5)
        self.vbox.addWidget(self.mb_radio6)
        self.vbox.addWidget(self.mb_radio7)
        self.vbox.addWidget(self.mb_radio8)
        self.vbox.addStretch(1)

        self.methodBox.setLayout(self.vbox)

        self.inputTab.layout.addWidget(self.methodBox, 0, 0)
        
        self.circuitBox = QGroupBox("Circuit Method")
        
        self.cb_radio1 = QRadioButton("Not a s domain method")
        self.cb_radio2 = QRadioButton("First Foster")
        self.cb_radio3 = QRadioButton("Second Foster")
        self.cb_radio4 = QRadioButton("First Cauer")
        self.cb_radio5 = QRadioButton("Second Cauer")
    
        self.cb_radio1.setChecked(True)

        self.vbox = QVBoxLayout()
        self.vbox.addWidget(self.cb_radio1)
        self.vbox.addWidget(self.cb_radio2)
        self.vbox.addWidget(self.cb_radio3)
        self.vbox.addWidget(self.cb_radio4)
        self.vbox.addWidget(self.cb_radio5)
        self.vbox.addStretch(1)

        self.circuitBox.setLayout(self.vbox)

        self.inputTab.layout.addWidget(self.circuitBox, 0, 1)


        self.frequencyBox = QGroupBox("Frequency Parameters")

        self.vbox = QVBoxLayout()

        self.fl_label = QLabel("Fl")

        self.fl_slider = QSlider(Qt.Horizontal)
        self.fl_slider.setMinimum(-10)
        self.fl_slider.setMaximum(10)
        self.fl_slider.setValue(0)
        self.fl_slider.setTickPosition(QSlider.TicksBelow)
        self.fl_slider.setTickInterval(1)
        self.fl_slider.valueChanged.connect(self.changeFl)

        self.fl_value = QLabel("0")

        self.hbox = QHBoxLayout()
        self.hbox.addWidget(self.fl_label)
        self.hbox.addWidget(self.fl_slider)
        self.hbox.addWidget(self.fl_value)

        self.vbox.addLayout(self.hbox)
        
        self.fu_label = QLabel("Fu")

        self.fu_slider = QSlider(Qt.Horizontal)
        self.fu_slider.setMinimum(-10)
        self.fu_slider.setMaximum(10)
        self.fu_slider.setValue(6)
        self.fu_slider.setTickPosition(QSlider.TicksBelow)
        self.fu_slider.setTickInterval(1)
        self.fu_slider.valueChanged.connect(self.changeFu)

        self.fu_value = QLabel("6")

        self.hbox = QHBoxLayout()
        self.hbox.addWidget(self.fu_label)
        self.hbox.addWidget(self.fu_slider)
        self.hbox.addWidget(self.fu_value)

        self.vbox.addLayout(self.hbox)

        self.fstep_label = QLabel("Fstep")

        self.fstep_slider = QSlider(Qt.Horizontal)
        self.fstep_slider.setMinimum(0)
        self.fstep_slider.setMaximum(20)
        self.fstep_slider.setValue(2)
        self.fstep_slider.setTickPosition(QSlider.TicksBelow)
        self.fstep_slider.setTickInterval(1)
        self.fstep_slider.valueChanged.connect(self.changeFstep)

        self.fstep_value = QLabel("2")

        self.hbox = QHBoxLayout()
        self.hbox.addWidget(self.fstep_label)
        self.hbox.addWidget(self.fstep_slider)
        self.hbox.addWidget(self.fstep_value)

        self.vbox.addLayout(self.hbox)

        self.blank_label = QLabel("\t"*10+"10^")
        self.hbox = QHBoxLayout()
        self.hbox.addWidget(self.blank_label)
        self.vbox.addLayout(self.hbox)

        self.frequencyBox.setLayout(self.vbox)

        self.inputTab.layout.addWidget(self.frequencyBox, 1, 0)
        

        self.inputBox = QGroupBox("Input Parameters")

        self.vbox = QVBoxLayout()

        self.hbox = QHBoxLayout()
        self.F_label = QLabel("F")
        self.F_input = QLineEdit("1")
        self.hbox.addWidget(self.F_label)
        self.hbox.addWidget(self.F_input)
        self.vbox.addLayout(self.hbox)

        self.hbox = QHBoxLayout()
        self.alpha_label = QLabel("alpha")
        self.alpha_input = QLineEdit("-0.5")
        self.hbox.addWidget(self.alpha_label)
        self.hbox.addWidget(self.alpha_input)
        self.vbox.addLayout(self.hbox)
        
        self.hbox = QHBoxLayout()
        self.N_label = QLabel("N")
        self.N_input = QLineEdit("10")
        self.hbox.addWidget(self.N_label)
        self.hbox.addWidget(self.N_input)
        self.vbox.addLayout(self.hbox)
        
        self.inputBox.setLayout(self.vbox)

        self.inputTab.layout.addWidget(self.inputBox, 1, 1)


        self.simulateButton = QPushButton("Simulate")
        self.simulateButton.clicked.connect(self.simulate)
        self.inputTab.layout.addWidget(self.simulateButton,2,1)

        self.inputTab.setLayout(self.inputTab.layout)


#    def initOutputUI(self):
        self.outputTab.layout = QGridLayout()

        self.graphSelector = QGroupBox("Approximation Method")
        
        self.gs_radio1 = QRadioButton("Ideal")
        self.gs_radio2 = QRadioButton("Simulated")
        self.gs_radio3 = QRadioButton("Ideal+Simulated")
        self.gs_radio4 = QRadioButton("Error")
        
        self.gs_radio3.setChecked(True)

        self.gs_radio1.toggled.connect(self.updatePlot)
        self.gs_radio2.toggled.connect(self.updatePlot)
        self.gs_radio3.toggled.connect(self.updatePlot)
        self.gs_radio4.toggled.connect(self.updatePlot)    

        self.vbox = QVBoxLayout()
        self.vbox.addWidget(self.gs_radio1)
        self.vbox.addWidget(self.gs_radio2)
        self.vbox.addWidget(self.gs_radio3)
        self.vbox.addWidget(self.gs_radio4)
        self.vbox.addStretch(1)

        self.graphSelector.setLayout(self.vbox)

        self.outputTab.layout.addWidget(self.graphSelector, 0, 0)

        # a figure instance to plot on
        self.figure = Figure()

        # this is the Canvas Widget that displays the `figure`
        # it takes the `figure` instance as a parameter to __init__
        self.canvas = FigureCanvas(self.figure)
        
        self.outputTab.layout.addWidget(self.canvas, 0, 1)
        
        self.outputTab.setLayout(self.outputTab.layout)

        # Add tabs to widget
        self.layout.addWidget(self.tabs)
        self.setLayout(self.layout)
        
        self.setWindowTitle("Fractional Order Filters GUI Tool")
        self.resize(1000, 500)

        self.mb_radio1.toggled.connect(self.restrictions)
        self.mb_radio2.toggled.connect(self.restrictions)
        self.mb_radio3.toggled.connect(self.restrictions)
        self.mb_radio4.toggled.connect(self.restrictions)  
        self.mb_radio5.toggled.connect(self.restrictions)
        self.mb_radio6.toggled.connect(self.restrictions)
        self.mb_radio7.toggled.connect(self.restrictions)
        self.mb_radio8.toggled.connect(self.restrictions)

        self.restrictions()  

    def changeFstep(self):
        self.fstep_value.setText(str(self.fstep_slider.value()))

    def changeFl(self):
        self.fl_value.setText(str(self.fl_slider.value()))

    def changeFu(self):
        self.fu_value.setText(str(self.fu_slider.value()))

    def restrictions(self):
        if self.mb_radio1.isChecked() or self.mb_radio2.isChecked():
            self.cb_radio1.setEnabled(True)
            self.cb_radio2.setEnabled(False)
            self.cb_radio3.setEnabled(False)
            self.cb_radio4.setEnabled(False)
            self.cb_radio5.setEnabled(False)
            self.cb_radio1.setChecked(True)   
            input_validator = QRegExpValidator(QRegExp("-[0-9]"), self.N_input)
            self.N_input.setValidator(input_validator)     
        else :
            self.cb_radio1.setEnabled(False)
            self.cb_radio2.setEnabled(True)
            self.cb_radio3.setEnabled(True)
            self.cb_radio4.setEnabled(True)
            self.cb_radio5.setEnabled(True)
            self.cb_radio2.setChecked(True)        
            input_validator = QRegExpValidator(QRegExp("*"), self.N_input)
            self.N_input.setValidator(input_validator)     

        if self.mb_radio8.isChecked():
            self.N_input.setText("3")
    

    def simulate(self):

        if self.mb_radio1.isChecked():
            self.method = 'adhikari'
        elif self.mb_radio2.isChecked():
            self.method = 'valsa'
        elif self.mb_radio3.isChecked():
            self.method = 'mastuda'
        elif self.mb_radio4.isChecked():
            self.method = 'TheileSecond'
        elif self.mb_radio5.isChecked():
            self.method = 'Oustaloup'
        elif self.mb_radio6.isChecked():
            self.method = 'ModiOustaloup'
        elif self.mb_radio7.isChecked():
            self.method = 'Charef'
        elif self.mb_radio8.isChecked():
            self.method = 'Carlson'

        if self.cb_radio1.isChecked():
            self.circuit = 'None'
        elif self.cb_radio2.isChecked():
            self.circuit = 'FirstFoster'
        elif self.cb_radio3.isChecked():
            self.circuit = 'SecondFoster'
        elif self.cb_radio4.isChecked():
            self.circuit = 'FirstCauer'
        elif self.cb_radio5.isChecked():
            self.circuit = 'SecondCauer'

        self.fl = 10**self.fl_slider.value()
        self.fu = 10**self.fu_slider.value()
        self.fstep = 10**self.fstep_slider.value()

        self.F = float(self.F_input.text())
        self.alpha = float(self.alpha_input.text())
        self.N = int(self.N_input.text())
        
        if (self.fl>self.fu) and ((self.fu-self.fl)%self.fstep!=0) :
            alert = QMessageBox()
            alert.setText('Invalid Input')
            alert.exec_()
        else:
            try:
                if self.circuit == 'None':
                    self.Zmagi,self.Zphai,self.Zmag,self.Zpha,self.magError,self.phaError = calculator(self.F,self.alpha,self.fl,self.fu,self.method,self.fstep,self.N)
                else:
                    self.Zmagi,self.Zphai,self.Zmag,self.Zpha,self.magError,self.phaError = calculator(self.F,self.alpha,self.fl,self.fu,self.method,self.fstep,self.N,self.circuit)
                self.f = numpy.logspace(numpy.log10(self.fl),numpy.log10(self.fu),((numpy.log10(self.fu / self.fl))*self.fstep) + 1).T
                
                self.updatePlot()

                self.tabs.setCurrentIndex(1) #switch to output tab
            except:
                alert = QMessageBox()
                alert.setText('Simulation Failed. Please try a different configuration.')
                alert.exec_()

    
    def updatePlot(self):
        # create an axis
        ax1 = self.figure.add_subplot(211)
        ax2 = self.figure.add_subplot(212)
        
        if self.gs_radio1.isChecked():
            ax1.clear()                             # discards the old graph
            ax1.semilogx(self.f,self.Zmagi)         # plot data
            ax1.set_xlabel('Frequency')
            ax1.set_ylabel('Magnitude(dB)')
            ax2.clear()                             # discards the old graph
            ax2.semilogx(self.f,self.Zphai)         # plot data
            ax2.set_xlabel('Frequency')
            ax2.set_ylabel('Phase')
        elif self.gs_radio2.isChecked():
            ax1.clear()                             # discards the old graph
            ax1.semilogx(self.f,self.Zmag)          # plot data
            ax1.set_xlabel('Frequency')
            ax1.set_ylabel('Magnitude(dB)')
            ax2.clear()                             # discards the old graph
            ax2.semilogx(self.f,self.Zpha)          # plot data
            ax2.set_xlabel('Frequency')
            ax2.set_ylabel('Phase')
        elif self.gs_radio3.isChecked():
            ax1.clear()                             # discards the old graph
            ax1.semilogx(self.f,self.Zmagi,self.f,self.Zmag) # plot data
            ax1.set_xlabel('Frequency')
            ax1.set_ylabel('Magnitude(dB)')
            ax2.clear()                             # discards the old graph
            ax2.semilogx(self.f,self.Zphai,self.f,self.Zpha)# plot data
            ax2.set_xlabel('Frequency')
            ax2.set_ylabel('Phase')
        elif self.gs_radio4.isChecked():
            ax1.clear()                             # discards the old graph
            ax1.semilogx(self.f,self.magError)      # plot data
            ax1.set_xlabel('Frequency')
            ax1.set_ylabel('Magnitude(dB) \nNon Relative Error')
            ax2.clear()                             # discards the old graph
            ax2.semilogx(self.f,self.phaError)      # plot data
            ax2.set_xlabel('Frequency')
            ax2.set_ylabel('Phase \nRelative Error')
        ax1.grid()
        ax2.grid()        
        self.canvas.draw()                      # refresh canvas

if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyle('Fusion')
    clock = Window()
    clock.show()
    sys.exit(app.exec_())