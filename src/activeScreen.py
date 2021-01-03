import numpy as np
import cv2
import matplotlib.pyplot as plt

def makeScreen(img):    
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    blur = cv2.GaussianBlur(gray,(5,5),2)

    th3 = cv2.adaptiveThreshold(blur,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY_INV,11,2)

    ret, res = cv2.threshold(th3, 72, 255, cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)

    median = cv2.medianBlur(res, 5)

    return res
