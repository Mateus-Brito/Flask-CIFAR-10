from flask import Blueprint, render_template, redirect, url_for, request, jsonify, current_app
from keras.models import load_model
from keras.preprocessing.image import load_img
from keras.preprocessing.image import img_to_array
from keras import backend as K
from datetime import datetime

import sys 
import os 

cifar_browser = Blueprint('cifar_browser', __name__,template_folder='templates')

@cifar_browser.route('/')
def index():
    return render_template("index.html")

@cifar_browser.route('/cifarTest', methods=['GET', 'POST'])
def cifarTest():
    if request.method == 'POST':
        f = request.files.get('file')
        image_path = os.path.join(current_app.config['UPLOADED_PATH'], f.filename)
        file = f.save(image_path)

        img = load_image( image_path )
        model = load_model( os.path.join(current_app.config['models'], 'final_model.h5'))
        result = model.predict_classes(img)
        K.clear_session()

    return jsonify({
        'filename': f.filename,
        'date': datetime.today().strftime('%Y-%m-%d-%H:%M:%S'),
        'classname': int(result[0]),
    }), 200

# load and prepare the image
def load_image(filename):
	# load the image
	img = load_img(filename, target_size=(32, 32))
	# convert to array
	img = img_to_array(img)
	# reshape into a single sample with 3 channels
	img = img.reshape(1, 32, 32, 3)
	# prepare pixel data
	img = img.astype('float32')
	img = img / 255.0
	return img