import cv2
from pathlib import Path
from PIL import Image

STANDARD_CROP = (0,0,1920, 512)
HD_CROP = (0,0, 1280, 360)

FRAME_GAP = 30

def getImages(path, printStatus=False, crop=None, frameskip = FRAME_GAP):
    vc = cv2.VideoCapture(path.as_posix())
    images = []
    count = 0
    while True:
        success,image = vc.read()
        if not success:
            break
        if count % frameskip == 0:
            if printStatus:
                print(f'captured image {count}')
            image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            im_pil = Image.fromarray(image)
            if(crop):
                im_pil = im_pil.crop((0, 0, im_pil.size[0], im_pil.size[1] // 2))
            images.append(im_pil)
        count += 1
    return images
