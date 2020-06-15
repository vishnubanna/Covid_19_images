import os
import cv2

folder = "Sm7vwNhHoV/"


def get_hw(image, width):
    sp = image.shape[:2] #height width

    height= int(sp[0]/sp[1] * width)
    return height

def resise_save(image): 
    width = 360
    print(image)
    img = cv2.imread(image)
    height = get_hw(img, width)
    img = cv2.resize(img, (width, height), cv2.INTER_NEAREST)
    # cv2.imshow(img)
    # cv2_imshow(img)
    cv2.imwrite(image, img)
    print(width, height, img.shape)

for root, dirs, files in os.walk(folder, topdown=False):
    print(root, dirs, files)
    for file in files:
        
        resise_save(f"{folder}/{file}")
