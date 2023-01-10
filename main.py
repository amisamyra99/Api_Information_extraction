
from  image_processing import *

image_file= "Data/ID/CIN.jpg"
img=cv2.imread(image_file)
im2=cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
#gray=cv2.cvtColor(im2,cv2.COLOR_BGR2GRAY)
#kernel=cv2.getStructuringElement(cv2.MORPH_RECT,(3,13))
#thresh=cv2.threshold(gray,0,255,cv2.THRESH_BINARY_INV +cv2.THRESH_OTSU)[1]
#dilate=cv2.dilate(thresh,kernel,iterations=1)
#test=cv2.fastNlMeansDenoising(dilate,None,10,7,21)
denoised = cv2.medianBlur(im2, 5)
#cv2.imwrite('test8.png',denoised)
ocr_result2=pytesseract.image_to_string(denoised,lang='fra')
ocr_result=tesseractOCR_img(denoised)

print (ocr_result2)
print(ocr_result)
print('hello')



