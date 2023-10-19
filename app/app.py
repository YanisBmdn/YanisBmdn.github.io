import os
from flask import Flask, render_template

app = Flask(__name__)

APP_DIRECTORY = "app"

@app.route('/')
def index():
    base_folder = os.path.join(APP_DIRECTORY, "static", "scans")
    folders = next(os.walk(base_folder))[1]
    print(folders)
    return render_template('index.html', folders=folders)

@app.route('/scans/<string:folder>/')
def show_images(folder):
    image_folder = os.path.join(APP_DIRECTORY, "static", "scans", folder)
    images=os.listdir(image_folder)
    return render_template('scan.html', folder=folder, images=images)

if __name__ == '__main__':
    app.run(debug=True)
