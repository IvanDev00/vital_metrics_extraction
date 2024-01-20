from flask import Flask, request, jsonify
from extract_data_from_image import extract_data_from_image
from flask_cors import CORS
import numpy as np
import cv2
from pdf_to_image import pdf_to_image
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)
CORS(app, resources={r"/v1/*": {"origins": ["*"]}})

@app.route('/v1/extract-metrics', methods=['POST'])
def extract():
    try:
        if 'record_file' not in request.files:
            return jsonify({'error': 'No file provided'}), 400

        uploaded_file = request.files['record_file']
        # print(uploaded_file)
        if uploaded_file.filename == '':
            return jsonify({'error': 'No selected file'}), 400

        region_choice = request.form.get('region_choice')
        broken_file_type = request.form.get('broken_file_type')
        file_type = request.form.get('file_type')

        if file_type == 'pdf':
            logger.info("Converting PDF to Image...")
            image = pdf_to_image(uploaded_file)
            logger.info("PDF converted successfully!")
        else:
            image = cv2.imdecode(np.frombuffer(uploaded_file.read(), np.uint8), cv2.IMREAD_UNCHANGED)

        raw_data, structured_data = extract_data_from_image(image, region_choice, broken_file_type)

        return jsonify({
            'raw_data': raw_data,
            'structured_data': structured_data
        }), 200

    except Exception as e:
        logger.error(f"An error occurred: {e}")
        return jsonify({'error': 'An error occurred'}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)