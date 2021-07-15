import cv2
import os
import sys
import random
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import math
matplotlib.use('TKAgg')


def random_crop(image, min_ratio=0.05, max_ratio=0.3):
    h, w = image.shape[:2]

    # M = cv2.getRotationMatrix2D(center, 45, 1.0) #12
    # rotated = cv2.warpAffine(image, M, (w, h)) #13
    ratio = random.random()
    scale = min_ratio + ratio * (max_ratio - min_ratio)
    image = cv2.resize(image, (int(w * scale), int(h * scale)), interpolation=cv2.INTER_LINEAR)
    return image, scale

def get_image_rotation(image):
    height, width = image.shape[:2]
    h, w = image.shape[:2]
    center = (width // 2, height // 2)
    rotation = random.randint(-180,180)
    nH=int(abs(h*math.cos(math.radians(rotation)))+abs(w*math.sin(math.radians(rotation))))
    nW=int(abs(h*math.sin(math.radians(rotation)))+abs(w*math.cos(math.radians(rotation))))

    #得到旋转矩阵，第一个参数为旋转中心，第二个参数为旋转角度，第三个参数为旋转之前原图像缩放比例
    M = cv2.getRotationMatrix2D(center, -rotation, 0.7)
    #进行仿射变换，第一个参数图像，第二个参数是旋转矩阵，第三个参数是变换之后的图像大小
    image_rotation = cv2.warpAffine(image, M, (nW, nH))
    return image_rotation

def overlay(bg, img):
    bg_h,bg_w,_ = bg.shape
    img_h,img_w,_ = img.shape
    start_0 = np.random.randint(0, bg_h-img_h)
    start_1 = np.random.randint(0, bg_w-img_w)
    starts = np.array([start_0, start_1])
    ends = starts + np.array([img_h, img_w])
    index = [slice(s, e) for s,e in zip(starts,ends)]
    mask_r = img[:,:,0] == img[:,:,1]
    mask_g = img[:,:,0] == img[:,:,2]
    mask_b = img[:,:,2] == img[:,:,1]
    mask = mask_b & mask_g & mask_b
    mask = np.where(~mask == True, 1, 0)
    mask = mask.astype(np.uint8)
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
    mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
    mask = cv2.morphologyEx(mask, cv2.MORPH_ERODE, kernel)
    mask = np.where(mask == 1, True, False)
    bg[tuple(index)][mask,:] = img[mask,:]
    # bg[tuple(index)] = img
    center = (starts+ends)//2
    center_x = center[1]/bg_w
    center_y = center[0]/bg_h
    y = img_h/bg_h
    x = img_w/bg_w
    return bg, center_x, center_y, x, y

#改变亮度和对比度
def relight(img,alpha=1,bias=0):
    w, h = img.shape[:2]
    for i in range(0,w):
        for j in range(0,h):
            for c in range(3):
                tmp=int(img[i,j,c]*alpha+bias)
                if tmp>255:
                    tmp=255
                elif tmp<0:
                    tmp=0
                img[i,j,c]=tmp
    return img
# bg = cv2.imread("../bg/1.jpg")
imgs = []
bg_imgs = []
bg_path="../bg/val2017"
path="../matting"
for x in os.listdir(path):
    if x.endswith('png'):
        imgs.append(os.path.join(path, x))

for x in os.listdir(bg_path):
    if x.endswith('jpg'):
        bg_imgs.append(os.path.join(bg_path, x))

for j in range(1000):
    img=random.sample(imgs,k=1)
    bg_img = random.sample(bg_imgs,k=1)
    img = cv2.imread(img[0])
    img = get_image_rotation(img)
    bg = cv2.imread(bg_img[0])
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    circles1 = cv2.HoughCircles(gray,cv2.HOUGH_GRADIENT,1,
    600,param1=100,param2=30,minRadius=100,maxRadius=1000)
    try:
        circles = circles1[0,:,:]
    except:
        continue
    circles = np.uint16(np.around(circles))
    i = circles[0]
    img = img[i[1]-i[2]:i[1]+i[2],i[0]-i[2]:i[0]+i[2]]
    img = relight(img, random.uniform(0.6, 1.2), random.randint(-50, 50))
    try:
        img, scale = random_crop(img)
    except:
        continue
    # cv2.circle(img,(i[0],i[1]),i[2],(255,0,0),5)
        # cv2.circle(img,(i[0],i[1]),2,(255,0,255),10)
        # cv2.rectangle(img,(i[0]-i[2],i[1]+i[2]),(i[0]+i[2],i[1]-i[2]),(255,255,0),5)
    mask_r = img[:,:,0] == img[:,:,1]
    mask_g = img[:,:,0] == img[:,:,2]
    mask_b = img[:,:,2] == img[:,:,1]
    mask = mask_b & mask_g & mask_b
    img[mask,:] = 0
    final, center_x, center_y, x, y = overlay(bg, img)
    # cv2.rectangle(final,starts[[1,0]],ends[[1,0]],(255,255,0),2)
    # plt.imshow(final[:,:,[2,1,0]])
    # plt.show()
    if not os.path.exists('./images/'):
        os.makedirs('./images/')
    cv2.imwrite('images' + '/%05d'%j + '.jpg', final)
    if not os.path.exists('./labels/'):
        os.makedirs('./labels/')
    with open('labels/' + '/%05d'%j + '.txt', "w") as f:
        f.write("{} {} {} {} {}".format(0, center_x, center_y, x, y))
    # cv2.imshow("",resized)
    # print('It`s the %s image.' % str(i))
    # i += 1
    # cv2.imshow("capture", img)

