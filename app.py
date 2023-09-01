from flask import Flask, request, jsonify
from extract_data_from_image import extract_data_from_image
from flask_cors import CORS
import numpy as np
import cv2
from pdf_to_image import pdf_to_image

app = Flask(__name__)
CORS(app, resources={r"/v1/*": {"origins": ["*"]}})

@app.route('/v1/extract-metrics', methods=['POST'])
def extract():
    try:
        # Check if the post request has the file part
        if 'record_file' not in request.files:
            return jsonify({'error': 'No file provided'}), 400
        uploaded_file = request.files['record_file']

        # If the user does not select a file, the browser might submit an empty file without a filename.
        if uploaded_file.filename == '':
            return jsonify({'error': 'No selected file'}), 400

        # Get the region choice from the form data
        region_choice = request.form.get('region_choice')
        file_type = request.form.get('file_type')

        # Convert the uploaded image file to OpenCV format
        # image = cv2.imdecode(np.fromstring(image_file.read(), np.uint8), cv2.IMREAD_UNCHANGED)
        if file_type == 'pdf':
            print("Converting PDF to Image...")
            image = pdf_to_image(uploaded_file)
            print("PDF converted successfully!")
        else:
            image = cv2.imdecode(np.frombuffer(uploaded_file.read(), np.uint8), cv2.IMREAD_UNCHANGED)
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
    app.run(host='0.0.0.0', port=5000)
