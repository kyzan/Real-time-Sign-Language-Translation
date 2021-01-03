import numpy as np
import cv2
import matplotlib.pyplot as plt

def process(path):    
    frame = cv2.imread(path)
    
    #The classification process does not require color channels
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    #canny edge detection
    canny = cv2.Canny(gray, 15, 255)

    #complement of canny edge output
    canny_invert = canny - 255

    #gaussian blur to remove noise
    blur = cv2.GaussianBlur(gray,(5,5),2)

    #adaptive thresholding
    th3 = cv2.adaptiveThreshold(blur,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY_INV,11,2)

    #otsu binarization
    ret, res = cv2.threshold(th3, 72, 255, cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)

    #salt-pepper noise removal
    median = cv2.medianBlur(res, 5)

    fig, axs = plt.subplots(2, 2)
    fig.suptitle("Features obtained from Canny Edge Detection Algorithm")
    axs[0, 0].imshow(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
    axs[0, 0].set_title('Original Image')
    axs[0, 1].imshow(gray, cmap='gray')
    axs[0, 1].set_title('Grayscale Image')
    axs[1, 0].imshow(canny, cmap='gray')
    axs[1, 0].set_title('Canny Edge Output')
    axs[1, 1].imshow(canny_invert, cmap='gray')
    axs[1, 1].set_title('Inverted Canny Edge')
    
    plt.show()
    
    fig, axs = plt.subplots(2, 3)
    fig.suptitle("Features obtained from Custom Algorithm")
    axs[0, 0].imshow(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
    axs[0, 0].set_title('Original Image')
    axs[0, 1].imshow(gray, cmap='gray')
    axs[0, 1].set_title('Grayscale Image')
    axs[0, 2].imshow(blur, cmap='gray')
    axs[0, 2].set_title('Gaussian Blur')
    axs[1, 0].imshow(th3, cmap='gray')
    axs[1, 0].set_title('Adaptive Threshold')
    axs[1, 1].imshow(res, cmap='gray')
    axs[1, 1].set_title('Final Thresholding')
    axs[1, 2].imshow(median, cmap='gray')
    axs[1, 2].set_title('Median Blur')
    
    plt.show()

    return res


process('hand_light.jpeg')

process('hand_dark.jpeg')