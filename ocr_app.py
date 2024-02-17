from flask import Flask, render_template, request, redirect, url_for
from PIL import Image
import pytesseract
app = Flask(__name__, static_url_path='/static')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def upload_image():
    if 'file' not in request.files:
        return redirect(request.url)

    file = request.files['file']

    if file.filename == '':
        return redirect(request.url)

    if file:
        image_path = 'static/uploads/' + file.filename
        file.save(image_path)
        extracted_text = perform_ocr(image_path)  
        return render_template('index.html', extracted_text=extracted_text, image_path=image_path)
def perform_ocr(image_path):
    image = Image.open(image_path)
    extracted_text = pytesseract.image_to_string(image)
    return extracted_text

if __name__ == "__main__":
    app.run(debug = True)