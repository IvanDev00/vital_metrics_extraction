import cv2
import numpy as np

def upscale_image(cropped_image, scale_percent = 1.25):
     # Scale dimensions    
    width = int(cropped_image.shape[1] * scale_percent)
    height = int(cropped_image.shape[0] * scale_percent)
    dim = (width, height)
    
    # Perform resize/upscale using linear interpolation
    resized = cv2.resize(cropped_image, dim, interpolation = cv2.INTER_LINEAR)

    return resized


# def enhance_image(image):
#     upscaled_image = upscale_image(image)
#       # Grayscale and sharpen image
#     gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  

#      # Enhance contrast through histogram equalization
#     # enhanced = cv2.equalizeHist(upscaled_image)
    
#     # # Apply adaptive thresholding 
#     # thresh = cv2.adaptiveThreshold(enhanced, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, 
#     #                                cv2.THRESH_BINARY, 11, 2) 
    
#     return upscaled_image

# def enhance_image(cropped_img):
#     # OpenCV resize (scale by 150%) 
#     resized = upscale_image(cropped_img)
    
#    # Load the pre-trained EDSR model
#     model = cv2.dnn_superres.DnnSuperResImpl_create()
#     model.readModel('model/EDSR_x4.pb')
#     model.setModel("edsr", 4)

#        # Use the super resolution model to upscale the image
#     image = model.upsample(resized)
    
#     return image

# def enhance_contrast(img, alpha=1.1, beta=0):
#     """
#     Enhance the contrast of the image using the formula: new_image = alpha * image + beta
#     :param img: Input image
#     :param alpha: Contrast control (1.0-3.0)
#     :param beta: Brightness control (0-100)
#     :return: Contrast-enhanced image
#     """
#     return cv2.convertScaleAbs(img, alpha=alpha, beta=beta)

# def preprocess_image(img):
#     # Enhance contrast
#     contrast_img = enhance_contrast(img)

#     # Convert to grayscale
#     gray = cv2.cvtColor(contrast_img, cv2.COLOR_BGR2GRAY)

#     # Thresholding for better clarity
#     _, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

#     return thresh
