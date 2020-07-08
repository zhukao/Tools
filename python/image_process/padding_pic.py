import os
import cv2
import argparse
import re
from pic_padding import padding

parser = argparse.ArgumentParser()
parser.add_argument("list", help="list of pic")
parser.add_argument("outpath", help="path of output crop pic")
args = parser.parse_args()

# pattern = re.compile('/home/kao.zhu/customerana_tools/nfs/tools/py_cv_crop_pic/mask_old/(\S+)/(\S+)')
# pattern = re.compile('/home/hobot-dev/bin.fei/mask/(\S+)/(\S+)/(\S+).jpg')
pattern = re.compile('/home/hobot-dev/bin.fei/mask/young/m/(\S+)/(\S+).jpg')

frame_id = 1

def padding_pic(pic_path, out_path):
    #out_pic_name = 'err.jpg'
    '''
    if re.match(pattern, pic_path):
        val_group = re.match(pattern, line).groups()
        path1 = val_group[0]
        path2 = val_group[1]
        out_pic_name = path1 + '_' + path2
    else:
        print 'error ', pic_path
    '''
    
    global frame_id
    out_pic_name = str(frame_id)
    frame_id += 1

    img = cv2.imread(pic_path, 1)
    # sp = img.shape
    # height = sp[0]
    # width = sp[1]
    # pad_t = (1080 - height) / 2
    # pad_l = (1920 - width) / 2
    # pad_b = 1080 - pad_t - height
    # pad_r = 1920 - pad_l - width
    # pad_image = cv2.copyMakeBorder(img, pad_t, pad_b, pad_l, pad_r, cv2.BORDER_CONSTANT, value = 0)
    # print pad_image.shape
    # print out_path, out_pic_name
    # cv2.imwrite(out_path + out_pic_name + '.jpg', pad_image)

    save_name = out_path + '/' + out_pic_name + '.jpg'
    print save_name
    cv2.imwrite(save_name, padding(img, 1920, 1080))

if __name__ == '__main__':
    with open(args.list, "r") as fd_in:
        for line in fd_in.readlines():
            padding_pic(line.strip(), args.outpath)
