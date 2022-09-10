import os

import numpy as np
from flask import current_app
from keras import backend as K
from keras.models import load_model
from tensorflow.keras.utils import img_to_array, load_img


def predict_class(image_path):
    img = load_image(image_path)
    model = load_model(os.path.join(current_app.config["models"], "final_model.h5"))
    predict_x = model.predict(img)
    classes_x = np.argmax(predict_x, axis=1)
    K.clear_session()
    return classes_x


def load_image(filename):
    # load the image
    img = load_img(filename, target_size=(32, 32))
    # convert to array
    img = img_to_array(img)
    # reshape into a single sample with 3 channels
    img = img.reshape(1, 32, 32, 3)
    # prepare pixel data
    img = img.astype("float32")
    img = img / 255.0
    return img
