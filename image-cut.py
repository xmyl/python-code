#!/usr/bin python3
# -*- coding: utf-8 -*-
# 将图片填充为正方形，切图为九宫格

from PIL import Image
import sys

class Image_cut(object):
    def __init__(self, path):
        self.image = Image.open(path)

    def fill_image(self, image):
        width, height = image.size
        image_length = width if width > height else height
        # 生成正方形白底的图片
        new_image = Image.new(image.mode, (image_length, image_length), color="white")
        # 合成一张图片
        if width > height:
            new_image.paste(image, (0, int((image_length - height)/2)))
        else:
            new_image.paste(image, (int((image_length - width)/2), 0))

        return new_image

    def save_images(self, image_list):
        index = 1
        # 保存图片
        for image in image_list:
            image.save('./imgs/python'+str(index) + '.png', 'PNG')
            index += 1

    def cut_image(self, image):
        width, height = image.size
        item_width = int(width / 3)
        box_list = []
        #切成九张图
        for i in range(0,3):
            for j in range(0,3):
                box = (j*item_width,i*item_width,(j+1)*item_width,(i+1)*item_width)
                box_list.append(box)

        image_list = [image.crop(box) for box in box_list]

        return image_list

    def run(self):
        image = self.fill_image(self.image)
        image_list = self.cut_image(image)
        self.save_images(image_list)

if __name__ == '__main__':
    # 传入图片路径
    path = './image-test.jpg'
    image_cut = Image_cut(path=path)
    image_cut.run()
