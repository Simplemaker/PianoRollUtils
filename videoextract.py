import cv2
from pathlib import Path
from PIL import Image


FRAME_GAP = 30

def getImages(path, printStatus=False, crop=None):
    vc = cv2.VideoCapture(path.as_posix())
    images = []
    count = 0
    while True:
        success,image = vc.read()
        if not success:
            break
        if count % FRAME_GAP == 0:
            if printStatus:
                print(f'captured image {count}')
            image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            im_pil = Image.fromarray(image)
            if(crop):
                im_pil = im_pil.crop(crop)
            images.append(im_pil)
        count += 1
    return images
