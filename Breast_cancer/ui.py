from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap




# GUI:
app = QApplication([])
text_area = QPlainTextEdit()
text_area.setFocusPolicy(Qt.NoFocus)
uploadbutton = QPushButton("upload file")
message = QLineEdit()
label = QLabel()


layout = QVBoxLayout()
layout.addWidget(uploadbutton)
layout.addWidget(text_area)
layout.addWidget(message)
layout.addWidget(label)

window = QWidget()
window.setGeometry(500,500,600,600)
window.setLayout(layout)
window.show()


def messageHandler(msg):
    return msg+"\n"+"AI:hahahaa SB!"


def imageHandler(img):
    pass


# Event handlers:
def send_message():
    info = message.text()
    msg = messageHandler(info)
    text_area.appendPlainText(msg)
    message.setText("")


def uploadfilefunc():
    fdiag = QFileDialog()
    fdiag.setFileMode(QFileDialog.AnyFile)
    if fdiag.exec_():
        filenames = fdiag.selectedFiles()
        print("File opened: ", filenames[0])
        f = open(filenames[0], 'r')
        # show imag
        img_show = QPixmap(filenames[0])
        # TODO: resize image
        label.setPixmap(img_show)
        # imageHandler(img)

    
# Signals:
message.returnPressed.connect(send_message)
uploadbutton.clicked.connect(uploadfilefunc)
app.exec_()


