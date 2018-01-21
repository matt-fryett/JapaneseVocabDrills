import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout,QVBoxLayout,QTabWidget, QComboBox,QSpacerItem, QSizePolicy, QLabel, QLineEdit, QPlainTextEdit
from PyQt5.QtGui import QIcon
from options import *
from db import *

class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.options = options()
        self.db = db(self.options)

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
        self.kanaHBox = QHBoxLayout()
        self.answerHBox = QHBoxLayout()
        self.interactionHBox = QHBoxLayout()

        self.homeTabVBox.addLayout(self.optionsHBox)
        self.homeTabVBox.addLayout(self.questionHBox)
        self.homeTabVBox.addLayout(self.kanaHBox)
        self.homeTabVBox.addLayout(self.answerHBox)
        self.homeTabVBox.addLayout(self.interactionHBox)

        self.questionGroupLabel = QLabel("Category")
        self.questionGroupCBox = QComboBox()
        self.questionGroupCBox.setMinimumSize(100, 1)
        self.questionGroupCBox.addItems(self.options.groups)

        self.questionSubGroupLabel = QLabel("Subgroup")
        self.questionSubGroupCBox = QComboBox()
        self.questionSubGroupCBox.setMinimumSize(200, 1)
        self.questionSubGroupCBox.addItems(self.options.subgroups["nouns"])

        self.questionLevelLabel = QLabel("JFBP Level")
        self.questionLevelCBox = QComboBox()
        self.questionLevelCBox.setMinimumSize(50, 1)
        self.questionLevelCBox.addItems(self.options.jfbpLevels)

        self.questionKanaLabel = QLabel("Kana")
        self.kanaCBox = QComboBox()
        self.kanaCBox.addItems(self.options.kana)

        self.startButton = QPushButton("Start")
        self.endButton = QPushButton("End")

        self.optionsHBox.addWidget(self.questionGroupLabel)
        self.optionsHBox.addWidget(self.questionGroupCBox)
        self.optionsHBox.addWidget(self.questionSubGroupLabel)
        self.optionsHBox.addWidget(self.questionSubGroupCBox)
        self.optionsHBox.addWidget(self.questionLevelLabel)
        self.optionsHBox.addWidget(self.questionLevelCBox)
        self.optionsHBox.addWidget(self.questionKanaLabel)
        self.optionsHBox.addWidget(self.kanaCBox)
        self.optionsHBox.addWidget(self.startButton)
        self.optionsHBox.addWidget(self.endButton)
        self.optionsHBox.addStretch(1)

        self.questionBox = QPlainTextEdit()
        self.font = self.questionBox.font()
        self.font.setPointSize(60)
        self.questionBox.setFont(self.font)
        self.questionBox.setSizePolicy(QSizePolicy.Minimum,QSizePolicy.Minimum)
        self.questionHBox.addWidget(self.questionBox)

        self.kanaBox = QPlainTextEdit()
        self.kanaBox.setFont(self.font)
        self.kanaBox.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        self.kanaHBox.addWidget(self.kanaBox)

        self.answerBox = QPlainTextEdit()
        self.answerBox.setFont(self.font)
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

        self.questionGroupCBox.currentTextChanged.connect(self.questionGroupBoxChanged)
        self.questionSubGroupCBox.currentTextChanged.connect(self.questionSubGroupBoxChanged)
        self.kanaCBox.currentIndexChanged.connect(self.kanaBoxChanged)
        self.startButton.clicked.connect(self.startButtonClicked)
        self.endButton.clicked.connect(self.endButtonClicked)
        self.correctButton.clicked.connect(self.correctButtonClicked)
        self.wrongButton.clicked.connect(self.wrongButtonClicked)
        self.hintButton.clicked.connect(self.hintButtonClicked)
        self.revealButton.clicked.connect(self.revealButtonClicked)

        self.questionGroupBoxChanged("<all>")
        self.endButton.setEnabled(False)
        self.hintButton.setEnabled(False)
        self.revealButton.setEnabled(False)
        self.correctButton.setEnabled(False)
        self.wrongButton.setEnabled(False)

        self.questionString = ""
        self.hintString = ""
        self.answerString = ""
        self.currentQuestionID = ""

        self.answerBox.setReadOnly(True)
        self.questionBox.setReadOnly(True)
        self.kanaBox.setReadOnly(True)

    def ask(self):
        self.currentQuestionID, self.questionString, self.hintString, self.answerString = self.db.getQuestion()
        print(self.currentQuestionID, self.questionString, self.hintString, self.answerString)
        self.questionBox.clear()
        self.kanaBox.clear()
        self.answerBox.clear()
        self.questionBox.insertPlainText(self.questionString)
        self.correctButton.setEnabled(False)
        self.wrongButton.setEnabled(False)

    def startButtonClicked(self):
        self.ask()
        self.startButton.setEnabled(False)
        self.endButton.setEnabled(True)
        self.hintButton.setEnabled(True)
        self.revealButton.setEnabled(True)

    def endButtonClicked(self):
        self.questionBox.clear()
        self.kanaBox.clear()
        self.answerBox.clear()
        self.startButton.setEnabled(True)
        self.endButton.setEnabled(False)
        self.hintButton.setEnabled(False)
        self.revealButton.setEnabled(False)
        self.correctButton.setEnabled(False)
        self.wrongButton.setEnabled(False)

    def correctButtonClicked(self):
        #Increment db
        self.ask()

    def wrongButtonClicked(self):
        #Decrement db
        self.ask()

    def hintButtonClicked(self):
        self.kanaBox.insertPlainText(self.hintString)

    def revealButtonClicked(self):
        self.kanaBox.clear()
        self.kanaBox.insertPlainText(self.hintString)
        self.answerBox.insertPlainText(self.answerString)
        self.correctButton.setEnabled(True)
        self.wrongButton.setEnabled(True)

    def kanaBoxChanged(self,id):
        self.options.isKanji=id

    def questionGroupBoxChanged(self,value):
        if value=="<all>":
            self.questionSubGroupCBox.clear()
            self.questionSubGroupCBox.addItems(["<all>"])
            self.questionSubGroupCBox.setEnabled(False)
        else:
            self.questionSubGroupCBox.clear()
            self.questionSubGroupCBox.addItems(self.options.subgroups[value])
            self.questionSubGroupCBox.setEnabled(True)

        self.options.group = self.questionGroupCBox.currentText()
        self.options.subGroup = self.questionSubGroupCBox.currentText()

    def questionSubGroupBoxChanged(self,value):
        self.options.group = self.questionGroupCBox.currentText()
        self.options.subGroup = self.questionSubGroupCBox.currentText()

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