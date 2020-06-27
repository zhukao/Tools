import os
import cv2
#resize pic to width <= w && heitht <= h
def resize(img, w, h):
    sp = img.shape
    # print sp
    height = sp[0]
    width = sp[1]
    if height <= h :
        # print height, ' ', h
        if width <= w:
            # print width, ' ', w
            # print 'no need resize'
            return img

    print 'need resize'
    fx = float(w)/width
    fy = float(h)/height
    f_scale = min(fx, fy)
    print 'f_scale:', f_scale
    # scale to less than 1920*1080
    return cv2.resize(img, (0, 0), fx = f_scale, fy = f_scale, interpolation=cv2.INTER_AREA)