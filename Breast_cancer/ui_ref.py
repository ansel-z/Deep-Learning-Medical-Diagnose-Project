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
result_area1 = QPlainTextEdit()
result_area1.setFocusPolicy(Qt.NoFocus)
uploadbutton1 = QPushButton("upload file")
showlabel1 = QLabel()
combox1 = QComboBox()
combox1.addItem("Breast Cancer")
combox1.addItem("Skin Cancer")

result_area2 = QPlainTextEdit()
result_area2.setFocusPolicy(Qt.NoFocus)
uploadbutton2 = QPushButton("upload file")
showlabel2 = QLabel()
combox2 = QComboBox()
combox2.addItem("Breast Cancer")
combox2.addItem("Skin Cancer")

result_area3 = QPlainTextEdit()
result_area3.setFocusPolicy(Qt.NoFocus)
uploadbutton3 = QPushButton("upload file")
showlabel3 = QLabel()
combox3 = QComboBox()
combox3.addItem("Breast Cancer")
combox3.addItem("Skin Cancer")

# text labels
label1 = QLabel("Diagnosis Result")
label2 = QLabel("Uploaded Image")
label3 = QLabel("Select Cancer Type")

height = 150
weight = 150
showlabel1.setMinimumSize(weight, height)
showlabel1.setMaximumSize(weight, height)
showlabel2.setMinimumSize(weight, height)
showlabel2.setMaximumSize(weight, height)
showlabel3.setMinimumSize(weight, height)
showlabel3.setMaximumSize(weight, height)


resultlayout1 = QVBoxLayout()
resultlayout1.addWidget(label1)
resultlayout1.addWidget(result_area1, 1)
resultlayout1.addWidget(label2)
resultlayout1.addWidget(showlabel1, 2)
resultlayout1.addWidget(uploadbutton1)
resultlayout1.addWidget(label3)
resultlayout1.addWidget(combox1)

resultlayout2 = QVBoxLayout()
resultlayout2.addWidget(label1)
resultlayout2.addWidget(result_area2, 1)
resultlayout2.addWidget(label2)
resultlayout2.addWidget(showlabel2, 2)
resultlayout2.addWidget(uploadbutton2)
resultlayout2.addWidget(label3)
resultlayout2.addWidget(combox2)

resultlayout3 = QVBoxLayout()
resultlayout3.addWidget(label1)
resultlayout3.addWidget(result_area3, 1)
resultlayout3.addWidget(label2)
resultlayout3.addWidget(showlabel3, 2)
resultlayout3.addWidget(uploadbutton3)
resultlayout3.addWidget(label3)
resultlayout3.addWidget(combox3)



hbox = QHBoxLayout()
hbox.addLayout(resultlayout1)
hbox.addLayout(resultlayout2)
hbox.addLayout(resultlayout3)


window = QWidget()
window.setWindowTitle("Cancer Detector")
window.setGeometry(500,500,1200,600)
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


def imageHandler1(img, cur_idx):
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
    print(pred)
    pred = np.array(pred)
    pred_res = float(pred[0][0])
    res_str = ""
    res_str += "The score given by our model is " + str(pred_res) + "\n"
    if pred_res > 0.5:
        res_str += "You may have " + cancer_type[cur_idx] + "!"
    else:
        res_str += "You are healthy!"
    res_str += " \nOur prediction is of " + acc[cur_idx] + " percent accuracy."
    result_area1.appendPlainText(res_str)
    

def imageHandler2(img, cur_idx):
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
    pred_res = float(pred[0][0])
    res_str = ""
    res_str += "The score given by our model is " + str(pred_res) + "\n"
    if pred_res > 0.5:
        res_str += "You may have " + cancer_type[cur_idx] + "!"
    else:
        res_str += "You are healthy!"
    res_str += " \nOur prediction is of " + acc[cur_idx] + " percent accuracy."
    result_area2.appendPlainText(res_str)


def imageHandler3(img, cur_idx):
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
    pred_res = float(pred[0][0])
    res_str = ""
    res_str += "The score given by our model is " + str(pred_res) + "\n"
    if pred_res > 0.5:
        res_str += "You may have " + cancer_type[cur_idx] + "!"
    else:
        res_str += "You are healthy!"
    res_str += " \nOur prediction is of " + acc[cur_idx] + " percent accuracy."
    result_area3.appendPlainText(res_str)


def uploadfilefunc1():
    cur_idx = combox1.currentIndex()
    fdiag = QFileDialog()
    fdiag.setFileMode(QFileDialog.AnyFile)
    if fdiag.exec_():
        filenames = fdiag.selectedFiles()
        print("File opened: ", filenames[0])
        # show imag
        img_show = QPixmap(filenames[0])
        # TODO: resize image
        showlabel1.setPixmap(img_show)
        showlabel1.setScaledContents(True)
        img = cv2.imread(filenames[0], 1)
        imageHandler1(img, cur_idx)
        

def uploadfilefunc2():
    cur_idx = combox2.currentIndex()
    fdiag = QFileDialog()
    fdiag.setFileMode(QFileDialog.AnyFile)
    if fdiag.exec_():
        filenames = fdiag.selectedFiles()
        print("File opened: ", filenames[0])
        # show imag
        img_show = QPixmap(filenames[0])
        # TODO: resize image
        showlabel2.setPixmap(img_show)
        showlabel2.setScaledContents(True)
        img = cv2.imread(filenames[0], 1)
        imageHandler2(img, cur_idx)


def uploadfilefunc3():
    cur_idx = combox3.currentIndex()
    fdiag = QFileDialog()
    fdiag.setFileMode(QFileDialog.AnyFile)
    if fdiag.exec_():
        filenames = fdiag.selectedFiles()
        print("File opened: ", filenames[0])
        # show imag
        img_show = QPixmap(filenames[0])
        # TODO: resize image
        showlabel3.setPixmap(img_show)
        showlabel3.setScaledContents(True)
        img = cv2.imread(filenames[0], 1)
        imageHandler3(img, cur_idx)

    
# Signals:
# message.returnPressed.connect(send_message)
uploadbutton1.clicked.connect(uploadfilefunc1)
uploadbutton2.clicked.connect(uploadfilefunc2)
uploadbutton3.clicked.connect(uploadfilefunc3)
app.exec_()


