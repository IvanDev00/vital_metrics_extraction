import easyocr
from preprocess_image import upscale_image
from regions import watch_regions, bmi_regions, ring_regions, broken_ring_regions
from structured_data import  bmi_data, ring_data, watch_data
from is_vertically_aligned import is_vertically_aligned
from correct_ocr_results import correct_ocr_results
import cv2

# Initialize the reader once
reader = easyocr.Reader(['en'], gpu=True)

def extract_data_from_image(image, region_choice, broken_file_type=""):
    print("broken_file_type: ",broken_file_type)
    # image = cv2.imread(images)
    # print(f"Processing for region_choice: {region_choice}")

    if region_choice == "dashboard":
        regions = watch_regions
    elif region_choice == "bmi":
        regions = bmi_regions
    elif region_choice == "ring":
        regions = broken_ring_regions if broken_file_type == "o2Ring" else ring_regions
    else:
        raise ValueError("Invalid record choice. Please choose either 'dashboard' for Dashboard Summary Record or 'bmi' for BMI Record.")

    texts = []
    for i, region in enumerate(regions):
        # print(f"Processing region: {region}")
        x, y, w, h = region["x"], region["y"], region["width"], region["height"]
        cropped_image = image[y:y+h, x:x+w]

        if region_choice in ("dashboard"):  
        # Skip enhancement for first 2 regions 
            ocr_input = upscale_image(cropped_image) 
        else:
            ocr_input = cropped_image  
            # Apply enhancement 
        try:
            extracted = reader.readtext(ocr_input)
            # print(f"Extracted text: {extracted}")
        except Exception as e:
            print(f"Error during OCR processing: {e}")
        
        # If the region is empty, add an empty string to the results
        if not extracted:
            texts.append("")
        elif(region_choice == "bmi"):
            if not extracted:
                texts.append("")
                # print(f"Processing extracted text for region: {region}")
            # Sort extracted text by their vertical position
            else:
                extracted = sorted(extracted, key=lambda entry: entry[0][0][1])

                combined_texts = []
                prev_text = extracted[0][1]
                prev_box = extracted[0][0]

                for current in extracted[1:]:
                    current_text = current[1]
                    current_box = current[0]

                    if is_vertically_aligned(prev_box, current_box):
                        print(f"Vertically aligned: {prev_text} and {current_text}")
                        prev_text += " " + current_text  # Concatenate vertically aligned texts
                    else:
                        combined_texts.append(correct_ocr_results(prev_text))
                        prev_text = current_text

                    prev_box = current_box

                combined_texts.append(correct_ocr_results(prev_text))
                texts.extend(combined_texts)
        else:
            data = [item[1] for item in extracted]
            for item in data:
                texts.append(correct_ocr_results(item))

        # Save the cropped image
        # cv2.imwrite(f"o2/cropped_image_{i}.png", cropped_image)

    print(f"Extracted texts: {texts}")
    if region_choice == "dashboard":
        structured_data = watch_data(texts)
        # print(f"Structured data: {structured_data}")
    elif region_choice == "bmi":
        structured_data = bmi_data(texts)
        # print(f"Structured data: {structured_data}")
    elif region_choice == "ring":
        structured_data = ring_data(texts)
        # print(f"Structured data: {structured_data}")

    return texts, structured_data

# extract_data_from_image("dataset/1.jpg", "dashboard")
# extract_data_from_image("dataset/bmi.png", "bmi")
# extract_data_from_image("22880.jpg", "dashboard")
# extract_data_from_image("images/output_image3.png", "ring")