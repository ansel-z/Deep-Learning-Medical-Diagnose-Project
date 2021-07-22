from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap
import tensorflow as tf
from PIL import Image
import numpy as np
import cv2
from NLP_application import *


# GUI:
app = QApplication([])
result_area = QPlainTextEdit()
result_area.setFocusPolicy(Qt.NoFocus)
text_area = QPlainTextEdit()
text_area.setFocusPolicy(Qt.NoFocus)
uploadbutton = QPushButton("upload file")
message = QLineEdit()
label = QLabel()
showlabel = QLabel()
combox = QComboBox()
combox.addItem("Breast Cancer")
combox.addItem("Skin Cancer")

chatlayout = QVBoxLayout()
chatlayout.addWidget(text_area)
chatlayout.addWidget(message)

uploadlayout = QVBoxLayout()
uploadlayout.addWidget(label)
uploadlayout.addStretch(5)
uploadlayout.addWidget(uploadbutton)


resultlayout = QVBoxLayout()
resultlayout.addWidget(result_area, 1)
resultlayout.addWidget(showlabel, 2)
resultlayout.addWidget(combox)


hbox = QHBoxLayout()
hbox.addLayout(chatlayout)
hbox.addLayout(uploadlayout)
hbox.addLayout(resultlayout)


window = QWidget()
window.setWindowTitle("Cancer Detector")
window.setGeometry(500,500,1000,600)
window.setLayout(hbox)
window.show()


def LoadModel(path):
    model = tf.keras.models.load_model(path)
    return model


def messageHandler(msg):
    list = get_keywords(msg)
    res_str = ""
    res_str += msg
    res_str += "\n" + "Keywords detected are: "
    for keyword in list:
        res_str += keyword + ", "
    return res_str[:-2]


def imageHandler(img, cur_idx):
    # models
    model_list = []
    model_list.append(tf.keras.models.load_model("Breast_cancer_model"))
    model_list.append(tf.keras.models.load_model("skin_cancer.hdf5"))
    cancer_type = ["breast cancer", "skin cancer"]
    acc = ["84", "80"]
    model = model_list[cur_idx]
    if cur_idx == 0:
        img = cv2.resize(img, (48, 48))
        img = np.array(img)
        img = np.reshape(img, (1, 48, 48, 3))
    else:
        img = img.astype(np.float32) / 255
        img = np.array([img])
    pred = model(img)
    pred = np.array(pred)
    pred_res = int(pred[0][0])
    res_str = ""
    if pred_res > 0.5:
        res_str = "You may have " + cancer_type[cur_idx] + "!"
    else:
        res_str = "You are healthy!"
    res_str += " \nOur prediction is of " + acc[cur_idx] + " percent accuracy."
    result_area.appendPlainText(res_str)
    


# Event handlers:
def send_message():
    info = message.text()
    msg = messageHandler(info)
    text_area.appendPlainText(msg)
    message.setText("")


def uploadfilefunc():
    cur_idx = combox.currentIndex()
    fdiag = QFileDialog()
    fdiag.setFileMode(QFileDialog.AnyFile)
    if fdiag.exec_():
        filenames = fdiag.selectedFiles()
        print("File opened: ", filenames[0])
        # show imag
        img_show = QPixmap(filenames[0])
        # TODO: resize image
        showlabel.setPixmap(img_show)
        showlabel.setScaledContents(True)
        img = cv2.imread(filenames[0], 1)
        imageHandler(img, cur_idx)
        
    
# Signals:
message.returnPressed.connect(send_message)
uploadbutton.clicked.connect(uploadfilefunc)
app.exec_()


