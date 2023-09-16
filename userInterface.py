import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QPushButton,
                             QHBoxLayout, QVBoxLayout, QWidget, QTextEdit, QLabel)

currentLineIndex = 0
ladderDiagram = "-------------------------------------------------------------------------------------------------------------------------------------()-----"
nextLine = "--------------------------------------------------------------------------------------------------------------------------------------------"
ladderDiagramList = [
    ladderDiagram,
    nextLine
]
currIdx = 6
output_statement = 'output'

arrayGatesMain = []
arrayGatesParallel = []

class LadderProgrammingConsole(QMainWindow):
    def __init__(self):
        super().__init__()

        # Main window properties
        self.setWindowTitle('PLC Ladder Programming Console')
        self.setGeometry(100, 100, 800, 400)  # Adjusted the size

        # Main layout
        main_layout = QVBoxLayout()

        # Horizontal layout for buttons
        btn_layout = QHBoxLayout()

        # Create buttons

        self.on_btn = QPushButton('ON', self)
        self.off_btn = QPushButton('OFF', self)
        self.parallel_on_btn = QPushButton('Parallel On', self)
        self.parallel_off_btn = QPushButton('Parallel Off', self)
        self.run_btn = QPushButton('Run', self)


        # Add buttons to horizontal layout
        btn_layout.addWidget(self.on_btn)
        btn_layout.addWidget(self.off_btn)
        btn_layout.addWidget(self.parallel_on_btn)
        btn_layout.addWidget(self.parallel_off_btn)
        btn_layout.addWidget(self.run_btn)


        # Add the horizontal button layout to the main layout
        main_layout.addLayout(btn_layout)

        # Add the display area
        self.text_display = QTextEdit(self)
        self.text_display.setText("\n".join(ladderDiagramList))
        main_layout.addWidget(self.text_display)

        # Add a small output section at the bottom
        self.output_label = QLabel("Out displayed here", self)
        main_layout.addWidget(self.output_label)

        central_widget = QWidget(self)
        central_widget.setLayout(main_layout)
        self.setCentralWidget(central_widget)

        # Connect buttons to respective functionalities (to be implemented)
        self.on_btn.clicked.connect(self.on_btn_function)
        self.off_btn.clicked.connect(self.off_btn_function)
        self.parallel_off_btn.clicked.connect(self.parallel_off_btn_function)
        self.parallel_on_btn.clicked.connect(self.parallel_on_btn_function)
        self.run_btn.clicked.connect(self.run_btn_function)
        # ... Do the same for other buttons

    # Implement the functionalities for the buttons
    def on_btn_function(self):
        global ladderDiagramList, currIdx
        # Your logic here
        print(currIdx)
        currentLine = ladderDiagramList[0]  # First line
        currentLine = currentLine[:currIdx - 1] + '[' + ' ' + ']' + currentLine[currIdx + 2:]
        ladderDiagramList[0] = currentLine
        self.text_display.setText("\n".join(ladderDiagramList))
        arrayGatesMain.append([True, currIdx])
        currIdx = currIdx + 8

    def off_btn_function(self):
        global ladderDiagramList, currIdx
        # Your logic here
        print(currIdx)
        currentLine = ladderDiagramList[0]  # First line
        currentLine = currentLine[:currIdx - 1] + '[' + '/' + ']' + currentLine[currIdx + 2:]
        ladderDiagramList[0] = currentLine
        self.text_display.setText("\n".join(ladderDiagramList))
        arrayGatesMain.append([False, currIdx])
        currIdx = currIdx + 8  # Assuming you still want the cursor index to move after pressing the off button

    def parallel_off_btn_function(self):
        global currIdx, ladderDiagramList
        print(currIdx)
        currentLine = ladderDiagramList[1]  # First line
        currentLine = currentLine[:currIdx - 1] + '[' + '/' + ']' + currentLine[currIdx + 2:]
        ladderDiagramList[1] = currentLine
        self.text_display.setText("\n".join(ladderDiagramList))
        arrayGatesParallel.append([False, currIdx])

    def parallel_on_btn_function(self):
        global currIdx, ladderDiagramList
        print(currIdx)
        currentLine = ladderDiagramList[1]  # First line
        currentLine = currentLine[:currIdx - 1] + '[' + ' ' + ']' + currentLine[currIdx + 2:]
        ladderDiagramList[1] = currentLine
        self.text_display.setText("\n".join(ladderDiagramList))
        arrayGatesParallel.append([True, currIdx])

    def run_btn_function(self):
        self.output_label.setText("Run pressed!")
        print(arrayGatesMain)
        print(arrayGatesParallel)
        for i in range(len(arrayGatesParallel)):
            for idx in range(len(arrayGatesMain)):
                if (arrayGatesParallel[i][1] == arrayGatesMain[idx][1]) and (arrayGatesParallel[i][0] == True):
                    arrayGatesMain[idx][0] = True
        print(arrayGatesMain)

        result = True
        for i in range(len(arrayGatesMain)):
            if arrayGatesMain[i][0] == False:
                result = False

        result_text = str(result)
        self.output_label.setText(result_text)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = LadderProgrammingConsole()
    window.show()
    sys.exit(app.exec_())
