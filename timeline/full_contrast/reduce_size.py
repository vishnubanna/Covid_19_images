import cv2
import numpy 
# from google.colab.patches import cv2_imshow

folder_names = ["usa1", "usa2", "usa3", "usa4", "usa5", "usa6", "usa7", "usa8", "usa9", "usa10", "usa11", "usa12", "usa13", "usa14", "usa15", "usa16",
                "japan1", "japan2", "japan3", "japan4", 
                "italy1", "italy2", "italy3", "italy4", 
                "un1", "un2", "un3", "un4", "un5", "un6", "un7", "un8", "un9", "un10", "un11", "un12",
                "china1", "china2", "china3", "china4"]


def get_hw(image, width):
    sp = image.shape[:2] #height width

    height= int(sp[0]/sp[1] * width)
    return height

width = 360
for folder in folder_names:
    image = f"{folder}.png"
    img = cv2.imread(image)
    height = get_hw(img, width)
    img = cv2.resize(img, (width, height), cv2.INTER_NEAREST)
    # cv2.imshow(img)
    # cv2_imshow(img)
    cv2.imwrite(image, img)
    print(width, height)