import os
from datetime import datetime

from flask import Blueprint, current_app, jsonify, render_template, request

from .utils import predict_class

cifar_browser = Blueprint("cifar_browser", __name__, template_folder="templates")


@cifar_browser.route("/")
def index():
    return render_template("index.html")


@cifar_browser.route("/cifar-test", methods=["POST"])
def cifar_test():
    uploaded_file = request.files.get("file")
    if uploaded_file.filename == "":
        return "No file selected for uploading", 400

    new_path_image = os.path.join(
        current_app.config["UPLOADED_PATH"], uploaded_file.filename
    )
    uploaded_file.save(new_path_image)
    classes_x = predict_class(new_path_image)
    if len(classes_x) == 0:
        return "Could not identify the image.", 400

    return jsonify(
        {
            "filename": uploaded_file.filename,
            "date": datetime.today().strftime("%Y-%m-%d-%H:%M:%S"),
            "classname": int(classes_x[0]),
        }
    )
