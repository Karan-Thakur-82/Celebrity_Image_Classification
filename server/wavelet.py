import numpy as np
import pywt
import cv2


# function takes an image and applies 2D wavelet transform
def w2d(img, mode='haar', level=1):
    #   convert image to grayscale
    imArray = img
    imArray = cv2.cvtColor(imArray, cv2.COLOR_RGB2GRAY)

    #   converts the image to a float32 type array and normalizes its values to be in the range [0, 1]
    imArray = np.float32(imArray)
    imArray /= 255;

    #   performs a 2D wavelet decomposition, returns a list of coefficients, first element is the approximation coefficients (low-frequency components), and the remaining elements are the detail coefficients (high-frequency components) at different levels.
    coeffs = pywt.wavedec2(imArray, mode, level=level)

    #   sets the approximation coefficients (the low-frequency part) to zero
    coeffs_H = list(coeffs)
    coeffs_H[0] *= 0;

    #   reconstruct the Image from the Modified Coefficients
    imArray_H = pywt.waverec2(coeffs_H, mode);

    #   convert the Image Back to 'uint8'
    imArray_H *= 255;
    imArray_H = np.uint8(imArray_H)

    return imArray_H