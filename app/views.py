from flask import render_template, request, redirect, url_for
import os
from PIL import Image
from app.utils import pipeline_model


UPLOAD_FOLDER = 'static/uploads'

def base():
    return render_template('base.html')


def index():
    return render_template('index.html')


def get_width(path):
    img = Image.open(path)
    size = img.size
    aspect_ratio = size[0] / size[1]
    width = 400 * aspect_ratio
    return int(width)


def gender():
    if request.method == 'POST':
        f = request.files['image']
        filename = f.filename
        path = os.path.join(UPLOAD_FOLDER, filename)
        f.save(path)
        image_width = get_width(path)
        # prediction
        pipeline_model(path, filename, color = 'bgr')
        return render_template('gender.html', fileupload = True, img_name = filename, image_width=image_width)
    return render_template('gender.html', fileupload = False, img_name = "Gender", image_width = "400")
