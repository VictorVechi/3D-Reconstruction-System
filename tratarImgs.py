import cv2
import numpy as np

def getImgs(name, file):
    path = "dataset/"+name+"/"+file
    f_img = cv2.imread(path, cv2.IMREAD_COLOR)
    f_img = cv2.resize(f_img, (640, 480))
    aux_img = f_img.copy()
    img, aux_img = processing(f_img, aux_img)
    return img, f_img, aux_img
    
def processing(img1, img2):
    bounding_box = [220, 121, 420-220, 373-121] 
    seg = np.zeros(img1.shape[:2],np.uint8)
    x,y,width,height = [220, 121, 420-220, 373-121]
    cv2.rectangle(img2, (x, y), (x + width, y + height), (0, 255, 255), 2)
    seg[y:y+height, x:x+width] = 1
    background_mdl = np.zeros((1,65), np.float64)
    foreground_mdl = np.zeros((1,65), np.float64)

    cv2.grabCut(img1, seg, bounding_box, background_mdl, foreground_mdl, 5, cv2.GC_INIT_WITH_RECT)
    mask_new = np.where((seg==2)|(seg==0),0,1).astype('uint8')

    img = img1*mask_new[:,:,np.newaxis]
    img_fundo = img1.copy()
    img_fundo = 255
    new_img = np.where(img!=0, img_fundo, img)
    new_img = ~new_img

    normal = cv2.cvtColor(new_img, cv2.COLOR_BGR2GRAY)
    kernel = np.ones((5,5), np.uint8)
    dilate = cv2.dilate(normal, kernel, iterations=1)
    return dilate, img2


def getContours(img, img2):
    contours, hierarchy = cv2.findContours(~img, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    max_area = -1
    for c in range(len(contours)):
        area = cv2.contourArea(contours[c])
        if area>max_area:
            cnt = contours[c]
            max_area = area

    x, y, w, h = cv2.boundingRect(cnt)
    cv2.rectangle(img2, (x, y), (x + w, y + h), (0, 0, 255), 1)
    return x, y, w, h, img2


def showResultado(img, x, y, w, h):
    imgCropped = img[y: y + h, x: x + w]
    imgResult = np.zeros((480, 640, 3), np.uint8)
    imgResult[y: y + h, x: x + w] = imgCropped
    return imgResult
    
