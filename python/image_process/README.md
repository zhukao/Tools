usage: padding_pic.py name.list outpath

输入：图片集的name list和转换后图片的存储路径

输出：转换后的图片

说明:
将任意分辨率的图片集处理成指定分辨率
如果输入图片分辨率小于目的，只做padding
如果输入图片分辨率大于目的，resize之后做padding
