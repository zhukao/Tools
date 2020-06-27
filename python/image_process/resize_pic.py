import os
import cv2
import argparse
import re
from pic_resize import resize
from pic_padding import padding

parser = argparse.ArgumentParser()
parser.add_argument("list", help="list of pic")
parser.add_argument("outpath", help="path of output crop pic")
args = parser.parse_args()

# pattern = re.compile('/home/kao.zhu/customerana_tools/nfs/tools/py_cv_crop_pic/mask_old/(\S+)/(\S+)')
pattern = re.compile('/home/hobot-dev/bin.fei/mask/old/(\S+)/(\S+)/normal.jpeg')

def crop(pic_path, out_path):
    # print pic_path, out_path
    out_pic_name = 'err.jpg'

    if re.match(pattern, pic_path):
        val_group = re.match(pattern, line).groups()
        path = val_group[0]
        name = val_group[1]
        out_pic_name = path + '_' + name
    else:
        print 'error ', pic_path

    # print 'pic_name:', out_pic_name

    img = cv2.imread(pic_path, 1)
    sp = img.shape
    # print sp
    height = sp[0]
    width = sp[1]
    rm_h = 0
    rm_w = 0
    out_h = 1080
    out_w = 1920
    if height > 1080:
        rm_h = (height - 1080) / 2
    if width > 1920:
        rm_w = (width- 1920) / 2

    if height < 1080:
        out_h = height
    if width < 1920:
        out_w = width

    # print rm_h, out_h, rm_w, out_w
    dst = img[rm_h:rm_h+out_h, rm_w:rm_w+out_w]
    cv2.imwrite(out_path + out_pic_name, padding(dst))

def resize_pic(pic_path, out_path, count):
    # print pic_path, out_path
    print count, ' ', pic_path
    out_pic_name = str(count) + '.jpg'
    img = cv2.imread(pic_path, 1)
    # scale to less than 1920*1080
    dst = resize(img, 1920, 1080)
    cv2.imwrite(out_path + out_pic_name + '.jpg', padding(dst, 1920, 1080))

if __name__ == '__main__':
    # img = cv2.imread("test2.jpeg", 1)
    # sp = img.shape
    # print sp
    # height = sp[0]
    # width = sp[1]
    # dst = cv2.resize(img, (1920, 1080))
    # dst = cv2.resize(img, (0, 0), fx = 1080.0/4608.0, fy = 1080.0/4608.0, interpolation=cv2.INTER_AREA)
    # print dst.shape
    # cv2.imwrite("new.jpg", dst)

    count = 0
    with open(args.list, "r") as fd_in:
        for line in fd_in.readlines():
            count += 1
            resize_pic(line.strip(), args.outpath, count)
