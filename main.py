import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout,QVBoxLayout,QTabWidget, QComboBox,QSpacerItem, QSizePolicy, QLabel, QLineEdit
from PyQt5.QtGui import QIcon
from options import *


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.options = options()

        self.initUI()
        self.setGeometry(600, 300, 1024, 768)
        self.setWindowTitle('Japanese')
        self.setWindowIcon(QIcon('icon.png'))

        self.mainLayout = QVBoxLayout(self)
        self.tabs = QTabWidget()
        self.homeTab = QWidget()
        self.statsTab = QWidget()
        self.tabs.addTab(self.homeTab, "Home")
        self.tabs.addTab(self.statsTab, "Stats")
        self.mainLayout.addWidget(self.tabs)
        self.setLayout(self.mainLayout)

        self.homeTabVBox = QVBoxLayout()
        self.homeTab.setLayout(self.homeTabVBox)

        self.optionsHBox = QHBoxLayout()

        self.questionHBox = QHBoxLayout()
        self.answerHBox = QHBoxLayout()
        self.interactionHBox = QHBoxLayout()

        self.homeTabVBox.addLayout(self.optionsHBox)
        self.homeTabVBox.addLayout(self.questionHBox)
        self.homeTabVBox.addLayout(self.answerHBox)
        self.homeTabVBox.addLayout(self.interactionHBox)

        self.questionTypeLabel = QLabel("Category")
        self.questionTypeCBox = QComboBox()
        self.questionTypeCBox.addItems(self.options.categories)
        self.questionLevelLabel = QLabel("JFBP Level")
        self.questionLevelCBox = QComboBox()
        self.questionLevelCBox.addItems(self.options.jfbpLevels)
        self.questionKanaLabel = QLabel("Kana")
        self.kanaCBox = QComboBox()

        self.optionsHBox.addWidget(self.questionTypeLabel)
        self.optionsHBox.addWidget(self.questionTypeCBox)
        self.optionsHBox.addStretch(1)
        self.optionsHBox.addWidget(self.questionLevelLabel)
        self.optionsHBox.addWidget(self.questionLevelCBox)
        self.optionsHBox.addStretch(1)
        self.optionsHBox.addWidget(self.questionKanaLabel)
        self.optionsHBox.addWidget(self.kanaCBox)

        self.questionBox = QLineEdit()
        #self.questionBox.setFont()
        self.questionBox.setSizePolicy(QSizePolicy.Minimum,QSizePolicy.Minimum)
        self.questionHBox.addWidget(self.questionBox)

        self.answerBox = QLineEdit()
        self.answerBox.setSizePolicy(QSizePolicy.Minimum,QSizePolicy.Minimum)
        self.answerHBox.addWidget(self.answerBox)

        self.hintButton = QPushButton("Hint")
        self.revealButton = QPushButton("Reveal")
        self.correctButton = QPushButton("Correct")
        self.wrongButton = QPushButton("Incorrect")

        self.interactionHBox.addWidget(self.hintButton)
        self.interactionHBox.addWidget(self.revealButton)
        self.interactionHBox.addWidget(self.correctButton)
        self.interactionHBox.addWidget(self.wrongButton)


    def initUI(self):
        None



        # okButton = QPushButton("OK")
        # cancelButton = QPushButton("Cancel")
        #
        # hbox = QHBoxLayout()
        # hbox.addStretch(1)
        # hbox.addWidget(okButton)
        # hbox.addWidget(cancelButton)
        #
        # vbox = QVBoxLayout()
        # vbox.addStretch(1)
        # vbox.addLayout(hbox)
        #
        # self.setLayout(vbox)

        self.show()

app = QApplication(sys.argv)
ex = Example()
sys.exit(app.exec_())