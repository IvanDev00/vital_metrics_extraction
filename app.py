from flask import Flask, request, jsonify
from extract_data_from_image import extract_data_from_image
from flask_cors import CORS
import numpy as np
import cv2

app = Flask(__name__)
CORS(app)

@app.route('/v1/extract-metrics', methods=['POST'])
def extract():
    try:
        # Check if the post request has the file part
        if 'image' not in request.files:
            return jsonify({'error': 'No image file provided'}), 400
        image_file = request.files['image']

        # If the user does not select a file, the browser might submit an empty file without a filename.
        if image_file.filename == '':
            return jsonify({'error': 'No selected image'}), 400

        # Get the region choice from the form data
        region_choice = request.form.get('region_choice')

        # Convert the uploaded image file to OpenCV format
        # image = cv2.imdecode(np.fromstring(image_file.read(), np.uint8), cv2.IMREAD_UNCHANGED)
        image = cv2.imdecode(np.frombuffer(image_file.read(), np.uint8), cv2.IMREAD_UNCHANGED)

        # Extract data from the image
        raw_data, structured_data = extract_data_from_image(image, region_choice)

        # Return the results
        return jsonify({
            'raw_data': raw_data,
            'structured_data': structured_data
        }), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)
