from pdf2image import convert_from_bytes
import cv2
import numpy as np

def pdf_to_image(pdf_file):
    # Convert the first page of the PDF to an image
    images = convert_from_bytes(pdf_file.read(), dpi=96,first_page=1, last_page=1)
    # Convert the PIL Image to an OpenCV format
    image_np = np.array(images[0])
    image_cv = cv2.cvtColor(image_np, cv2.COLOR_RGB2BGR)
    
    # Save the image to the output path
    # output_path = "./images/output_image2.png"  # Change this to your desired path and filename
    # cv2.imwrite(output_path, image_cv)
    # print(f"Image saved to {output_path}")
    
    return image_cv
