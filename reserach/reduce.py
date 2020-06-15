import os
import cv2

folders = ["1yY7h9xkXt","4mKEIb96LV","113644aeaa","0369289ba3","bcfe3110b5","h5SGg1wbzT","h092zALqYg", "OVZjQQIIYf", "U7REmkvwZs"]
#folders = ["OVZjQQIIYf"]

def get_hw(image, width):
    sp = image.shape[:2] #height width

    height= int(sp[0]/sp[1] * width)
    return height

def resise_save(image): 
    width = 240
    print(image)
    img = cv2.imread(image)
    height = get_hw(img, width)
    img = cv2.resize(img, (width, height), cv2.INTER_NEAREST)
    # cv2.imshow(img)
    # cv2_imshow(img)
    cv2.imwrite(image, img)
    print(width, height, img.shape)

def folder_run(folder):
    for root, dirs, files in os.walk(folder, topdown=False):
        print(root, dirs, files)
        for file in files:
            try:
                resise_save(f"{folder}/{file}")
            except:
                print(file)

for folder in folders:
    folder_run(folder)
