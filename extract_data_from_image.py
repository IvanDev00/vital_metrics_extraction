import cv2
import easyocr
from preprocess_image import preprocess_image
from regions import dashboard_regions, bmi_regions
from structured_data import dashboard_data, bmi_data
from is_vertically_aligned import is_vertically_aligned
from correct_ocr_results import correct_ocr_results

# Initialize the reader once
reader = easyocr.Reader(['en'], gpu=True)

def extract_data_from_image(image, region_choice):
    # image = cv2.imread(image_path)

    if region_choice == "dashboard":
        regions = dashboard_regions
    elif region_choice == "bmi":
        regions = bmi_regions
    else:
        raise ValueError("Invalid record choice. Please choose either 'dashboard' for Dashboard Summary Record or 'bmi' for BMI Record.")

    texts = []
    for region in regions:
        x, y, w, h = region["x"], region["y"], region["width"], region["height"]
        cropped_image = image[y:y+h, x:x+w]

        if region_choice == "dashboard":
            # processed_image = preprocess_image(cropped_image)
            extracted = reader.readtext(cropped_image)
        else:
            extracted = reader.readtext(cropped_image)
    
        # If the region is empty, add an empty string to the results
        if not extracted:
            texts.append("")
        else:
            # Sort extracted text by their vertical position
            extracted = sorted(extracted, key=lambda entry: entry[0][0][1])

            combined_texts = []
            prev_text = extracted[0][1]
            prev_box = extracted[0][0]

            for current in extracted[1:]:
                current_text = current[1]
                current_box = current[0]

                if is_vertically_aligned(prev_box, current_box):
                    prev_text += " " + current_text  # Concatenate vertically aligned texts
                else:
                    combined_texts.append(correct_ocr_results(prev_text))
                    prev_text = current_text

                prev_box = current_box

            combined_texts.append(correct_ocr_results(prev_text))
            texts.extend(combined_texts)

    if region_choice == "dashboard":
        structured_data = dashboard_data(texts)
    else:
        structured_data = bmi_data(texts)

    return texts, structured_data

# print(extract_data_from_image("22880.jpg", "dashboard"))