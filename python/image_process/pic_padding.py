import os
import cv2
#padding small pic to width == w && heitht == h
def padding(img, w, h):
    sp = img.shape
    height = sp[0]
    width = sp[1]
    pad_t = (h - height) / 2
    pad_l = (w - width) / 2
    pad_b = h - pad_t - height
    pad_r = w - pad_l - width
    pad_image = cv2.copyMakeBorder(img, pad_t, pad_b, pad_l, pad_r, cv2.BORDER_CONSTANT, value = 0)
    # print  pad_image.shape
    sp = pad_image.shape
    height = sp[0]
    width = sp[1]
    assert width == w
    assert height == h
    # print pad_image.shape
    return pad_image
