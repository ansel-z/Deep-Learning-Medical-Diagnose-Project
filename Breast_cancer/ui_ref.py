from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap
import tensorflow as tf
from PIL import Image
import numpy as np
import cv2


model_list = []
option_list = ["Breast Cancer", "Skin Cancer"]



# GUI:
app = QApplication([])
result_area = QPlainTextEdit()
result_area.setFocusPolicy(Qt.NoFocus)
text_area = QPlainTextEdit()
text_area.setFocusPolicy(Qt.NoFocus)
uploadbutton = QPushButton("upload file")
message = QLineEdit()
label = QLabel()
combox = QComboBox()

# set up models and options
combox.addItems(option_list)
#load model here and store results in model_list


chatlayout = QVBoxLayout()
chatlayout.addWidget(text_area)
chatlayout.addWidget(message)

uploadlayout = QVBoxLayout()
uploadlayout.addWidget(label)
uploadlayout.addStretch(5)
uploadlayout.addWidget(uploadbutton)


resultlayout = QVBoxLayout()
resultlayout.addWidget(result_area)
resultlayout.addWidget(combox)


hbox = QHBoxLayout()
hbox.addLayout(chatlayout)
hbox.addLayout(uploadlayout)
hbox.addLayout(resultlayout)

window = QWidget()
window.setGeometry(500,500,1000,600)
window.setLayout(hbox)
window.show()


def LoadModel(path):
    model = tf.keras.models.load_model(path)
    return model


def messageHandler(msg):
    return msg+"\n"+"Hi, what can I do for you?"


def imageHandler(img, ):
    model = LoadModel("Breast_cancer_model")
    print("model loaded")
    model.summary()
    pred = model(img)
    pred = np.array(pred)
    pred_res = int(pred[0][0])
    res_str = ""
    if pred_res == 1:
        res_str = "You have breast cancer!"
    else:
        res_str = "You are healthy!"
    result_area.appendPlainText(res_str)
    


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
        # show imag
        #img_show = QPixmap(filenames[0])
        # TODO: resize image
        #label.setPixmap(img_show)
        img = cv2.imread(filenames[0], 1)
        img = cv2.resize(img, (48, 48))
        img = np.array(img)
#        img = np.transpose(img, (2, 0, 1))
        img = np.reshape(img, (1, 48, 48, 3))
        imageHandler(img)
        
    
# Signals:
message.returnPressed.connect(send_message)
uploadbutton.clicked.connect(uploadfilefunc)
app.exec_()


