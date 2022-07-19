from cv2 import blur, boundingRect
import pytesseract
import cv2

image = cv2.imread("imagens/teste.jpg")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imwrite("temp/1teste_gray.png", gray)

blur = cv2.GaussianBlur(gray, (7,7), 0)
cv2.imwrite("temp/2teste_gray_blur.png", blur)

thresh = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
cv2.imwrite("temp/3teste_thresh.png", thresh)

kernal = cv2.getStructuringElement(cv2.MORPH_RECT, (5,15))
dilate = cv2.dilate(thresh, kernal, iterations=1)
cv2.imwrite("temp/4teste_dilate.png", dilate)

contorno = cv2.findContours(dilate, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
contorno = contorno[0] if len(contorno) == 2 else cents[1]
contorno = sorted(contorno, key = lambda x: cv2.boundingRect(x)[0])
for c in contorno:
    x, y, w, h = cv2.boundingRect(c)
    if h > 250 and w > 20:
        roi = image[y:y+h, x:x+h]
        cv2.imwrite("temp/6teste_roi.png", roi)
        cv2.rectangle(image, (x,y), (x+w, y+h), (36,255,12), 2)
cv2.imwrite("temp/5.1teste_bbox.png", image) 