import cv2
import pytesseract
"""
This code defines a function thick_font that takes a single argument, an image. The function does the following:

It negates the image using cv2.bitwise_not(image). This means that every pixel in the image is flipped, so that white pixels become black and vice versa.
It creates a kernel (a small matrix of ones) using np.ones((2,2),np.uint8). This kernel will be used for dilation, which is a morphological image processing operation that expands the white regions of the image.
It dilates the image using cv2.dilate(image, kernel, iterations=1). This expands the white regions of the image by applying the kernel to the image.
It negates the image again using cv2.bitwise_not(image). This flips the colors of the image back to their original state.
It returns the modified image using return (image).
"""
def thick_font(image):
    import numpy as np
    image = cv2.bitwise_not(image)
    kernel = np.ones((2,2),np.uint8)
    image = cv2.dilate(image, kernel, iterations=1)
    image = cv2.bitwise_not(image)
    return (image)


"""
This code defines a function tesseractOCR_img that takes a single argument, img, which is expected to be an image file path. The function does the following:

It stores the file path in a variable called filePath.
It calls pytesseract.image_to_string() with the file path and the language ('fra') as arguments. This function uses the Tesseract OCR engine to extract text from the image. The config argument is set to '--psm 6', which stands for "page segmentation mode". This tells Tesseract to treat the image as a single block of text.
It stores the extracted text in a variable called text.
It replaces all instances of '-\n' (a hyphen followed by a newline character) in text with an empty string using text.replace('-\n', ''). This removes the hyphen and newline characters from the text.
"""
def tesseractOCR_img(img):
    filePath = img
    text = str(pytesseract.image_to_string(filePath, lang='eng', config='--psm 6'))
    text = text.replace('-\n', '')
    return text

def Image_preprocessing_vehicule_license(img):
    filePath = img
    result=img
    return result


def Image_preprocessing_IDCARD(img):
    filePath = img
    result=img
    return result


