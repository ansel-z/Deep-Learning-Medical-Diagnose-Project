import os
from keras.models import load_model
import cv2
import numpy as np

def test_image():
    model = load_model("skin_cancer.hdf5")
    test_example_path = "ISIC_0024854.jpg"
    img = cv2.imread(os.path.join(test_example_path)).astype(np.float32) / 255
    predicted_result = model.predict(np.array([img]))
    result = "benign" if predicted_result[0][0] < 0.5 else "malignant"
    print(f"Your skin lesion is {result}")
