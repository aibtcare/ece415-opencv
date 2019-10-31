# import numpy as np
import cv2
from matplotlib import pyplot as plt


def binaryThreshold(img, value):

    for i, j in img:
        # if img[i, j] > value
        pass


def main():
    img = cv2.imread("Text.bmp")

    cv2.imshow("image", img)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

    # plt.hist(img.ravel(), 256, [0, 256])
    # plt.show()
    ret, thresh = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
    # cv2.imshow("threshed", thresh)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
    plt.imshow(thresh)
    plt.show()


main()
