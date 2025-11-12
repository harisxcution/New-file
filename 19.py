from flask import Flask, request, jsonify, send_file
from flask_cors import CORS
import cv2
import numpy as np
import tempfile
import os

app = Flask(__name__)
CORS(app)  # allows frontend requests

@app.route('/sketch', methods=['POST'])
def sketch():
    if 'image' not in request.files:
        return jsonify({'error': 'No image uploaded'}), 400

    file = request.files['image']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    # Convert image to grayscale and apply sketch effect
    np_img = np.frombuffer(file.read(), np.uint8)
    img = cv2.imdecode(np_img, cv2.IMREAD_COLOR)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    inv = 255 - gray
    blur = cv2.GaussianBlur(inv, (21, 21), 0)
    inv_blur = 255 - blur
    sketch = cv2.divide(gray, inv_blur, scale=256.0)

    # Save temp file and return
    temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".png")
    cv2.imwrite(temp_file.name, sketch)
    temp_file.close()

    return send_file(temp_file.name, mimetype='image/png')

if __name__ == '__main__':
    app.run(debug=True)
