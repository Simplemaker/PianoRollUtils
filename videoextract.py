import cv2
from pathlib import Path

## Just get the first video in video folder
file = [f for f in Path('video').iterdir()][0] 

vc = cv2.VideoCapture(file.as_posix())

FRAME_GAP = 30
count = 0
while True:
    success,image = vc.read()
    if not success:
        break
    if count % FRAME_GAP == 0:
        p = (Path('frames') / "frame{:d}.png".format(count))

        cv2.imwrite(p.as_posix(), image)     # save frame as JPEG file
    count += 1